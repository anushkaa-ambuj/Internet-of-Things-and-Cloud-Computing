import time
import board
import busio
import adafruit_vl53l0x

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# try:
#     Main loop will read the range and print it every second.
#     while True:
#         print("Range: {0}mm".format(vl53.range))
#         time.sleep(0.2)
# except KeyboardInterrupt:
#     print("Exit")  # Exit on CTRL+C

def fetch_data():
    try:
        return vl53.range  ## Function returns the LIDAR data
    except:
        return -1000       ## Error Handling
        
        

    
    
