import smbus
import math
class read_i2c():
    bus = None
    i2c_address=0x48
    command = 0x44
    def __init__(self) -> None:
        self.bus = smbus.SMBus(1)

    def vr_read(self) -> float:
        adc_data = self.bus.read_i2c_block_data(self.i2c_address,self.command,5)
        vrValue  = adc_data[1]
        vrValue = vrValue * 100/255
        vrValue = round(vrValue,2)
        return vrValue
    
    def cds_read(self) -> float:
        adc_data = self.bus.read_i2c_block_data(self.i2c_address,self.command,5)
        cdsValue = adc_data[2]
        cdsValue = cdsValue * 100/255
        cdsValue = round(cdsValue,2)

    def gas_read(self) -> float:
        adc_data = self.bus.read_i2c_block_data(self.i2c_address,self.command,5)
        gasValue = adc_data[3]
        return gasValue
    
    def psd_read(self) -> float:
        adc_data = self.bus.read_i2c_block_data(self.i2c_address,self.command,5)
        psd_val = (adc_data[4]/255.0*3.3)*3/2
        psd_val = 29.988 * math.pow(psd_val,-1.173)
        psd_val = round(psd_val,2)
        return psd_val

class write_i2c():
    state = 0b00000000
    bus = None
    def __init__(self) -> None:
        self.bus = smbus.SMBus(1)
    def On(self, cmd):
        self.state = (self.state | cmd)
        print(self.state)
        self.bus.write_byte(0x20, self.state)
    def off(self, cmd):
        self.state = (self.state & (~cmd))
        print(self.state)
        self.bus.write_byte(0x20, self.state)