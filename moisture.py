#this function is to collect sensor readings from the Pimoroni Grow Hat Moisture Sensor
#this function then passes the value back to the main function for the bot to message in chat

from grow.moisture import Moisture
import math
from time import sleep

def grab_moisture():
    m1 = 0
    capture = 0

    m1_sensor = Moisture(1)

    while m1 == 0:
        m1 = m1_sensor.moisture

    for i in range(10):
        moistures = []
        capture = m1_sensor.moisture
        moistures.append(capture)
        print(moistures)
        sleep(.5)
    
    avg_moisture = sum(moistures) / len(moistures)
    print(avg_moisture)
    return(avg_moisture)

if __name__ == "__main__":
    grab_moisture()