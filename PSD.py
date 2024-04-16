import smbus
import math
import time
bus = smbus.SMBus(1)

i2c_address=0x48

command = 0x44



import time
try:
    while True:
        adc_data = bus.read_i2c_block_data(i2c_address,command,5)
        psd_val = (adc_data[4]/255.0*3.3)*3/2
        psd_val = 29.988 * math.pow(psd_val,-1.173)
        psd_val = round(psd_val,2)
        print("PSD Senser : " +str(psd_val)+"cm")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
