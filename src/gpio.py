import board
import digitalio
from src.configs import load_from_json

class BasicGPIO():
    def __init__(self):
        print("setting up GPIO pins...")

        self.pin_settings = load_from_json('pin_settings.json')
        self.button_settings = load_from_json('button_settings.json')

        # Convert string pin names to actual board pins
        for key, setting in self.pin_settings.items():
            if 'pin' in setting:
                setting['pin'] = getattr(board, setting['pin'])

        for key, setting in self.button_settings.items():
            if 'pin' in setting:
                setting['pin'] = getattr(board, setting['pin'])

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
        

