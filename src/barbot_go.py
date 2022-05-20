# All rights are yours to do what you want with. 
# I can't stop you, I'm just pixels on a screen.

from src.configs import load_from_json

class BarbotGo() :
    run_mode = None
    def __init__ (self, mode="CONSOLE"):
        self.run_mode = mode
        self.print_to_display("Starting up Dr. McGillicutty's Magic Drink Elixir Mixer")
        # TODO: Load in config, for now we can use a placeholder
        self.drink_list = load_from_json("./src/drinks_config.json")
        # Need: GPIO Config (set drink per gpio), Drink mix config (what  makes what drink)
        # TODO: Initialize all hardware
        # TODO: Initialize UX

    def main_menu(self):
        if(self.run_mode == "CONSOLE"):
            for idx,item in enumerate(self.drink_list):
                print("%d %s" % (idx, item["name"]))
            user_input = input("Please select a drink: ")

        else:
            # Poll the buttons
            user_input = 0
        try:
            self.drink_selection = self.drink_list[int(user_input)]
            # TO DO: Trigger make drink
            self.make_drink()
        except: 
            self.print_to_display("NOT A VALID OPTION.")

        

    def print_to_display(self, text):
        if(self.run_mode == "CONSOLE"):
            print(text)
        else:
            print("IDKWTFUDO, DO IT BETTER")

    def make_drink(self):
        self.print_to_display(f"Making {self.drink_selection['name']}...")
        # use drink config to mix drink
        order = []
        ingredients = self.drink_selection['ingredients']
        
        print(ingredients)

        


