from machine import UART, Pin
import time
from blink import blink

#uart0 = UART(0, baudrate=115200, timeout = 10, timeout_char = 10)
uart = UART(0, baudrate=115200, timeout = 10, timeout_char = 10)

led2 = Pin(15, Pin.OUT)

class ReadSerialLines():
    def __init__(self, uart):
        self.uart = uart
        self.buffer = b""
        self.buffer_ready = False
        self.c = b''

    
    def read(self):
        s = serReader.read_raw()
        if s:
            try:
                s = s.decode('utf-8')
            except:
                s = ""    
        return s
    
    
    def read_raw(self):
        if self.uart.any():
            
            self.c = self.uart.read(1)
            if self.c == b'\n':
                self.buffer_ready = True
            else:
                self.buffer += self.c
                
        if self.buffer_ready:
            s = self.buffer
            #s = self.buffer.decode('utf-8')
            self.buffer = b""
            self.buffer_ready = False
            
            return s
        else:
            return ""

#----------------------------------------------------------
infos = []

serReader = ReadSerialLines(uart)


while True:   
    ##s0 = serReader0.read()
    
    s = serReader.read()
  
    
    
        
    if s:
        #print(s)
        blink(1, dt = 0.02)

        s = s.replace('\r', '')
        
        # Get parameter info:   
        if s[0:3] == "# i":
            infos = s.split('\t')
            print("Info: ", infos)
        elif s[0:2] == "##":
            pass
      
        
        else:
            values = s.split('\t')
            print("Values: ", values)
            
    
    
        
            
