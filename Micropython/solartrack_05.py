
from machine import Pin, ADC, I2C
import time
from OLED_03 import OLED
from measure_vip import Measure_VIP        # Measure V2, I2, P2 with INA169
from pwmc import PWMc                      # PWM generator

# User defined parameters (editable)
use_oled = True
track_time = 10                       # track every xx seconds

pwm_min = 0.1
pwm_max = 0.6
pwm_step = 0.01
# ----------------------------------------------------------------------------------
# Hardware parameters:

# ADC
a0 = Pin(26, Pin.IN)				  # this is needed to turn input to high impedance
a1 = Pin(27, Pin.IN)				  # this is needed to turn input to high impedance
a2 = Pin(28, Pin.IN)
adc0 = ADC(0)		# Pin 31           Current I2
adc1 = ADC(1)		# Pin 32           Voltage V2
adc2 = ADC(2)       # Pin 34           Manual PWM pot
i2c_channel = 0
sclpin = 9
sdapin = 8
i2c = I2C(i2c_channel, scl=Pin(sclpin), sda=Pin(sdapin))

# PWM
PWMpin = 3
PWMfreq = 16E3
pwmgen = PWMc(PWMpin, freq= PWMfreq)

# Jumper auto PWM / manual PWM
pwm_manual = Pin(14, Pin.IN, Pin.PULL_UP)


# OLED
if use_oled:
    oled = OLED(128, 64, i2c, rotate = 180)
    oled.clear()
else:
    oled = None
#-------------------------------------------------------------------------------
# MPPT class    
    
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
        
        if printflag:    
                print( '# PWM track', '\t', "PWM%",'\t', "V2/V", '\t', "I2/A", '\t', "P2/W", '\t', "P2max")
        
        power_max = 0
        pwmopt_percent = 0
        vmax = 0
        imax = 0
        for pw in pwm_percent_range:
            
            self.set_pwm(pw/100)
            time.sleep(0.01)                    # allow some time for results to be stable
            v, i, power = meas.get_VIP()
            
            if power > power_max:
                            
                vmax = v
                imax = i
                power_max = power
                pwmopt_percent = pw
            
            if printflag:    
                print( '# PWM track', '\t', pw,'\t', '%2.2f' % v, '\t', '%2.2f' % i, '\t', '%3.0f' % power, '\t', '%3.0f' % power_max)
            
        self.pwmval = pwmopt_percent/100
        self.set_pwm(self.pwmval)
        time.sleep(0.01)
        
        if printflag:
            print("## PWM = %2.0i" % pwmopt_percent, "%") 
            print("## P = %2.0f" % power_max, "W")
            print()
            
        return power_max, pwmopt_percent, vmax, imax
    
    ## overwrite print_oled function from Measure_VIP
    ## to add print PWM value
    def print_oled(self):
        # Display values if oled is defined
        if self.oled:
            v, i, p = self.values
            self.oled.clear()
            
            s = '\tV = %2.2fV' % v
            s +=  '\tI = %2.2fA' % i
            s += "\tPWM: %1.3f" % self.pwmval
            s += '\tP = %2.0fW' % p
          
            self.oled.print_s(s)
            
            
            
#------------------------------------------------------------------------------
def print_values(i):
    if i % 10 == 0:
        print("# i", '\t', "V2/V", '\t', "I2/A", '\t', "P2/W")
    print(i, '\t', "%2.3f" % meas.v, '\t', "%2.3f" % meas.i, '\t', "%3.1f" % meas.p)

#meas = Measure_VIP(adc0, adc1)           # without oled
#meas = Measure_VIP(adc0, adc1, oled)      # with oled
meas = MPPT(adc0, adc1, pwmgen, oled)
meas.nbmean = 10
meas.pwm_min = pwm_min
meas.pwm_max = pwm_max
meas.pwm_step = pwm_step

meas.set_pwm(0)


i = 0
while True:
    if ( i % track_time) == 0:
        if pwm_manual.value():
            meas.mpp_track()
       
    
    meas.get_VIP()
    ## meas.print_VIP()
    # or:
    print_values(i)
    meas.print_oled()
    
    if pwm_manual.value() == 0:
        # PWM pot
        vpwm = adc2.read_u16() / 65535
        pwmgen.set_pwm(vpwm)
               
        time.sleep(0.05)
    else:
        time.sleep(1)
    
    
    i+= 1
    
    
