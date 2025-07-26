from ds18x20_jc03 import TemperatureSensors
import machine 
import time


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
        
        
        ga, a = sensors.checktemp(30)
        if ga:
            print(a)
        
        time.sleep(1)
    

