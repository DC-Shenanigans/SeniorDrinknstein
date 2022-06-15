# log was fuck
# Does logging and stats
import json

# I want to make this fuck so badddd
# fuck it. I'll revert later if u want
class fuck:

    stat_file = None
    stat_obj = None

    def __init__(self, stat_file):
        self.stat_file = open(stat_file, "r+")
        
        try:
            self.stat_obj = json.load(self.stat_file)
        except:
            # Probably empty file. Will need to make new one
            self.stat_obj = {
                "drinks": {},
                "pumps": {}
            }

            self.update_statfile()

    def update_statfile(self):
        self.stat_file.seek(0)
        json.dump(self.stat_obj, self.stat_file)
        self.stat_file.truncate()
        