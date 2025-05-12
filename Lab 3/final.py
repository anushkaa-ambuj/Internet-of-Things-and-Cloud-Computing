import time
import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import adafruit_vl53l0x

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Clear display.
oled.fill(0)
oled.show()

def disp1(ROLLNO,DATA):
    # Create blank image for drawing.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Load default font.
    font = ImageFont.load_default()

    # Define text position
    (x, y) = (0, 0)

    # Draw the text
    draw.text((x, y), ROLLNO, font=font, fill=255)
    draw.text((x, y+10), DATA, font=font, fill=255)

    # Display the image
    oled.image(image)
    oled.show()

def disp(DATA):
    # Create blank image for drawing.
    image = Image.new("1", (oled.width, oled.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Load default font.
    font = ImageFont.load_default()

    # Define text position
    (x, y) = (0, 0)

    # Draw the text
    draw.text((x, y+10), DATA, font=font, fill=255)

    # Display the image
    oled.image(image)
    oled.show()


rollno = "B21ES006"
try:
    # Main loop will read the range and print it every second.
    while True:
        disp1(rollno,":- {0}mm".format(vl53.range))
        time.sleep(0.2)
except KeyboardInterrupt:
    print("Exit")  # Exit on CTRL+C