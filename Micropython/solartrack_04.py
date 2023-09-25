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
pwmgen = PWMc(PWMpin, freq= PWMfreq)



#-------------------------------------------------------------------------------    
class MPPT(Measure_VIP):
    def __init__(self, adc0, adc1,  pwmgen, oled = None):
        Measure_VIP.__init__(self, adc0, adc1, oled)      # inherits everythin from Measure_VIP
        
        # PWM generator:
        self.pwmgen = pwmgen
        self.pwmval = 0
        self.pwm_min = 0.1
        self.pwm_max = 0.5
        self.pwm_step = 0.01
      
    def set_pwm(self, pwmval):
        self.pwmgen.set_pwm(pwmval)
        self.pwmval = pwmval
    
    def mpp_track(self, printflag = True):
        # Tracks maximum power point in PWM range between self.pwm_min and  self.pwm_max  using  self.pwm_step 
        # returns p2max, p1max, pwmopt, i1max, i2max, pwmopt
        # printflag decides if values are printed 
        ## Note: Only in this function pwm values are int in % because range is used
       
        
        # range accepts only int, so convert to %:
        pwm_percent_min = int(self.pwm_min * 100)
        pwm_percent_max = int(self.pwm_max * 100)
        pwm_percent_step = int(self.pwm_step * 100)
        pwm_percent_range = range(pwm_percent_min, pwm_percent_max , pwm_percent_step)
        
        power_max = 0
        pwmopt_percent = 0
        vmax = 0
        imax = 0
        for pw in pwm_percent_range:
            
            self.set_pwm(pw/100)
            v, i, power = meas.get_VIP()
            
            if power > power_max:
                            
                vmax = v
                imax = i
                power_max = power
                pwmopt_percent = pw
            
            if printflag:    
                print( '# PWM track', '\t', pw,'\t', '%2.2f' % v, '\t', '%2.2f' % i, '\t', '%3.0f' % power, '\t', '%3.0f' % power)
            
        self.pwmval = pwmopt_percent/100
        self.set_pwm(self.pwmval)
        
        if printflag:
            print("## PWM = %2.0i" % pwmopt_percent, "%") 
            print("## P = %2.0f" % power_max, "W")
            print()
            
        return power_max, pwmopt_percent, vmax, imax
#------------------------------------------------------------------------------
#meas = Measure_VIP(adc0, adc1)           # without oled
#meas = Measure_VIP(adc0, adc1, oled)      # with oled
meas = MPPT(adc0, adc1, pwmgen, oled)
meas.nbmean = 100


i = 0
while True:
    if ( i % 10) == 0:
        meas.mpp_track()
    
    meas.get_VIP()
    meas.print_VIP()
    meas.print_oled()
    time.sleep(2)
    i+= 1
    
    
