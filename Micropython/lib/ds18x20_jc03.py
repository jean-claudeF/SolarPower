#ds18x20_jc03.py
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
    
        
    def get_as_string(self, tformat = '%2.1f'):
        # tab terminated!
        temps = self.get()
        
        s = ""
        for t in temps:
            s += tformat % t + '\t' 
            #s += str(t) + '\t' 
        return s
        
    
    def get_maxtemps_as_string(self):
        # tab terminated!
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

    while True:
        sensors.convert()
        time.sleep(0.75)
        #temps = sensors.get()
        sensors.get()
        sensors.print_temps('\t\t')
        
        s = sensors.get_as_string(tformat = '%2.0f')
        print(s)
        
        '''
        ga, a = sensors.checktemp(25)
        if ga:
            print(a)
        '''
        time.sleep(1)
    
    