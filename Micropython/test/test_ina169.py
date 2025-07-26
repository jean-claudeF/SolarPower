from machine import Pin, ADC
import time

# ADC
a0 = Pin(26, Pin.IN)				  # this is needed to turn input to high impedance
a1 = Pin(27, Pin.IN)				  # this is needed to turn input to high impedance 
adc0 = ADC(0)		# Pin 31
adc1 = ADC(1)		# Pin 32



class Measure_VI():
    def __init__(self, adc0, adc1):
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
            v += adc1.read_u16()
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


def print_format(vvect):
    # print elements of vvect (list of voltages) in tabular form
    
    for v in vvect:
        vs = "%1.3f" % v
        print(vs, end = "\t")
    print()

#-----------------------

meas = Measure_VI(adc0, adc1)


while True:
    i = meas.get_I()
    #v = meas.readADC1(1)
    v = meas.get_V()
    
    #v = readADC0(10)
    #v = v * 10 * 10.2866779
    #print("%2.2f" % v)
    print("%2.2f" % i, '\t', "%2.3f" % v)
    time.sleep(0.5)
    
