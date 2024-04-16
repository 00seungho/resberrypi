import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 27

if __name__=="__main__":
    while True:
        sensorValue = Adafruit_DHT.read(sensor,pin)
        humidity = sensorValue[0]
        if humidity is not None:
            print(f"Humidity = {humidity}%")
        else:
            print("Failed to get reading. Try agin!")
        time.sleep(1.0)
