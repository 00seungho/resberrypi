import smbus
bus = smbus.SMBus(1)

i2c_address=0x48

command = 0x44

import time
try:
    while True:
        adc_data = bus.read_i2c_block_data(i2c_address,command,5)
        gasvalue = adc_data[3]

        gasvalue = gasvalue * 100/255
        gasvalue = round(gasvalue,2)
        print("Gas Senser : " +str(gasvalue)+"%")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass