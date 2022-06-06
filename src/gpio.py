import board
import digitalio


class BasicGPIO():
    def __init__(self):
        print("setting up basic GPIO")
        
        self.pin_settings = {}
        self.pin_settings["GP16"] = {"pin": board.GP16, "drink": "rum"}
        self.pin_settings["GP17"] = {"pin": board.GP17, "drink": "coke"}
        self.pin_settings["GP19"] = {"pin": board.GP19, "drink": "gin"}
        self.pin_settings["GP20"] = {"pin": board.GP20, "drink": "tonic"}
        self.pin_settings["GP21"] = {"pin": board.GP21, "drink": "tequila"}
        self.pin_settings["GP22"] = {"pin": board.GP22, "drink": "margmix"}
        self.pin_settings["GP26"] = {"pin": board.GP26, "drink": "maitaimix"}
        self.pin_settings["GP27"] = {"pin": board.GP27, "drink": "whitewine"}
        self.pin_settings["GP28"] = {"pin": board.GP28, "drink": "redwine"}
        self.pin_settings["green"] = {
            "pin": board.GP10, "color": "green", "status": False, "mode": None}
        self.pin_settings["red"] = {
            "pin": board.GP11, "color": "red", "status": True, "mode": "solid"}
        self.pin_settings["loud"] = {
            "pin": board.GP12, "color": "loud", "status": False}

        self.button_settings = {}
        self.button_settings["GP2"] = {"pin": board.GP2, "drink": "Rum & Coke"}
        self.button_settings["GP3"] = {
            "pin": board.GP3, "drink": "Gin & Tonic"}
        self.button_settings["GP4"] = {"pin": board.GP4, "drink": "Margarita"}
        self.button_settings["GP5"] = {"pin": board.GP5, "drink": "Mai Tai"}
        self.button_settings["GP6"] = {"pin": board.GP6, "drink": "White Wine"}
        self.button_settings["GP7"] = {"pin": board.GP7, "drink": "Red Wine"}
        self.button_settings["GP8"] = {"pin": board.GP8, "drink": "Crash"}
        self.button_settings["GP9"] = {"pin": board.GP9, "drink": "Override"}

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
