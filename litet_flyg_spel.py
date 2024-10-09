import time
import os

EMOJI = ["🧑‍✈️","👨‍✈️","👩‍✈️","🐦","🦅","🪶","🪽","🌍","🌎","🌏","🗺️","🗾","🧭","🗽","🛩️","🛫","🛬","🪂","💺","🚀","🧳","🕹️","📦","🛃","🛄","🛅"]
WORLDS = ["🌍","🌎","🌏"]
PILOT = ["🧑‍✈️","👨‍✈️","👩‍✈️"]
WELCOME = "Välkommen till Lindas Luft Hansa🪽"
TIME_DELAY = 0.1

def typewriter(message, time_delay, end_newline=True):
    for i in message:
        print(i, end='', flush=True)
        time.sleep(time_delay)
    if end_newline:
        print()
        

class Pilot:
    def __init__(self, emoji, namn):
        self.emoji = emoji
        self.namn = namn

class Flygplan:

    def __init__(self, pilot:Pilot):
        """Pilot ska vara en emoji"""
        self.pilot = pilot

    def hälsa_på_piloten(self):
        print(f"{self.pilot.emoji} Hejsan! Mitt namn är {self.pilot.namn} och jag kommer vara er kapten idag!")

    def flyg_till_destination(self, destination, distance):
        print("Startar planet:")
        for t in range(20):
            if t%2:
                print("\r🕹️", end='', flush=True)
            else:
                print("\r   ", end='', flush=True)

            time.sleep(0.2)

        print("\nPlanet har startat! Redo för flyg! Kollar kartan🗺️")
        time.sleep(3)
        clear_screen()
        p_f = "🛩️"
        for i in range(distance):
            print("\r🗺️" + ' '*i + p_f + " "*(distance-i-1) +"🗾", end='', flush=True)
            time.sleep(TIME_DELAY)
        
        print(f" Du har anlänt till {destination}! Tack för att du har flygit med oss {self.pilot.emoji}")

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    elif os.name == "posix":
        os.system('clear')
        
def start_up_function():
    typewriter(WELCOME, TIME_DELAY)
    print("Laddar in flotta!")

    for i in range(len(WELCOME)):
        print('\r'+' '*i + "🛬", end='', flush=True)
        time.sleep(TIME_DELAY)

    for i in range(len(WELCOME)):
        earth = WORLDS[i%3]
        print('\b\b' + earth, end='', flush=True)
        time.sleep(0.2)

    print("\nUppladdning klar!")
    time.sleep(2)
    clear_screen()


if __name__ == "__main__":
    # start_up_function()
    top_gun = Pilot(PILOT[0], 'Maveric')
    fligt332 = Flygplan(top_gun)
    fligt332.flyg_till_destination("New York", 25)

    