from machine import I2C, Pin
from ssd1306_plus import SSD1306_PLUS
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
## i2c = I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_PLUS(128, 64, i2c)
oled.fill(0)


star = '''
.#.
#.#
.#.
'''

oled.draw_sprite(star, 0, 0, '#', '.')
# Sprite string, (x, y) of top left corner, white-colour character, black-colour character
# Any non-newline character in the sprite that is not either of the colour characters will be ignored (i.e. 'transparent').
