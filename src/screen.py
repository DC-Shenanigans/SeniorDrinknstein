import board
import hd44780


class ScreenGo():
    def __init__(self):
        self.has_screen = False
        try:
            self.lcd = hd44780.HD44780()  # https://github.com/bablokb/circuitpython-hd44780
            self.has_screen = True
        except:
            print("Unable to initialize screen")

    def write_to_screen(self, message):
        if self.has_screen:
            self.lcd.clear()

            line_index = [1, 3, 2, 4]
            count = 0

            print_output = ""
            for idx, letter in enumerate(message):
                if count > 3:
                    print("message too long for screen")
                    break
                print_output = print_output + letter

                if len(print_output) == 20 or idx == len(message) - 1:
                    self.lcd.write(f"{print_output}", line_index[count])

                    print_output = ""
                    count += 1
