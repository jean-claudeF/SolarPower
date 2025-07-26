# User defined parameters (editable)
# This is for unit B

def print_config():
    with open("config_B.py", 'r') as f:
        s = f.read()
        print(s)
print_config()


# new for unit B: (7.2025)
identity = "B"
ds1820_order = [0,2,3,1]
jmpr_watchdog_pin = 14
ds1820_pin = 15
btn1_pin = 16
btn2_pin = 17
PWM_pin = 3
vent_pin = 18
on_demand_pin = 13          # jumper open:print auto (every print_interval) or closed: on demand 
#-----------------------

use_oled = True
print_interval = 2
print_header_every = 10
track_interval = 30                       # track every xx seconds
###dt = 3                                # display every dt

# PWM:
pwm_min = 0.1
pwm_max = 0.6
pwm_step = 0.01
PWMfreq = 18E3

# Limit power
powerlimit = 1000        # Don't exceed this power, exit track loop when exceeded
U1 = 48                  # Over U1, reduce power limit
U2 = 52                  # At U2 powerlimited to 0


vent_on_temp = 40       # switch on ventilator at this temperature

baud0 = 115200           # for UART0, terminal
baud1 = 9600             # for UART1, communication with Home Assistant

helpfile = "solartrack.hlp"



