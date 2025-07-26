
import os
import time
import sys

# Test UART0 as sys.out and for REPL
# Best is testing without Thonny, as this interferes.
# To do this, create main.py with only this:
# import_test_uart_repl

helptext = """
Available commands:
Ctrl-C = interrupt program and provide REPL
Ctrl-D = Reset
*      = Interrupt program to enter a command and continue afterwards
         The command could be a function (like the dummy function "hi()"
         After executing the command, the program continues
         If empty, the program continues simply
"""

def hi():
    print(" HELLO ")


print(helptext)

from machine import UART, reset
uart0 = UART(0, baudrate=115200)
os.dupterm(uart0)
uart1 = UART(1, baudrate=9600)

# Check incoming commands
# Ctrl-C, Ctrl-D, * = CMD (in this case only <Enter> = continue program
def check_uart0():
    #  STOP or RESET via RxD0:
    if uart0.any():
        inp = uart0.read()
        # stop running program or reset:
        if b'\04' in inp:
            uart0.write("## RESET\n")
            time.sleep(0.1)
            reset()
            #soft_reset()
        elif b'\03' in inp:
            uart0.write("## STOP PROGRAM\n")
            #break
            sys.exit()
        elif b'*' in inp:
            s = input('CMD: ')
            print('#', s)
            try:
                exec(s)
            except:
                print("# CMD ERROR")

i=0
while 1:
    
    check_uart0()
        
    print("UART0: " + str(i))         # Writes to USB and UART0 (because of os.dupterm(uart0)
    uart1.write("UART1: " + str(i) + "\r\n")
    i+=1
    time.sleep(1)
    