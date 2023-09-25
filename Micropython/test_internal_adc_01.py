from machine import Pin, ADC
import time
a = Pin(26, Pin.IN)				  # this is needed to turn input to high impedance   
adc0 = ADC(0)		# Pin 31

offset0 = -0.006
k0 = 0.98522

def read_ADC0(nb):
    v = 0
    for i in range(0,nb):
        v += adc0.read_u16()
    v = v/nb * 3.3 / (65535)
    v += offset0
    v *= k0
    return v
    
        
    

while True:
	#v = adc.read_u16() * 3.3 / (65535)
	v = read_ADC0( 7)
	vs = "%1.3f" % v
	print(vs)
	time.sleep(0.5)