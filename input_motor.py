import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SW1_PIN = 4
SW2_PIN = 17
SW3_PIN = 18
MOTOR_P = 19
MOTOR_M = 13
SW_PIN_LIST = [SW1_PIN,SW2_PIN,SW3_PIN]
if __name__ == "__main__":
    GPIO.setup(SW_PIN_LIST,GPIO.IN)
    GPIO.setup(MOTOR_P, GPIO.OUT)
    GPIO.setup(MOTOR_M, GPIO.OUT)
    try:
        GPIO.output(MOTOR_P,GPIO.LOW)
        GPIO.output(MOTOR_M,GPIO.LOW)
        while(True):
            if GPIO.input(SW_PIN_LIST[0]) == 0:
                GPIO.output(MOTOR_P,GPIO.LOW)
                GPIO.output(MOTOR_M,GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(MOTOR_P,GPIO.HIGH)
                GPIO.output(MOTOR_M,GPIO.LOW)
                print("정회전")  
            elif GPIO.input(SW_PIN_LIST[1]) == 0:
                GPIO.output(MOTOR_P,GPIO.LOW)
                GPIO.output(MOTOR_M,GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(MOTOR_P,GPIO.LOW)
                GPIO.output(MOTOR_M,GPIO.HIGH)
                print("역회전") 
            elif GPIO.input(SW_PIN_LIST[2]) == 0:
                GPIO.output(MOTOR_P,GPIO.LOW)
                GPIO.output(MOTOR_M,GPIO.LOW)
                print("멈춤")
            
    finally:
        GPIO.cleanup()