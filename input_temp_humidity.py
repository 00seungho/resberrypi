import Adafruit_DHT
import time
import RPi.GPIO as GPIO
sensor = Adafruit_DHT.DHT11
pin = 27
GPIO.setmode(GPIO.BCM)
SW1_PIN = 4

if __name__=="__main__":
    try:
        nowtemperature = None
        nowhumidity = None
        GPIO.setup(SW1_PIN,GPIO.IN)
        while True:
            humidity,temperature = Adafruit_DHT.read(sensor,pin)
            if temperature is not None or humidity is not None:
                  nowtemperature = temperature
                  nowhumidity = humidity
            if GPIO.input(4) == 0:
                if nowtemperature is None:
                    print("errer")
                else:
                    print(f"Temperatrue = {nowtemperature}°C")
                    print(f"Humidity = {nowhumidity}%")

                
                    
        
    finally:
        GPIO.cleanup()
