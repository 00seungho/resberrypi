import smbus
import time

RED_LED = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED = 0b00000100

bus = smbus.SMBus(1)
#RED LED ON
state = 0b00000001
while True:
    
    if state == 0b00000000:
        state = 0b00000100
    bus.write_byte(0x20,state)
    state = state >>  1
    time.sleep(0.5)