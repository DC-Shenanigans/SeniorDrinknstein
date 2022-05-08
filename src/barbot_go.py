# All rights are yours to do what you want with. 
# I can't stop you, I'm just pixels on a screen.

class BarbotGo() :
    run_mode = None
    def __init__ (self, mode="CONSOLE"):
        self.run_mode = mode
        self.print_to_display("Starting up Dr. McGillicutty's Magic Drink Elixir Mixer")
        # TODO: Load in config, for now we can use a placeholder
        # Need: GPIO Config (set drink per gpio), Drink mix config (what  makes what drink)
        # TODO: Initialize all hardware
        # TODO: Initialize UX
    
    def print_to_display(self, text):
        if(self.run_mode == "CONSOLE"):
            print(text)
        else:
            print("IDKWTFUDO, DO IT BETTER")



        


