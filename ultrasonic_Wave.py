import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trig = 23
echo = 24
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

try:
    while True:
        GPIO.output(trig,True)
        time.sleep(0.5)
        GPIO.output(trig,False)
        time.sleep(0.00001)
        while GPIO.input(echo) == 0:
            signal_Start = time.time()
        while GPIO.input(echo) == 1:
            signal_End = time.time()
        responseDuration = signal_End - signal_Start
        distance = responseDuration * 34000/2

        distance = round(distance,2)
        if distance < 1000:
            print(f"Distance: {distance} cm")
        else:
            pass
finally:
    GPIO.cleanup()