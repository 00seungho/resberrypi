import smbus
bus = smbus.SMBus(1)

i2c_address=0x48

command = 0x44

import time
try:
    while True:
        adc_data = bus.read_i2c_block_data(i2c_address,command,5)
        vrValue = adc_data[1]

        vrValue = vrValue * 100/255
        vrValue = round(vrValue,2)
        print("가변저항 : " +str(vrValue)+"%")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass