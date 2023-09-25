from machine import Pin, ADC, I2C
import time
from OLED_03 import OLED
from pwmc import PWMc



class Measure_VIP():
    '''Read V, I from adc0, adc1 and calculate P
       values can also b printed and displayed on OLED
       adc0 -> I
       adc1 -> V'''
    
    def __init__(self, adc0, adc1, oled = None):
        self.oled = oled
        self.adc0 = adc0
        self.adc1 = adc1
        self.offset0 = -0.006
        self.k0 = 0.98522
        self.offset1 = -0.007
        self.k1 = 0.98791
        self.ifactor = 10.2866779
        self.vfactor = 21
        self.nbmean = 3

    def readADC0(self, nb):
        v = 0
        for i in range(0,nb):
            v += self.adc0.read_u16()
        v = v/nb * 3.3 / (65535)
        v += self.offset0
        v *= self.k0
        return v

    def readADC1(self, nb):
        v = 0
        for i in range(0,nb):
            v += self.adc1.read_u16()
        v = v/nb * 3.3 / (65535)
        v += self.offset1
        v *= self.k1
        return v
    
    def get_I(self):
        v = self.readADC0(self.nbmean)
        i = v * self.ifactor
        return i
    
    def get_V(self):
        v = self.readADC1(self.nbmean)
        v = v * self.vfactor
        return v        

    def get_VIP(self):
        i = self.get_I()
        v = self.get_V()
        p = v * i
        self.i = i
        self.v = v
        self.p = p
        self.values = v, i, p
        return v, i, p
    
    def print_VIP(self):
        print("%2.3f" % self.v, '\t', "%2.3f" % self.i, '\t', "%3.1f" % self.p)
        
    def print_oled(self):
        # Display values if oled is defined
        if self.oled:
            v, i, p = self.values
            self.oled.clear()
            
            s = '\tV = %2.2fV' % v
            s +=  '\tI = %2.2fA' % i
            s += '\tP = %2.0fW' % p
           
            self.oled.print_s(s)    
#-------------------------------------------------------------------------------    

def measure_loop():
    
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
    
    #meas = Measure_VIP(adc0, adc1)           # without oled
    meas = Measure_VIP(adc0, adc1, oled)      # with oled
    meas.nbmean = 10
    
    while True:
        v, i, p = meas.get_VIP()
        meas.print_VIP()
        meas.print_oled()
        time.sleep(1)
    


if __name__ == "__main__":
    measure_loop()
    