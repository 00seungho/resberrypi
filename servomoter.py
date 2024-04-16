import RPi.GPIO as GPIO
import time
 
#GPIO의 모드를 BCM으로 설정한다(GPIO번호 사용)
GPIO.setmode(GPIO.BCM)
 
#서보모터와 연결된 GPIO 번호를 변수에 저장한다.
SERVO_PIN = 25
 
if __name__ == "__main__":
 
    # 서보모터 핀을 OUTPUT 으로 설정한다.
    GPIO.setup(SERVO_PIN, GPIO.OUT)
 
    # 서보모터를 제어할 pwm 모듈을 저장한다.
    servo_pwm = GPIO.PWM(SERVO_PIN, 50)
 
    # 서보모터 핀의 출력을 초기화한다.
    servo_pwm.start(0)
 
    # 서보모터를 반복하여 0 -> 180 -> 90 순서로 동작시킨다.
    try:
 
        while(True):
            # 서보모터의 각도를 0도로 제어한다.
            servo_pwm.ChangeDutyCycle(7.5)
            time.sleep(1)
 
            # 서보모터의 각도를 -90도로 제어한다.
            servo_pwm.ChangeDutyCycle(2.5)
            time.sleep(1)
 
            # 서보모터의 각도를 0도로 제어한다.
            servo_pwm.ChangeDutyCycle(7.5)
            time.sleep(1)
 
            # 서보모터의 각도를 90도로 제어한다.
            servo_pwm.ChangeDutyCycle(12.5)
            time.sleep(1)
 
    # 키보드 인터럽트, 에러 등으로 소스가 종료될 경우 GPIO를 초기화한 후 종료한다.
    finally:
        GPIO.cleanup()