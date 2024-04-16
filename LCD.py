import I2C_LCD_driver

textLcd = I2C_LCD_driver.lcd()
textLcd.backlight(0                    )
textLcd.lcd_display_string("abc",line= 1, pos=3)
textLcd.lcd_display_string("123456",line=2,pos=4)