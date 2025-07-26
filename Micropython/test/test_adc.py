from machine import Pin, ADC
import time

# ADC
a0 = Pin(26, Pin.IN) # his is needed to turn input to high impedance
a1 = Pin(27, Pin.IN) # this is needed to turn input to high impedance 
a2 = Pin(28, Pin.IN)
adc0 = ADC(0)
adc1 = ADC(1)
adc2 = ADC(2)
adc = [adc0, adc1, adc2]

def readADC():
    voltages = []
    for a in adc:
        v16 = a.read_u16()
        v = v16 * 3.3 / (65535)
        voltages.append(v)
    return voltages

while True:
    voltages = readADC()
    for v in voltages:
        print("%2.3f" % v + '\t', end = "")
    print()
    time.sleep(0.5)
    
