from machine import Pin
import time

vent = Pin(18, Pin.OUT)
v = 0

while True:
    vent.value(v)
    s = input("Ventilator on / off (1 / 0): ")
    v = int(s)
    
    
    
    