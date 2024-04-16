import smbus
import math
import RPi.GPIO as GPIO
import time
bus = smbus.SMBus(1)

i2c_address=0x48

command = 0x44


GPIO.setmode(GPIO.BCM)
trig = 23
echo = 24
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

import time
try:
    while True:
        adc_data = bus.read_i2c_block_data(i2c_address,command,5)
        psd_val = (adc_data[4]/255.0*3.3)*3/2
        psd_val = 29.988 * math.pow(psd_val,-1.173)
        psd_val = round(psd_val,2)
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
            print(f"Micro Distance: {distance} cm") 
        else:
            pass
        print("PSD Senser : " +str(psd_val)+"cm")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()


