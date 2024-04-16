import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
buzzer = 12
# 4옥타브 도레미~ 5옥타브 도
SCALE = [261, 294, 330, 349, 392, 440, 493, 523]
dic = {"도":261,"레":294,"미":330,"파":349,"솔":392,"라":440,"시":493}
do = ['미', '레', '도', '레', '미', '미', '미', '레', '레', '레', '미', '솔', '솔', '미', '레', '도', '레', '미', '미', '미', '레', '레', '미', '레', '도']

GPIO.setup(buzzer, GPIO.OUT)
pwm = GPIO.PWM(buzzer, 100) # 100Hz
try:
    # pwm 시작
    pwm.start(100)
    # dutycycle 50%
    pwm.ChangeDutyCycle(50)
 
    for i in do:
      connet = dic[i]
      pwm.ChangeFrequency(connet) #주파수 변경  
      time.sleep(0.5)
    # Buzzer를 끈다
    pwm.ChangeDutyCycle(100)
    print("OFF")
 
# 종료 등의 키보드 인터럽트 발생시 처리 동작
except KeyboardInterrupt:
        # Buzzer를 끈다
        GPIO.output(buzzer,GPIO.LOW)
        # GPIO를 초기화한다
        GPIO.cleanup()