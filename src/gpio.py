import board
import digitalio


class BasicGPIO():
    def __init__(self):
        print("setting up basic GPIO")
        
        self.pin_settings = {}
        self.pin_settings["GP2"] = {"pin": board.GP2, "drink": "rum"}
        self.pin_settings["GP3"] = {"pin": board.GP3, "drink": "pina_colada"}
        self.pin_settings["GP4"] = {"pin": board.GP4, "drink": "daqmix"}
        self.pin_settings["GP5"] = {"pin": board.GP5, "drink": "malort"}
        self.pin_settings["GP6"] = {"pin": board.GP6, "drink": "tequila"}
        self.pin_settings["GP7"] = {"pin": board.GP7, "drink": "margmix"}
        self.pin_settings["GP16"] = {"pin": board.GP16, "drink": "maitaimix"}
        self.pin_settings["GP17"] = {"pin": board.GP17, "drink": "whitewine"}
        self.pin_settings["GP19"] = {"pin": board.GP19, "drink": "redwine"}
        self.pin_settings["green"] = {
            "pin": board.GP20, "color": "green", "status": False, "mode": None}
        self.pin_settings["red"] = {
            "pin": board.GP21, "color": "red", "status": True, "mode": "solid"}
        self.pin_settings["loud"] = {
            "pin": board.GP22, "color": "loud", "status": False}

        self.button_settings = {}
        self.button_settings["GP8"] = {"pin": board.GP8, "drink": "Mai Tai"}
        self.button_settings["GP9"] = {"pin": board.GP9, "drink": "Pina Colada"}
        self.button_settings["GP10"] = {"pin": board.GP10, "drink": "Mango Daquiri"}
        self.button_settings["GP11"] = {"pin": board.GP11, "drink": "Margarita"}
        self.button_settings["GP12"] = {"pin": board.GP12, "drink": "Red Wine"}
        self.button_settings["GP13"] = {"pin": board.GP13, "drink": "White Wine"}
        self.button_settings["GP14"] = {"pin": board.GP14, "drink": "Malort"}
        self.button_settings["GP15"] = {"pin": board.GP15, "drink": "Rum"}

        self.initialize_gpio()

    def initialize_gpio(self):
        for target_gpio in self.pin_settings:
            self.initialize_digital_output(target_gpio)
        for target_gpio in self.button_settings:
            self.initialize_button_pull_down(target_gpio)
        led = digitalio.DigitalInOut(board.LED)
        led.direction = digitalio.Direction.OUTPUT
        led.value = True

    def initialize_button_pull_down(self, target_gpio):

        if "object" in self.button_settings[f'{target_gpio}']:
            print("Already initialized pin!!!")
            return None

        if (target_gpio in self.button_settings):
            self.button_settings[f'{target_gpio}']["object"] = digitalio.DigitalInOut(
                self.button_settings[f'{target_gpio}']["pin"])
            self.button_settings[f'{target_gpio}']["object"].switch_to_input(
                pull=digitalio.Pull.DOWN)

        else:
            print("NOT A VALID PIN")

    def initialize_digital_output(self, target_gpio):
        if ("object" in self.pin_settings[f'{target_gpio}']):
            print("Already initialized pin!!!")
            return None

        if (target_gpio in self.pin_settings):
            self.pin_settings[f'{target_gpio}']["object"] = digitalio.DigitalInOut(
                self.pin_settings[f'{target_gpio}']["pin"])
            self.pin_settings[f'{target_gpio}']["object"].direction = digitalio.Direction.OUTPUT

        else:
            print("NOT A VALID PIN")

    def toggle_pin_state(self, target_gpio):
        if(self.pin_settings[f'{target_gpio}']["object"].value is True):
            self.pin_settings[f'{target_gpio}']["object"].value = False
        else:
            self.pin_settings[f'{target_gpio}']["object"].value = True
    
    def purge_mode(self, button_gpio, relay_gpio):
        # set the gpio to high while the button is held
        while(self.button_settings[f'{button_gpio}']["object"].value == True):
            self.pin_settings[relay_gpio]["object"].value = True
        self.pin_settings[relay_gpio]["object"].value = False
        

