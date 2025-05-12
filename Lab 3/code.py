import time
import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import adafruit_vl53l0x

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Initialize OLED display
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Initialize LIDAR sensor
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

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

    # Clear the display before drawing new text
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Define text position
    (x, y) = (0, 0)

    # Draw the text
    draw.text((x, y), data, font=font, fill=255)

    # Display the image
    oled.image(image)
    oled.show()

try:
    while True:
        distance = vl53.range
        disp("M24EEV020_Dist: {} mm".format(distance))
        time.sleep(1)  # Update every second
except KeyboardInterrupt:
    print("Exit")  # Exit on CTRL+C
