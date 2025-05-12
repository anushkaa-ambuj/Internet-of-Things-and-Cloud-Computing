from influxdb import InfluxDBClient
from lidar import fetch_data

# Connect to InfluxDB
client = InfluxDBClient(host='localhost', port=8086)
# Choosing the DB
client.switch_database('ROOM6')

# Running infinite loop to insert data from LIDAR continuously.
# Stop the INSERT by KeyboardInterrupt(Ctrl+C)
while True:
    try:
        data = fetch_data()
        json_body = [
            {
                "measurement": "B21ES006",
                "fields": {
                    "value"   : data
                }
            }
        ]
        print(client.write_points(json_body))  ## prints TRUE if insert is successful.
    except KeyboardInterrupt:
        print("exit")

    
    
