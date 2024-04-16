import smbus
import I2C_LCD_driver
import smbus
import time

RED_LED = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED = 0b00000100

def ledInit():
    global state
    global bus
    state = 0b00000000
    bus = smbus.SMBus(1)
 
def ledOn(cmd):
    global state
    state = (state | cmd)
    bus.write_byte(0x20, state)
   
def ledOff(cmd):
    global state
    state = (state & (~cmd))
    bus.write_byte(0x20, state)


bus = smbus.SMBus(1)
textLcd = I2C_LCD_driver.lcd()

i2c_address=0x48

command = 0x44
ledInit()
import time
try:
    while True:
        adc_data = bus.read_i2c_block_data(i2c_address,command,5)
        CdsValue = adc_data[2]

        CdsValue = CdsValue * 100/255
        CdsValue = round(CdsValue,2)
        msg = f"CDS:{CdsValue}%"
        textLcd.lcd_display_string(msg,line= 1)
        print(msg)
        if CdsValue <30:
            ledOn(RED_LED)
        else:
            ledOff(RED_LED)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass