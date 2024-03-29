# All rights are yours to do what you want with.
# I can't stop you, I'm just pixels on a screen.

import re
import time
from src.configs import load_from_json
from src.gpio import BasicGPIO
from src.screen import ScreenGo
from src.logwas import fuck         # Log was fuck


class BarbotGo():
    run_mode = None

    def __init__(self, mode="CONSOLE"):
        # Init screen
        self.screen = ScreenGo()

        # Set mode for some reason even though i'm going to require a screen
        self.run_mode = mode

        self.basic_gpio = BasicGPIO()
        
        # Print startup message
        self.print_to_display(
            "Starting up         \
Dr. McGillicutty's  \
Magic Drink Elixir  \
Mixer               ")

        self.drink_list = load_from_json("drinks_config.json")
        
        # See if we're in purge mode
        if self.basic_gpio.button_settings[f'GP13']["object"].value:
            self.basic_gpio.toggle_pin_state("red")
            self.purge_mode()
        
        # See if we're in mapping mode
        if self.basic_gpio.button_settings[f'GP14']["object"].value:
            self.basic_gpio.toggle_pin_state("red")
            self.basic_gpio.toggle_pin_state("green")
            self.button_mapping_mode()
        
        # self.button_mapping_mode()

        # prepare logger
        # There is something up with the truncate here :/
        self.log = fuck("stats.json")

        # Turn on the green light baby
        #time.sleep(5)


                
        self.basic_gpio.toggle_pin_state("green")
        self.idle_message = "Dr. McGillicutty's  \
Magic Drink Elixir  \
Mixer               \
Ready to mix!      "
        self.print_to_display(self.idle_message)
    
    def button_mapping_mode(self):
        self.print_to_display("Entering BUTTON MAPPING mode, one moment...")
        run_loop = True
        self.print_to_display("Now in BUTTON MAPPING mode BEEP BOOP BOP BEEEEEEP")
        count = 0
        while(run_loop):
            count +=1
            if count % 5000 == 0:
                self.print_to_display("Get back to mappin why don't ya!", True)

            for target_gpio in self.basic_gpio.button_settings:
                if self.basic_gpio.button_settings[f'{target_gpio}']["object"].value:
                    self.print_to_display(f"Button {target_gpio} was being pressed", True)
                    if self.basic_gpio.button_settings['GP8']["object"].value == True \
                        and self.basic_gpio.button_settings['GP9']["object"].value == True:
                        self.print_to_display("Exiting Mapping Mode ^_^")
                        run_loop = False
                    

    def purge_mode(self):
        self.print_to_display("Entering PURGE mode, one moment...")
        time.sleep(1)

        run_loop = True
        self.print_to_display("PURGE mode ENABLED")
        while(run_loop):
            for target_gpio in self.basic_gpio.button_settings:
                if self.basic_gpio.button_settings[f'{target_gpio}']["object"].value:
                    self.print_to_display(f"Button {target_gpio} is being pressed", True)
                    button_map = {
                        "GP8":"GP2",
                        "GP9":"GP3",
                        "GP10":"GP4",
                        "GP11":"GP5",
                        "GP12":"GP6",
                        "GP13":"GP7",
                        "GP14":"GP16",
                        "GP15":"GP17"
                    }
                    if self.basic_gpio.button_settings['GP8']["object"].value == True \
                        and self.basic_gpio.button_settings['GP9']["object"].value == True:
                        self.print_to_display("You escaped the PURGE! Now have a drink on Dr. McGillicutty ^_^")
                        run_loop = False
                    if self.basic_gpio.button_settings['GP8']["object"].value == True \
                        and self.basic_gpio.button_settings['GP12']["object"].value == True:
                        self.print_to_display("I'm sorry Dave, I can't let you do that")
                    if self.basic_gpio.button_settings['GP8']["object"].value == True \
                        and self.basic_gpio.button_settings['GP13']["object"].value == True:
                        self.print_to_display("PROTIP: Aask me no questions and I'll tell you no lies")
                    else:
                        liquor = self.basic_gpio.pin_settings[button_map[target_gpio]]["drink"]
                        if liquor == "malort":
                            self.print_to_display("KILL ALL HUMANS")
                        else:
                            self.print_to_display(f"Purging {liquor}....")

                        self.basic_gpio.purge_mode(target_gpio, button_map[target_gpio])

                        if liquor == "malort":
                            self.print_to_display("Thank you for using Dr. McGillicutty's Suicide Booth!")
                        else:
                            self.print_to_display(f"Done purging Dr. McGillicutty's {liquor}!")

                        self.print_to_display("PURGE mode ENABLED", immediate=True)

    def main_menu(self):
        if(self.run_mode == "CONSOLE"):
            for idx, item in enumerate(self.drink_list):
                print("%d %s" % (idx, item["name"]))
            user_input = input("Please select a drink: ")
            try:
                self.drink_selection = self.drink_list[int(user_input)]
                self.make_drink()
            except Exception as e:
                self.print_to_display(f"NOT A VALID OPTION. {e}")
        else:
            # Poll the buttons
            for target_gpio in self.basic_gpio.button_settings:
                if self.basic_gpio.button_settings[f'{target_gpio}']["object"].value:
                    self.print_to_display(
                        f"Button {target_gpio} is being pressed", True)
                    drink = self.basic_gpio.button_settings[f'{target_gpio}']["drink"]
                    for item in self.drink_list:
                        if drink == item["name"]:
                            article = "an" if re.search("^[AaEeIiOoUu]", drink) else "a"
                            self.print_to_display(f"This is {article} {drink}")
                            self.drink_selection = item
                            self.make_drink()

                    time.sleep(0.5)

    def print_to_display(self, text, immediate = False, letter_sleep = 0.01):
        # Clear the screen
        self.screen.write_to_screen(text, immediate, letter_sleep)
        print(text)
        # print("IDKWTFUDO, DO IT BETTER")

    def make_drink(self):
        self.print_to_display(f"Making {self.drink_selection['name']}...")

        # Set tower light to RED and turn off GREEN
        self.basic_gpio.toggle_pin_state("green")
        self.basic_gpio.toggle_pin_state("red")

        # stat drink being poured
        # self.log.stat_drink(self.drink_selection['name'])

        # use drink config to mix drink
        ingredients = self.drink_selection['ingredients']

        # self.print_to_display(ingredients)

        liquor_to_pour = {}
        for ingredient in ingredients.keys():
            value = ingredients[ingredient]
            liquor_to_pour[ingredient] = value

        drinklist = []
        for liquor in liquor_to_pour.keys():
            self.print_to_display(f"Looking for {liquor}...")
            for target_gpio in self.basic_gpio.pin_settings:
                if "drink" in self.basic_gpio.pin_settings[target_gpio]:
                    if self.basic_gpio.pin_settings[target_gpio]["drink"] == liquor:
                        booze = {
                            "name":liquor,
                            "gpio":target_gpio,
                            "pour_time":liquor_to_pour[liquor],
                            "pouring":False
                        }
                        
                        drinklist.append(booze)
        start_time = time.time()
        for liquor in drinklist:
            timeout = liquor["pour_time"]
            name = liquor["name"]
            self.print_to_display(
                f"pouring {name} for {timeout / 10:0.1f} seconds...", True)
            self.basic_gpio.toggle_pin_state(liquor["gpio"])
            liquor["pouring"] = True
        
        run = True
        finished_count = 0
        
        while run:
            print_text = ""
            actual_time_running = (time.time() - start_time) * 10

            for liquor in drinklist:
                if liquor["pouring"] and liquor["pour_time"] <= actual_time_running: #you have more time than the pour time turn off your gpio
                    self.basic_gpio.toggle_pin_state(liquor["gpio"])
                    liquor["pouring"] = False
                    # Log time poured so far for current pin
                    # self.log.stat_pump(liquor["gpio"], actual_time_running / 10)
                    finished_count += 1
                elif liquor["pouring"]:
                    booze = liquor["name"]
                    timeout = liquor["pour_time"] - actual_time_running
                    print_text += f"pouring {booze} for {timeout / 10:0.1f} seconds... \
"
            self.print_to_display(print_text, True)
            time.sleep(1)           

            if finished_count == len(liquor_to_pour):
                run = False

        self.print_to_display(
            f"Your {self.drink_selection['name']} is ready, please enjoy ^_^", False, 0.01)

        # Turn off the red light and on the green
        self.basic_gpio.toggle_pin_state("red")
        self.basic_gpio.toggle_pin_state("green")

        ## Make green flash for 5 seconds saying it's done
        #for index in range(0, 10):
        #    self.basic_gpio.toggle_pin_state("green")
        #    time.sleep(1)
        #    self.basic_gpio.toggle_pin_state("green")

        self.print_to_display(self.idle_message)
