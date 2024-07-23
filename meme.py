from picographics import PicoGraphics, DISPLAY_TUFTY_2040
import jpegdec
import time

IMAGE_NAME = "tuftymeme.jpg"
display = PicoGraphics(display=DISPLAY_TUFTY_2040)

def show_photo():
    j = jpegdec.JPEG(display)

    # Open the JPEG file
    j.open_file(IMAGE_NAME)

    # Draws a box around the image
    #display.set_pen(DARKEST)
    #display.rectangle(PADDING, HEIGHT - ((BORDER_SIZE * 2) + PADDING) - 120, 120 + (BORDER_SIZE * 2), 120 + (BORDER_SIZE * 2))

    # Decode the JPEG
    j.decode(0,0,0)


while True:
        show_photo()
        display.update()
        time.sleep(10)