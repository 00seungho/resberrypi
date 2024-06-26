import RPi.GPIO as GPIO
import time
from collections import deque
STEP_IN1 = 16
STEP_IN2 = 20
STEP_IN3 = 21
STEP_IN4 = 26
sig = deque([1,0,0,0])
step = 2048
dir = 1
if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(STEP_IN1, GPIO.OUT)
    GPIO.setup(STEP_IN2, GPIO.OUT)
    GPIO.setup(STEP_IN3, GPIO.OUT)
    GPIO.setup(STEP_IN4, GPIO.OUT)
 
    try:
        while(True):
            for cnt in range(0,step):
                GPIO.output(STEP_IN1,sig[0])
                GPIO.output(STEP_IN2,sig[1])
                GPIO.output(STEP_IN3,sig[2])
                GPIO.output(STEP_IN4,sig[3])
                time.sleep(0.005)
                sig.rotate(dir)
            dir = dir*-1
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  