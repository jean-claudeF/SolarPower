#ds18x20_jc04.py
# Easy reading of any number of DS18x20 temperature sensors
# Originally the sensors are ordered according to their addresses,
# but it is possible to change that order with e.g. sensors.re_sort_addr([2,1,3])
# where the array contains the indexes of the original order
# (the index array may be smaller than the number of sensors,
# thus allowing to use only part of the sensors)
#
# Overheating can be checked with e.g. ga, a = sensors.checktemp(maxtemp)
#
# Writing to CSV files is easy using s = sensors.get_as_string()

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
            
    def re_sort_addr(self, indexes):
        # Reorder sensors: indexes e.g. [3, 1, 2, 0]
        print("# Reordering ", indexes)
        newaddresses = []
        for i in range(0, len(indexes)):
            n = indexes[i]
            a = self.addresses[n]
            newaddresses.append(a)
        self.addresses = newaddresses
        self.nbsensors = len(self.addresses)
        
    def sort_addr(self):
        # sort according to address scan
        self.addresses = self.ds_sensor.scan()
    
    def convert(self):
        if len(self.addresses):
            self.ds_sensor.convert_temp()
        
    def get(self, nbtries = 3):
        # get all temperatures as array and update maxtemps
        # to avoid problems with  read errors that stop a program,
        # reading is done with try - except and on error, -300 is returned
        self.temps = []
        
        for i in range(0, self.nbsensors):
            a = self.addresses[i]
            
            for j in range(nbtries):
                try:
                    t = self.ds_sensor.read_temp(a)
                    break
                except:
                    t = -300
                
            self.temps.append(t)
            
            if t > self.maxtemps[i]:
                self.maxtemps[i] = t
        return self.temps
    
        
    def get_as_string(self, tformat = '%2.1f', separator = '\t'):
        # get all temperatures as tab separated string
        # separator can also be something else e.g. '\n'
        temps = self.get()
        s = ""
        for t in temps:
            s += tformat % t + separator 
        return s
    
    def get_maxtemps_as_string(self, tformat = '%2.1f', separator = '\t'):
        # get maximum temperatures as tab separated string
        s = ""
        for t in self.maxtemps:
            s += tformat % t + separator
        return s
    
    def print_temps(self, separator):
        for temp in self.temps:
            print(temp, end = separator)
        print()
        
    def checktemp(self, alarmtemp):
        # returns tuple of globalaalarm (True/False) and
        # array of 0/1 for allsensors
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
    
    def print_info(self):
        print("# Temperature sensor addresses: (Family, SerialNb, CRC)")
        for address in self.addresses:
            family_code = address[0]
            serial_number = bytearray_to_hexstring(address[1:7])
            crc = address[7]
            print("#", hex(family_code),  "  " , serial_number, "  ", crc  )
        print()          
        
#------------------------------------------------------------------
def bytearray_to_hexstring(bytes):
    ''' Format bytearray to reader friendly string'''
    h = ''
    for i in bytes:
        
        s = hex(i)[2:]
        ##print(i, s)
        if len(s) == 1:
            s='0' + s
        s = s.upper()
        h += s

    return h    
#----------------------------------------------------


if __name__ == "__main__":
    
    ds_pin = machine.Pin(15)
 
    sensors = TemperatureSensors(ds_pin)
    sensors.print_info()
    
    
    indexes = [0,2,3, 1]
    #indexes = [3,1]
    sensors.re_sort_addr(indexes)
    sensors.print_info()
        
    while True:
        sensors.convert()
        time.sleep(0.75)
        
        s = sensors.get_as_string()
        print(s, end = '\t\t')
        sm = sensors.get_maxtemps_as_string()
        print(sm)  
      
        ga, a = sensors.checktemp(27)
        if ga:
            print(a)
        
        time.sleep(1)
    
    