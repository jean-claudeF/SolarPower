from machine import Pin, ADC
import time
a = Pin(26, Pin.IN)				  # this is needed to turn input to high impedance   
adc0 = ADC(0)		# Pin 31

offset0 = -0.006
k0 = 0.98522




def readADC0(nb):
    v = 0
    for i in range(0,nb):
        v += adc0.read_u16()
    v = v/nb * 3.3 / (65535)
    v += offset0
    v *= k0
    return v
    
def print_format(vvect):
    # print elements of vvect (list of voltages) in tabular form
    
    for v in vvect:
        vs = "%1.3f" % v
        print(vs, end = "\t")
    print()

## Analyze results for min, max + variation:

v1list = []
v5list = []
v11list = []
        

for i in range(0,100):
    #v = adc.read_u16() * 3.3 / (65535)
    v1 = readADC0( 1)
    v5 = readADC0( 5)
    v11 = readADC0(11)
    ##vr = r.filter(v0)
    #print_format([v, v0, vr])
    print_format([v1, v5, v11])
    
    v1list.append(v1)
    v5list.append(v5)
    v11list.append(v11)
       

    time.sleep(0.01)

v1min = min(v1list)
v5min = min(v5list)
v11min = min(v11list)

v1max = max(v1list)
v5max = max(v5list)
v11max = max(v11list)

delta1 = v1max - v1min
delta5 = v5max - v5min
delta11 = v11max - v11min



print()
print("Min: ")
print_format( [v1min, v5min, v11min])
print("Max:")
print_format( [v1max, v5max, v11max])
print("Variation:")
print_format([delta1, delta5, delta11])
