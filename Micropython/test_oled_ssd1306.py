from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C as OLED


i2c = I2C(0, scl=Pin(9), sda=Pin(8))
#oled = SH1106_I2C(128, 64, i2c)
#oled = OLED(128, 64, i2c, rotate = 180)
oled = OLED(128, 64, i2c)
oled.init_display()

import time
time.sleep(0.5)
oled.fill(0)
oled.text('Hello', 0, 0)
oled.show()
