import math
import time
from gpiozero import Button

radius_cm = 9.0
wind_interval = 5
wind_count = 0

def spin():
    global wind_count
    wind_count = wind_count + 1
    #print("spin" + str(wind_count))

def calculate_speed(time_sec):
    global wind_count
    circumference_cm = (2 * math.pi) * radius_cm
    rotations = wind_count / 2.0
    dist_cm = circumference_cm * rotations
    speed = dist_cm / wind_interval

    return speed

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin

while True:
    wind_count = 0
    time.sleep(wind_interval)
    print(calculate_speed(wind_interval))
    

