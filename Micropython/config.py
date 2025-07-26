# User defined parameters (editable)
identity = "A"

use_oled = True
print_interval = 2
print_header_every = 10
track_interval = 30                       # track every xx seconds
dt = 3                                # display every dt

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

baud = 115200           # for UART0

helpfile = "solartrack.hlp"