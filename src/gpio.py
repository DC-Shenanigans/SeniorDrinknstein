import board
import digitalio

class BasicGPIO():
    def __init__(self):
        print("setting up basic GPIO")
        self.pin_settings = {}
        self.pin_settings["GP16"] = {"pin":board.GP16, "drink":"rum"}
        self.pin_settings["GP17"] = {"pin":board.GP17, "drink":"coke"}

        self.button_settings = {}
        self.button_settings["GP14"] = {"pin":board.GP14, "drink":"Rum & Coke"}
        self.button_settings["GP15"] = {"pin":board.GP15, "drink":"Gin & Tonic"}
        
        self.initialize_gpio()

    def initialize_gpio(self):
        for target_gpio in self.pin_settings:
            self.initialize_digital_output(target_gpio)
        for target_gpio in self.button_settings:
            self.initialize_button_pull_down(target_gpio)
            
    def initialize_button_pull_down(self, target_gpio):

        if "object" in self.button_settings[f'{target_gpio}']:
            print("Already initialized pin!!!")
            return None
        
        if (target_gpio in self.button_settings):
            self.button_settings[f'{target_gpio}']["object"] = digitalio.DigitalInOut(self.button_settings[f'{target_gpio}']["pin"])
            self.button_settings[f'{target_gpio}']["object"].switch_to_input(pull=digitalio.Pull.DOWN)

        else:
            print("NOT A VALID PIN")

    def initialize_digital_output(self, target_gpio):
        if ("object" in self.pin_settings[f'{target_gpio}']):
            print("Already initialized pin!!!")
            return None
        
        if (target_gpio in self.pin_settings):
            self.pin_settings[f'{target_gpio}']["object"] = digitalio.DigitalInOut(self.pin_settings[f'{target_gpio}']["pin"])
            self.pin_settings[f'{target_gpio}']["object"].direction = digitalio.Direction.OUTPUT

        else:
            print("NOT A VALID PIN")
    
    def toggle_pin_state(self, target_gpio):
        if(self.pin_settings[f'{target_gpio}']["object"].value is True):
            self.pin_settings[f'{target_gpio}']["object"].value = False
        else:
            self.pin_settings[f'{target_gpio}']["object"].value = True

    