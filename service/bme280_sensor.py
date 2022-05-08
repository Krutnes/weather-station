import bme280
import smbus2
from time import sleep

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

def read_air():
    bme280_data = bme280.sample(bus,address)
    humidity = bme280_data.humidity
    pressure = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    return humidity, pressure, ambient_temperature

while True:
    airReading = read_air()
    humidity,pressure,temperature = airReading
    print("Temperatur: ", temperature)
    print("Lufttrykk: ", pressure)
    print("Luftfuktighet: ", humidity)
    print("=========")
    sleep(5)