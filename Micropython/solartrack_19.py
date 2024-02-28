
'''
solartrack_19.py       27.2.2024
Changed:
blink every s
Class TemperatureSensors -> file temperature_sensor.py
Removed manual PWM
Power limit
Global variables
MPPT class moved to module MPPT_01.py
Config paramters moved to config.py 
'''

import onewire, ds18x20
from machine import Pin, ADC, I2C, UART, reset, soft_reset
import sys
import time
import os

from OLED_03 import OLED

from measure_vip import Measure_VIP        # Measure V2, I2, P2 with INA169
from pwmc import PWMc                      # PWM generator
import blink
from temperature_sensors import TemperatureSensors
from MPPT_01 import *   
#-------------------------------------------------------------------------------
# Parameters loaded from config.py, or default values if no config.py
try:
    from config import *
except:    
    # load default parameters:
    use_oled = True
    track_time = 10                       # track every xx seconds
    dt = 1                                # display every dt 

    pwm_min = 0.1
    pwm_max = 0.6
    pwm_step = 0.01
    powerlimit = 900        # Don't exceed this power, exit track loop when exceeded
    PWMfreq = 16E3

    vent_on_temp = 45       # switch on ventilator at this temperature

    baud = 115200           # for UART0
    
    

# ----------------------------------------------------------------------------------
# Hardware parameters:
# Temperature sensors
ds_pin = Pin(15)

# Buttons
btn1 = Pin(16, Pin.IN, Pin.PULL_UP)      # oled switch pages
btn2 = Pin(17, Pin.IN, Pin.PULL_UP)

led = Pin(25, Pin.OUT)

# ADC
a0 = Pin(26, Pin.IN)       # this is needed to turn input to high impedance
a1 = Pin(27, Pin.IN)       # this is needed to turn input to high impedance
a2 = Pin(28, Pin.IN)
adc0 = ADC(0)             # Pin 31           Current I2
adc1 = ADC(1)             # Pin 32           Voltage V2
adc2 = ADC(2)             # Pin 34           Manual PWM pot
i2c_channel = 0
sclpin = 9
sdapin = 8
i2c = I2C(i2c_channel, scl=Pin(sclpin), sda=Pin(sdapin))

# PWM
PWMpin = 3
pwmgen = PWMc(PWMpin, freq= PWMfreq)

# Jumper auto PWM / manual PWM used now to activate remote REPL
### pwm_manual = Pin(14, Pin.IN, Pin.PULL_UP)


# OLED
if use_oled:
    try:
        oled = OLED(128, 64, i2c, rotate = 180)
        oled.clear()
    except:
        print("# NO OLED ?")
        oled = None
else:
    oled = None
    
# ventilator
vent_pin = 18
ventilator = Pin(vent_pin, Pin.OUT)

# serial data over Tx on Pin1:
uart0 = UART(0, baudrate=baud, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
uart0.write("# SOLAR TRACK\n")

# With Micropython 1.23: Communication over serial
os.dupterm(uart0, 0)

# ----------------------------------------------------------------------------------
# Define class instances for temperature sensors + MPPT

# temperature sensors:
sensors = TemperatureSensors(ds_pin)
print("# ", sensors.nbsensors, " temperature sensors:")
print("# ", sensors.addresses)

# voltage + current sensors:
mppt = MPPT(adc0, adc1, pwmgen, oled, powerlimit = powerlimit)
mppt.nbmean = 10
mppt.pwm_min = pwm_min
mppt.pwm_max = pwm_max
mppt.pwm_step = pwm_step

mppt.set_pwm(0)

#----------------------------------------------------------------------------------------

## Use a dedicated print function, though MeasureVIP has one            
def print_my_values( additional = ""):
    if i % 10 == 0:
        print("# i",  "V2/V",  "I2/A",  "P2/W",   "PWM",  "E/Wh", "TMOS", "TD", "TCOIL", "TMmax", "TDmax", "TCmax", "P2max/W", "Limited", sep = '\t')
    #print(i, '\t', "%2.2f" % V, '\t', "%2.2f" % I, '\t', "%3.0f" % P, " ## %3.1f " % maxpower, " %1.2f" % mppt.pwmval, additional , "\t", sensors.get_maxtemps_as_string())
    
    print(i,  "%2.2f" % V,  "%2.2f" % I,  "%3.0f" % P,  " %1.3f" % mppt.pwmval,  " %i" % EnergyWh, stemperatures +  sensors.get_maxtemps_as_string() +  "%i " % maxpower,
          mppt.powerlimit_reached, sep = '\t')



## Use dedicated oled function though MPPT has one
def print_my_oled(mppt, page = 0, additional = ""):
        # Display values if oled is defined
        if mppt.oled:
            if page == 0:
                V, I, P = mppt.values
                mppt.oled.clear()
                
                s = '\tV = %2.2fV' % V
                s +=  '\tI = %2.2fA' % I
                s += "\tPWM: %1.2f" % mppt.pwmval
                s += '\tP = %2.0fW' % P
                s += '\t' + additional
                mppt.oled.print_s(s)
            if page == 1:
                stemp = sensors.get_as_string()
                stemp = "Temperatures\tFET DIODE COIL\t" + stemp
                mppt.oled.print_s(stemp)
            if page == 2:
                stemp = sensors.get_maxtemps_as_string()
                stemp = "Max. Temps\tFET DIODE COIL\t" + stemp
                mppt.oled.print_s(stemp)
#------------------------------------------------------------------------------



def check_buttons():
    
    
        
    if btn1.value():
        page = 0
    else:
        page = 1
    if btn2.value() == 0:
        page = 2
    
    return page


def check_temperature():
    # get temperatures and switch ventilator
    global stemperatures
    sensors.convert()
    stemperatures = sensors.get_as_string()
    ga, a = sensors.checktemp(vent_on_temp)
    if ga:
       ventilator.on()
    else:
        ventilator.off()
        
def check_uart():
    #  STOP or RESET via RxD0:
    if uart0.any():
        inp = uart0.read()
        # stop running program or reset:
        if b'\04' in inp:
            uart0.write("## RESET\n")
            time.sleep(0.1)
            soft_reset()
        if b'\03' in inp:
            uart0.write("## STOP PROGRAM\n")
            #break
            sys.exit()
        
#------------------------------------------------------------------------------

i = 0
maxpower = 0              # max power over whole operation
interval = 0
time_before = time.time()
EnergyWs = 0
page = 0
#--------------------------------------------------------------------------
time1 = time.time()

def main_loop():
    global i, interval, time1, page
    global V, I, P, mppt,  EnergyWs, EnergyWh, maxpower, stemperatures
    
    while True:
        
        interval = time.time() - time1 
        if interval >= dt:
        
            blink.blink(1, dt = 0.01)
      
            check_temperature()
        
            # MPP track every track_time:
            if ( i % track_time) == 0:
                mppt.mpp_track()
            
            # Get voltage, current, power, energy
            V, I, P = mppt.get_VIP()
            EnergyWs += P * interval
            EnergyWh = EnergyWs / 3600
            
            # Remember max power over whole operation
            if P > maxpower:
                maxpower = P
                
            # track again if power exceeds powerlimit -> limit power:
            if P > powerlimit:
                mppt.mpp_track()    
            
            # Print + display values
            print_my_values( )
            ### print_Tx0_table(i, V, I, P, mppt.pwmval, additional = str(EnergyWh) +  '\t' + stemperatures)
            print_my_oled(mppt, page = page, additional = 'Pmax = %2.0fW' % maxpower)
           
            # Nb of measurement + time           
            i+= 1
            time1= time.time()
      
        page = check_buttons()
        
        check_uart()
        
    
main_loop()    

