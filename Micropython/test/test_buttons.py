from machine import Pin
from blink import blink
import time

btn1 = Pin(16, Pin.IN, Pin.PULL_UP)
btn2 = Pin(17, Pin.IN, Pin.PULL_UP)
btn3 = Pin(22, Pin.IN, Pin.PULL_UP)

led = Pin(18, Pin.OUT)

while True:
    if btn1.value() == 0:
        print("BTN1, GPIO 16")
    if btn2.value() == 0:
        print("BTN2, GPIO 17")
    if btn3.value() == 0:
        print("BTN3, GPIO 22")
        
    #print()
    time.sleep(0.3)
    blink(1)
        
        