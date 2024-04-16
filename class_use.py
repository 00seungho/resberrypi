from i2c_class import read_i2c
from i2c_class import write_i2c
import I2C_LCD_driver
import time

RED_LED = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED = 0b00000100
RELAY_1 = 0b00010000
RELAY_2 = 0b00100000

textLcd = I2C_LCD_driver.lcd()
textLcd.lcd_display_string("KOPO AISW",1)
textLcd.lcd_display_string("I2C_BUS TEST",2)

adc = read_i2c()
write = write_i2c()

print(f"VR: {adc.vr_read()} %")
print(f"CdS: {adc.cds_read()} %")
print(f"GAS: {adc.gas_read()} GAS")
print(f"Distance: {adc.psd_read()} cm")
textLcd.lcd_display_string(f"{adc.vr_read()}%{adc.cds_read()}%",2)
write.On(RED_LED)
time.sleep(0.5)
write.On(GREEN_LED)
time.sleep(0.5)
write.On(BLUE_LED)
time.sleep(0.5)
write.off(RED_LED|GREEN_LED|BLUE_LED)
time.sleep(0.5)
write.On(RELAY_1|RELAY_2)
time.sleep(0.5)
write.off(RELAY_1|RELAY_2)
time.sleep(0.5)

