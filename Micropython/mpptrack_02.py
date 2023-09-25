'''Measure voltages, currents and power for a quadrupole
   Track  MPP 
'''



# ADC factors + offset:
k0 = 1.02584814     
k1 = 1.016  
k2 = 21*1.007
k3 = 21*1.007
offset0 = 0.00085
offset1 = 0.0008

#--------------------------------------------------------------

from ADC_ADS1115_03 import ADS1115
import time
from machine import Pin, I2C
from OLED_03 import OLED
from pwmc import PWMc

d15 = Pin(15, Pin.OUT)          # for debugging purposes
i2c_channel = 0
sclpin = 9
sdapin = 8
i2c = I2C(i2c_channel, scl=Pin(sclpin), sda=Pin(sdapin))
adc = ADS1115(i2c, address = 72, gain = 1)
oled = OLED(128, 64, i2c, rotate = 180)
oled.clear()
PWMpin = 3
PWMfreq = 16E3
pw = PWMc(PWMpin, freq= PWMfreq)
pwmgen = pw

#--------------------------------------------------------------

class Measure4pole():
    def __init__(self, adc, pwmgen, adcrate = 4, nbmean = 3 , oled = None):
        # Hardware related:
        self.adc = adc
        self.pwmgen = pwmgen
        self.oled = oled
        self.adcrate = adcrate
        self.nbmean = nbmean
        
        # Default: calculated values using ADC factors + offset:
        self.cooked = True
        
        # PWM generator:
        self.pwmval = 0
        self.pwm_min = 0.1
        self.pwm_max = 0.5
        self.pwm_step = 0.01
        
        # Use ADC factors + offset
        self.set_calibration()
        
        # self.values = i1, i2, v1, v2, p1, p2, eta
        self.values = ()
        
        # for print: counter + title every e.g. 10 lines
        self.print_counter = 0
        self.title_every = 10
        
    
    def set_calibration(self, k0=1, k1=1, k2=21, k3=21, offset0=0, offset1 = 0):
        # set default calibration by using set_calibration() or use variables
        self.k0 = k0
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.offset0 = offset0
        self.offset1 = offset1
        
        
    def measure(self):
        # Measure currents, voltages, powers and efficiency
        self.rawvalues = adc.read_all_meanvalue(rate = self.adcrate,  nb = self.nbmean)
        i1, i2, v1, v2, p1, p2, eta = self.calculate()
        self.values = i1, i2, v1, v2, p1, p2, eta
        return i1, i2, v1, v2, p1, p2, eta
    
    def mpp_track(self, printflag = True):
        # Tracks maximum power point in PWM range between self.pwm_min and  self.pwm_max  using  self.pwm_step 
        # returns p2max, p1max, pwmopt, i1max, i2max, pwmopt
        # printflag decides if values are printed 
        ## Note: Only in this function pwm values are int in % because range is used
        p2max = 0
        pmin = int(self.pwm_min * 100)
        pmax = int(self.pwm_max * 100)
        step = int(self.pwm_step * 100)
        for p in range(pmin, pmax , step):
            
            self.set_pwm(p/100)
            i1, i2, v1, v2, p1, p2, eta = self.measure()
            
            if p2 > p2max:
                            
                i1max = i1
                i2max = i2
                p1max = p1
                p2max = p2
                pwmopt = p
            
            if printflag:    
                print( '# PWM track', '\t', p,'\t', '%2.2f' % i1, '\t', '%2.2f' % i2, '\t', '%2.2f' % v1, '\t', '%2.2f' % v2, '\t', '%3.0f' % p1, '\t', '%3.0f' % p2, '\t', '%1.2f' % eta)
            
        self.pwmval = pwmopt/100
        pw.set_pwm(pwmopt/100)
    
        return p2max, p1max, pwmopt, i1max, i2max, pwmopt
    
    def print_values(self):
        # prints counter, pwm, i1, i2, v1, v2, p1, p2, eta
        i1, i2, v1, v2, p1, p2, eta = self.values
        pwm = self.pwmval * 100
        
        if (self.print_counter % self.title_every == 0):
            print('# i \t pwm%', '\t',  'I1/A', '\t', 'I2/A', '\t', 'V1/V', '\t', 'V2/V', '\t', 'P1/W', '\t', 'P2/W', '\t', 'eta')
        print(self.print_counter, '\t','%2.0f' % pwm, '\t',  '%2.2f' % i1, '\t', '%2.2f' % i2, '\t', '%2.2f' % v1, '\t', '%2.2f' % v2, '\t', '%3.0f' % p1, '\t', '%3.0f' % p2, '\t', '%1.2f' % eta)
        self.print_counter += 1
    
    def calculate(self):
        
        v = self.rawvalues
        for i in range(0,3):
        
            if v[i] <= 0:
                v[i] = 0
        
            if self.cooked == True:
                v[0] = v[0] - self.offset0
                v[1] = v[1] - self.offset1
                            
                i1 = v[0] *10 * self.k0 
                i2 = v[1] *10 * self.k1 
                v1 = v[2] * self.k2
                v2 = v[3] * self.k3
            else:
                i1 = v[0]
                i2 = v[1]
                v1 = v[2]
                v2 = v[3]
            
            if v1 <0:
                v1 = 0
            if v2 <0:
                v2 = 0    
                
            p1 = v1 * i1
            p2 = v2 * i2
        
            if (p1 >=  p2) & (p2 > 0):
                eta = p2/p1
            else:
                eta = 0
        return i1, i2, v1, v2, p1, p2, eta
    
    def set_pwm(self, pwmval):
        self.pwmgen.set_pwm(pwmval)
        self.pwmval = pwmval
        

    def print_oled(self):
        # Display values if oled is defined
        if self.oled:
            i1, i2, v1, v2, p1, p2, eta = self.values
            self.oled.clear()
            s =  'I1 = %2.2fA' % i1
            s += '\tI2 = %2.2fA' % i2
            s += '\tV1 = %2.2fV' % v1
            s += '\tV2 = %2.2fV' % v2
            s += '\tP1 = %2.0fW' % p1
            s += '\tP2 = %2.0fW' % p2
            
            self.oled.print_s(s)
    
#--------------------------------------------------------------
def print_oled_last(p2max, pwmopt):
    oled.print("MPP tracking")
    s = "Last values:"
    s += '\tP2max = %2.0fW' % p2max
    s += '\tPWM = %2.0f' % pwmopt + "%"
    oled.print_s(s)
#            

# Define object with or without connected OLED:
m4p = Measure4pole(adc, pwmgen, oled = oled)
#m4p = Measure4pole(adc, pwmgen, oled = None)

m4p.set_calibration(k0, k1, k2, k3, offset0, offset1)
m4p.set_pwm(0.3)

# Track MPP, set PWM accordingly in regular intervals
# Display values
p2max = 0
pwmopt = 0
i = 0
while True:
    if i % 10 == 0:
        if oled:
            print_oled_last(p2max, pwmopt)    
            
        p2max, p1max, pwmopt, i1max, i2max, pwmopt = m4p.mpp_track()
        
        
            
        
    ##i1, i2, v1, v2, p1, p2, eta = m4p.measure()
    m4p.measure()
    m4p.print_values()
    m4p.print_oled()
    i += 1
    time.sleep(1)
        


    
            
        
        
    
