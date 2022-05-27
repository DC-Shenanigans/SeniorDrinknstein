import board
import hd44780

class ScreenGo():
    def __init__(self):
        self.lcd = hd44780.HD44780() # https://github.com/bablokb/circuitpython-hd44780

    def write_to_screen(self,message):
        self.lcd.clear()
        count = 0
        print = ""

        for idx,letter in enumerate(message):
            print = print + letter
            if idx % 19 == 0:
                self.lcd.write(f"{message}", count)
                count += 1
                print = ""
                if count > 4:
                    print("message too long for screen")
                    break

        


