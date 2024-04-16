import smbus
import time

RELAY_1 = 0b00010000
RELAY_2 = 0b00100000

bus = smbus.SMBus(1)

print("릴레이 1 ON / " + bin(RELAY_1))
bus.write_byte(0x20, RELAY_1)
time.sleep(1)

print("릴레이 2 ON / " + bin(RELAY_2))
bus.write_byte(0x20, RELAY_2)

#0011 0000
#1110 0000
#0010 0000

# 0010 0000
# 1101 1111
# 0000 0000


#현재상태 저장 off를 하기 위해 상태 저장
state = RELAY_2 | RELAY_1
time.sleep(1)
print(f"{bin(state)}")
state = state & (~RELAY_1)
print("릴레이 1 OFF" + bin(state))
bus.write_byte(0x20, state)
time.sleep(1)
# state = 00100000
# state = 00010000 ~ 11101111

state = state & (~RELAY_2)
print("릴레이 2 OFF" + bin(state))
bus.write_byte(0x20, state)



