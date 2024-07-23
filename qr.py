from picographics import PicoGraphics, DISPLAY_TUFTY_2040
from pimoroni import Button
import jpegdec
import time
import qrcode

display = PicoGraphics(display=DISPLAY_TUFTY_2040)
button_c = Button(9, invert=False)
WIDTH, HEIGHT = display.get_bounds()

links = [["github","https://github.com/FashionFrame"],["linkedin","https://www.linkedin.com/in/lacey-howarth-0b258b256/"]]

LIGHTEST = display.create_pen(233, 239, 236)
LIGHT = display.create_pen(160, 160, 139)
DARK = display.create_pen(85, 85, 104)
DARKEST = display.create_pen(33, 30, 32)

def measure_qr_code(size, code):
    w, h = code.get_size()
    module_size = int(size / w)
    return module_size * w, module_size

def draw_qr_code(ox, oy, size, code):
    size, module_size = measure_qr_code(size, code)
    display.set_pen(LIGHTEST)
    display.rectangle(ox, oy, size, size)
    display.set_pen(DARKEST)
    for x in range(size):
        for y in range(size):
            if code.get_module(x, y):
                display.rectangle(ox + x * module_size, oy + y * module_size, module_size, module_size)


def show_qr(link):
    display.set_pen(DARK)
    display.clear()

    code = qrcode.QRCode()
    code.set_text(link[1])

    size, module_size = measure_qr_code(HEIGHT, code)
    left = int((WIDTH // 2) - (size // 2))
    top = int((HEIGHT // 2) - (size // 2))
    draw_qr_code(left, top, HEIGHT, code)
    display.set_pen(LIGHTEST)
    display.text(link[0], 240, 215, 160, 2)


badge_mode = "photo"
show_qr(links[0])
display.update()
index = 0

while True:
    for x in links:
        show_qr(x)
        display.update()
        while True:
            time.sleep(1)
            if button_c.is_pressed: break
        
