# All rights are yours to do what you want with. 
# I can't stop you, I'm just pixels on a screen.

from src.configs import load_from_json
from src.gpio import BasicGPIO
import time

class BarbotGo() :
    run_mode = None
    def __init__ (self, mode="CONSOLE"):
        self.run_mode = mode
        self.print_to_display("Starting up Dr. McGillicutty's Magic Drink Elixir Mixer")
        # TODO: Load in config, for now we can use a placeholder
        self.drink_list = load_from_json("drinks_config.json")
        # Need: GPIO Config (set drink per gpio), Drink mix config (what  makes what drink)
        # TODO: Initialize all hardware
        self.basic_gpio = BasicGPIO()
        # TODO: Initialize UX

    def main_menu(self):
        if(self.run_mode == "CONSOLE"):
            for idx,item in enumerate(self.drink_list):
                print("%d %s" % (idx, item["name"]))
            user_input = input("Please select a drink: ")
            try:
                self.drink_selection = self.drink_list[int(user_input)]
                # TO DO: Trigger make drink
                self.make_drink()
            except: 
                self.print_to_display("NOT A VALID OPTION.")
        else:
            # Poll the buttons
            for target_gpio in self.basic_gpio.button_settings:
                if self.basic_gpio.button_settings[f'{target_gpio}']["object"].value:
                    self.print_to_display(f"Button {target_gpio} is being pressed")
                    drink = self.basic_gpio.button_settings[f'{target_gpio}']["drink"]                    
                    for item in self.drink_list:
                        if drink == item["name"]:
                            self.print_to_display(f"This is a(n) {drink}")
                            self.drink_selection = item
                            self.make_drink()
                    
                    time.sleep(0.5)

    def print_to_display(self, text):
        if(self.run_mode == "CONSOLE"):
            print(text)
        else:
            print(text)
            # print("IDKWTFUDO, DO IT BETTER")

    def make_drink(self):
        self.print_to_display(f"Making {self.drink_selection['name']}...")
        # use drink config to mix drink
        ingredients = self.drink_selection['ingredients']
        
        # self.print_to_display(ingredients)
        
        liquor_to_pour = {}
        for ingredient in ingredients.keys():
            value = ingredients[ingredient]
            liquor_to_pour[ingredient] = value
        start_time = time.time()
        for liquor in liquor_to_pour.keys():
            self.print_to_display(f"Looking for {liquor}...")
            for target_gpio in self.basic_gpio.pin_settings:
                if self.basic_gpio.pin_settings[target_gpio]["drink"] == liquor:
                    timeout = liquor_to_pour[liquor]
                    self.print_to_display(f"pouring {liquor} for {timeout} ms...")
                    self.basic_gpio.toggle_pin_state(target_gpio)
                    time.sleep(timeout / 10)
                    self.basic_gpio.toggle_pin_state(target_gpio)
        


