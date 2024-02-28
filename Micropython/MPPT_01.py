# MPPT class    

from machine import Pin, ADC, I2C, UART, reset
import time
from OLED_03 import OLED
from measure_vip import Measure_VIP        # Measure V2, I2, P2 with INA169
from pwmc import PWMc                      # PWM generator


class MPPT(Measure_VIP):
    def __init__(self, adc0, adc1,  pwmgen, oled = None, powerlimit = 500):
        Measure_VIP.__init__(self, adc0, adc1, oled)      # inherits everythin from Measure_VIP
        
        # PWM generator:
        self.pwmgen = pwmgen
        self.pwmval = 0
        self.pwm_min = 0.1
        self.pwm_max = 0.5
        self.pwm_step = 0.01
        self.powerlimit = powerlimit
        self.powerlimit_reached = False
        
        ''' Inherited from Measure_VIP:
        self.i 
        self.v 
        self.p 
        self.values = v, i, p
        '''
      
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
        self.powerlimit_reached = False
        
        for pw in pwm_percent_range:
            
            self.set_pwm(pw/100)
            time.sleep(0.01)                    # allow some time for results to be stable
            v, i, power = self.get_VIP()
            
            if power > power_max:
                            
                vmax = v
                imax = i
                power_max = power
                pwmopt_percent = pw
            
            if power >= self.powerlimit:
                self.powerlimit_reached = True
                break
                
            
            if printflag:    
                print( '## PWM track', '\t', pw,'\t', '%2.2f' % v, '\t', '%2.2f' % i, '\t', '%3.0f' % power, '\t', '%3.0f' % power_max)
            
        self.pwmval = pwmopt_percent/100
        self.set_pwm(self.pwmval)
        time.sleep(0.01)
        
        if printflag:
            print("## PWM = %2.0i" % pwmopt_percent, "%") 
            print("## P = %2.0f" % power_max, "W")
            print("### Power limit reached:", self.powerlimit_reached)
            print()
            
        return power_max, pwmopt_percent, vmax, imax
    
    ## overwrite print_oled function from Measure_VIP
    ## to add print PWM value
    def print_oled(self, additional = ""):
        # Display values if oled is defined
        if self.oled:
            V, I, P = self.values
            self.oled.clear()
            
            s = '\tV = %2.2fV' % V
            s +=  '\tI = %2.2fA' % I
            s += "\tPWM: %1.2f" % self.pwmval
            s += '\tP = %2.0fW' % P
            s += '\t' + additional
            self.oled.print_s(s)
            
            
            