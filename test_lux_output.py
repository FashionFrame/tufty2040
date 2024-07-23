from machine import ADC, Pin
from time import sleep
from picographics import PicoGraphics, DISPLAY_TUFTY_2040

display = PicoGraphics(display=DISPLAY_TUFTY_2040)
WHITE = display.create_pen(255, 255, 255)

lux_pwr = Pin(27, Pin.OUT)
lux_pwr.value(1)

lux = ADC(26)

while True:
    reading = lux.read_u16()
    display.set_pen(WHITE)
    display.text(str(reading), 40, 60, 360, 15)
    display.update()
    sleep(1)
    display.set_pen(display.create_pen(0, 0, 0))
    display.clear()
    