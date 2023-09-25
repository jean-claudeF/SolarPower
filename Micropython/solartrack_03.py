from machine import Pin, ADC, I2C
import time
from OLED_03 import OLED
from measure_vip import Measure_VIP
from pwmc import PWMc

# ADC
a0 = Pin(26, Pin.IN)				  # this is needed to turn input to high impedance
a1 = Pin(27, Pin.IN)				  # this is needed to turn input to high impedance 
adc0 = ADC(0)		# Pin 31
adc1 = ADC(1)		# Pin 32
i2c_channel = 0
sclpin = 9
sdapin = 8
i2c = I2C(i2c_channel, scl=Pin(sclpin), sda=Pin(sdapin))
oled = OLED(128, 64, i2c, rotate = 180)
oled.clear()
PWMpin = 3
PWMfreq = 16E3
pw = PWMc(PWMpin, freq= PWMfreq)
pwmgen = pw


#-------------------------------------------------------------------------------    


#meas = Measure_VIP(adc0, adc1)           # without oled
meas = Measure_VIP(adc0, adc1, oled)      # with oled

while True:
    v, i, p = meas.get_VIP()
    meas.print_VIP()
    meas.print_oled()
    time.sleep(0.5)
    
