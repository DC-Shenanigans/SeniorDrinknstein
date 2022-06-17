import time
import board
import hd44780


class ScreenGo():
    def __init__(self):
        self.has_screen = False
        self.to_write = [[], [], [], []]
        self.current_screen = [[], [], [], []]
        try:
            self.lcd = hd44780.HD44780()  # https://github.com/bablokb/circuitpython-hd44780
            self.has_screen = True
        except:
            print("Unable to initialize screen")

    def write_to_screen(self, message, immediate = False, letter_sleep = 0.01):
        if self.has_screen:
            self.lcd.clear()

            self.to_write = [[], [], [], []]

            count = 0

            line = []
            for idx, letter in enumerate(list(message)):
                if count > 3:
                    print("message too long for screen")
                    break
                line.append(letter)

                if len(line) == 20 or idx == len(message) - 1:
                    self.to_write[count] = line

                    line = []
                    count += 1
            
            line_indexes = [1, 2, 3, 4]
            for line_index, line in enumerate(self.to_write):
                if immediate:
                    self.lcd.write(line, line_indexes[line_index])
                else:
                    self.current_screen[line_index] = []
                    for letter_index, letter in enumerate(line):
                        if len(self.current_screen[line_index]) > letter_index:
                            self.current_screen[line_index][letter_index] = letter
                        else:
                            self.current_screen[line_index].append(letter)
                        if letter != ' ':
                            self.lcd.write("".join(self.current_screen[line_index]), line_indexes[line_index])
                            time.sleep(letter_sleep)
