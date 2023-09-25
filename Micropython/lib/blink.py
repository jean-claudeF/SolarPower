from machine import Pin
import time

led = Pin(25, Pin.OUT)

def blink(n, dt = 0.15):
    led.value(0)
    for i in range(0, 2*n ):
        led.toggle()
        time.sleep(dt)
    led.value(0)
    
if __name__ == "__main__":
    blink(3)