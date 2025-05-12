import time

import board
import busio

import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Clear display.
oled.fill(0)
oled.show()
def disp(data):

    # Create blank image for drawing.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Load default font.
    font = ImageFont.load_default()

    # Define text position
    (x, y) = (0, 0)

    # Draw the text
    draw.text((x, y), data, font=font, fill=255)

    # Display the image
    oled.image(image)
    oled.show()


try:
    while True:
        data = input("Enter text to display :- ")
        disp(data)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("Exit")  # Exit on CTRL+C
