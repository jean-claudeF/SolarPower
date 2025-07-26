from machine import Pin
import onewire, ds18x20
import time

ds_pin = Pin(15)
ventilator = Pin(18, Pin.OUT)

class TemperatureSensors():
    def __init__(self, ds_pin):
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
        self.addresses = self.ds_sensor.scan()

    def convert(self):
        if len(self.addresses):
            self.ds_sensor.convert_temp()
        
    def get(self):
        self.temps = []
        for a in self.addresses:
            t = self.ds_sensor.read_temp(a)
            self.temps.append(t)
        return self.temps

    def print_temps(self, separator):
        for temp in self.temps:
            print(temp, end = separator)
        print()
        
    def checktemp(self, alarmtemp):
        """ returns
            globalalarm = 1/0
            alarms = [al0, al1 ...] indicates which sensor has given the alarm
        """
        alarms = []
        globalalarm = 0
        temps = self.get()
        
        n = 1
        for t in temps:
                       
            if t > alarmtemp:
                alarms.append(1)
                globalalarm = 1
            else:
                alarms.append(0)
            n += 1        
        return globalalarm, alarms
    
                
#------------------------------------------------------------------ 
trigger_temp = 40 
sensors = TemperatureSensors(ds_pin)
print(sensors.addresses)

i = 0
while True:
    sensors.convert()
    time.sleep(0.75)
    temps = sensors.get()
    ga, a = sensors.checktemp(trigger_temp)
    if ga:
        ventilator.on()
    else:
        ventilator.off()
    
    for temp in temps:
        print(i, '\t', temp, end = '\t')
    print(ga)    
  
    i += 1
    
   
    
    
