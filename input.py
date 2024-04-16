import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SW1_PIN = 4
SW2_PIN = 17
SW3_PIN = 18
SW4_PIN = 22

SW_PIN_LIST = [SW1_PIN,SW2_PIN,SW3_PIN,SW4_PIN]

if __name__ == "__main__":
    GPIO.setup(SW_PIN_LIST,GPIO.IN)
    try:
        while(True):
            button_state =[]
            for i in SW_PIN_LIST:
                button_state.append(GPIO.input(i))
            print("Button State: ",button_state)
            time.sleep(0.5)
    finally:
        GPIO.cleanup()