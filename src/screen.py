import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

class ScreenGo():
    def __init__(self):

        self.i2c = busio.I2C(board.SCL, board.SDA)
        cols = 16
        rows = 2
        self.lcd = character_lcd.Character_LCD_I2C(self.i2c, cols, rows)
        self.turn_on_backlight()

    def write_to_screen(self,message):
        self.lcd.message = "%s" % message

    def turn_on_backlight(self):
        self.lcd.backlight = True
