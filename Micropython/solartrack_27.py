
'''

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
#from temperature_sensors import TemperatureSensors
from ds18x20_jc03 import TemperatureSensors
from MPPT_01 import *   
#-------------------------------------------------------------------------------
# Parameters loaded from config.py

from config import *
print("## Loading parameters from config.py")


# ----------------------------------------------------------------------------------

# Hardware parameters:
# Temperature sensors
ds_pin = Pin(15)

# Buttons
btn1 = Pin(16, Pin.IN, Pin.PULL_UP)      
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

# Watchdog only when WDT jumper is set
jp_WDT = Pin(14, Pin.IN, Pin.PULL_UP)
if jp_WDT.value()==0:
    from machine import WDT
    wdt = WDT(timeout=6000)  # enable it with a timeout of 6s, max. = ca. 8s


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

# Serial datat to HA on UART1:
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5), bits=8, parity=None, stop=1)
uart1.write("# SOLAR TRACK\n")

# ----------------------------------------------------------------------------------
# Define class instances for temperature sensors + MPPT

# temperature sensors:
sensors = TemperatureSensors(ds_pin)
sensors.print_info()

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
    global n_rows
    if n_rows % print_header_every == 0:
        print("# i",  "V2/V",  "I2/A",  "P2/W",   "PWM",  "E/Wh", "TMOS", "TD", "TL", "TC2", "TMmax",
              "TDmax", "TLmax", "TC2max", "P2max/W", "Limited", sep = '\t')
    
    
    print(i,  "%2.2f" % V,  "%2.2f" % I,  "%3.0f" % P,  " %1.3f" % mppt.pwmval,
          " %i" % EnergyWh, stemperatures +  sensors.get_maxtemps_as_string() +  "%i " % maxpower,
          mppt.powerlimit_reached, sep = '\t')
    n_rows +=  1


def print_my_values_uart1( additional = ""):
    # i	  V   I   P   PWM   EWh   TMOS   TD   TL   TC2   Pmax   Powerlim   
    s = str(i) +'\t' +  "%2.2f" % V +'\t'+  "%2.2f" % I + '\t' + "%3.0f" % P + '\t'
    s += " %1.3f" % mppt.pwmval + '\t'+ " %i" % EnergyWh + '\t' + stemperatures + '\t'
    s +=    "%i " % maxpower + '\t' + str( mppt.powerlimit_reached)
    s +=   '\r\n'
    uart1.write(s)
    


## Use dedicated oled function though MPPT has one
def print_my_oled(mppt, page = 0, additional = ""):
        # Display values if oled is defined
        if mppt.oled:
            if page == 0:
                V, I, P = mppt.values
                mppt.oled.clear()
                
                s = '\tP = %2.0fW' % P
                s += '\tV = %2.2fV' % V
                
                s +=  '\tI = %2.2fA' % I
                s += "\tPWM: %1.2f" % mppt.pwmval
                
                
                stemp = sensors.get_as_string(tformat = '%2.0f')
        
                stemp = stemp.replace('\t', '  ')
                s += '\t' + stemp
                mppt.oled.print_s(s)
            
            if page == 1:
                stemp = sensors.get_maxtemps_as_string()
                stemp = "Max. Temps\tFET DIODE COIL\t" + stemp
                mppt.oled.print_s(stemp)
#------------------------------------------------------------------------------


def calc_powerlimit(V):
    if V <= U1:
        pl = powerlimit
    else:    
        pl = 1 -(V - U1)/(U2-U1)
        pl = pl * powerlimit
    return pl
#--------------------------------------------------------
def check_buttons():
        
    if btn1.value():
        page = 0
    else:
        page = 1
    if btn2.value() == 0:
        #page = 2
        sys.exit()
    
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
#------------------------------------------------------------------

# Remote control functions:
def track():
    mppt.mpp_track(printflag = True)

# Check incoming commands
# Ctrl-C, Ctrl-D, * = CMD, ? = HELP
def check_uart():
    #  STOP or RESET via RxD0:
    if uart0.any():
        inp = uart0.read()
        # stop running program or reset:
        if b'\04' in inp:
            uart0.write("## RESET\n")
            time.sleep(0.1)
            soft_reset()
        elif b'\03' in inp:
            uart0.write("## STOP PROGRAM\n")
            #break
            sys.exit()
        elif b'*' in inp:
            s = input('CMD: ')
            print('#', s)
            try:
                exec(s)
            except:
                print("# CMD ERROR")
        elif b'?' in inp:
            print_help()
            
# Display helpfile over UART + USB            
def print_help():
    try:
        with open(helpfile, "r") as f:
            h = f.read()
            print(h)
    except:
        print ("ERROR reading ", helpfile)
    s = input("Any key to continue")
    
#------------------------------------------------------------------------------

i = 0
n_rows = 0
maxpower = 0              # max power over whole operation
interval = 0
time_before = time.time()
EnergyWs = 0
page = 0
#--------------------------------------------------------------------------


def main_loop():
    global i, interval,  page, n_rows
    global V, I, P, mppt,  EnergyWs, EnergyWh, maxpower, stemperatures
    
    last_t = time.ticks_ms()
    
    while True:
        
        # only when WDT is active:
        try:
            wdt.feed()
        except:
            pass
        
        # Every second do this:
        current_t = time.ticks_ms()
        if time.ticks_diff(current_t, last_t) >= 1000:
        ## if interval >= dt:
        
            blink.blink(1, dt = 0.02)
      
            check_temperature()
        
            # Get voltage, current, power, energy
            V, I, P = mppt.get_VIP()
            EnergyWs += P * 1                        # 1s!
            EnergyWh = EnergyWs / 3600
            
            # MPP track every track_time:
            if ( i % track_interval) == 0:
                print("## Tracking")
                mppt.mpp_track(printflag = False)
            
                        
            # Remember max power over whole operation
            if P > maxpower:
                maxpower = P
            
            # Eventually reduce power if battery nearly full:
            P_lim = calc_powerlimit(V)
            mppt.powerlimit = P_lim
            
            
            # track again if power exceeds powerlimit -> limit power:
            if P > mppt.powerlimit:
                mppt.mpp_track(printflag = False)    
            
            
            if ( i % print_interval):
                # Print + display values
                print_my_values( )
                print_my_values_uart1()
                
            ### print_Tx0_table(i, V, I, P, mppt.pwmval, additional = str(EnergyWh) +  '\t' + stemperatures)
            #print_my_oled(mppt, page = page, additional = 'Pmax = %2.0fW' % maxpower)
                
            print_my_oled(mppt, page = page, additional = "")
           
            # Nb of measurement + time           
            i+= 1
            ## time1= time.time()
            last_t = current_t
      
        page = check_buttons()
        
        check_uart()
        
        # prevent the loop from turning too fast:    (tip from ChatGPT)
        time.sleep_ms(100)
    
main_loop()    

