
import machine, onewire, ds18x20
import time

ds_pin = machine.Pin(15)


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
        alarms = []
        globalalarm = False
        temps = self.get()
        
        for t in temps:
                       
            if t > alarmtemp:
                alarms.append(1)
                globalalarm = True
            else:
                alarms.append(0)
        return globalalarm, alarms
    
                
#------------------------------------------------------------------ 
 
sensors = TemperatureSensors(ds_pin)
print(sensors.addresses)

while True:
    sensors.convert()
    time.sleep(0.75)
    #temps = sensors.get()
    sensors.get()
    sensors.print_temps('\t\t')
    
    
    '''
    ga, a = sensors.checktemp(25)
    if ga:
        print(a)
    '''
    time.sleep(1)
    
