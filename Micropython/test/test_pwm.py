from machine import Pin
import time
from pwmc import PWMc


PWMpin = 3
PWMfreq = 16E3
pwmgen = PWMc(PWMpin, freq= PWMfreq)
vp = 0.2

while True:
    pwmgen.set_pwm(vp)
    v = input("PWM value (0...1):  ")
    vp = float(v)
    
    
    