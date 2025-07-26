from machine import Pin
from blink import blink
import time

jp1 = Pin(14, Pin.IN, Pin.PULL_UP)
jp2 = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    if jp1.value() == 0:
        print("JP1 set ")
    if jp2.value() == 0:
        print("JP2 set")
            
    #print()
    time.sleep(0.3)
    blink(1)
        
        