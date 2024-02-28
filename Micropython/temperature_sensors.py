import onewire, ds18x20
import time

class TemperatureSensors():
    def __init__(self, ds_pin):
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
        self.addresses = self.ds_sensor.scan()
        self.nbsensors = len(self.addresses)
        self.maxtemps = [-100]*self.nbsensors
        
        # dummy measurement to avoid 85°C error
        self.convert()
        time.sleep(0.75)
        for i in range(0, self.nbsensors):
            a = self.addresses[i]
            t = self.ds_sensor.read_temp(a)
        
        
        
    def convert(self):
        if len(self.addresses):
            self.ds_sensor.convert_temp()
        
    def get(self):
        self.temps = []
        #for a in self.addresses:
        for i in range(0, self.nbsensors):
            a = self.addresses[i]
            t = self.ds_sensor.read_temp(a)
            self.temps.append(t)
            
            if t > self.maxtemps[i]:
                self.maxtemps[i] = t
        return self.temps
    
        
    def get_as_string(self):
        temps = self.get()
        s = ""
        for t in temps:
            s += '%2.1f' % t + '\t' 
            #s += str(t) + '\t' 
        return s
    
    def get_maxtemps_as_string(self):
        
        s = ""
        for t in self.maxtemps:
            s += '%2.1f' % t + '\t' 
            
        return s
    
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
    