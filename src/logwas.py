# log was fuck
# Does logging and stats
from itertools import count
import json

# I want to make this fuck so badddd
# fuck it. I'll revert later if u want
class fuck:

    drink_count_name = "drink_count"
    pump_time_name = "pump_time"
    stat_file = None
    stat_obj = None

    def __init__(self, stat_file):
        try:
            self.stat_file = open(stat_file, "r+")
        except:
            # Probably new file open new for creation
            try:
                self.stat_file = open(stat_file, "w+")
            except:
                #fatal error
                print("Cannot open", stat_file)
        
        try:
            self.stat_obj = json.load(self.stat_file)
        except:
            # Probably empty file. Will need to make new one
            self.stat_obj = {
                self.drink_count_name: {},
                self.pump_time_name: {}
            }

            self.__update_statfile()

    def stat_drink(self, drink_name):
        if not drink_name in self.stat_obj[self.drink_count_name]:
            self.stat_obj[self.drink_count_name][drink_name] = 1
        else:
            self.stat_obj[self.drink_count_name][drink_name] += 1

        self.__update_statfile()

    def stat_pump(self, pump_pin, time_sec):
        if not pump_pin in self.stat_obj[self.pump_time_name]:
            self.stat_obj[self.pump_time_name][pump_pin] = time_sec
        else:
            self.stat_obj[self.pump_time_name][pump_pin] = round(self.stat_obj[self.pump_time_name][pump_pin] + time_sec, 1)

        self.__update_statfile()

    def __update_statfile(self):
        self.stat_file.seek(0)
        json.dump(self.stat_obj, self.stat_file)
        self.stat_file.truncate()
        