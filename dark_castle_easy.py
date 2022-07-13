from pyautogui import *
import colorama
from colorama import Fore

from mouseUtils import *
from gameutils import * 

colorama.init(autoreset=True)

def start():

    print(f'{Fore.CYAN}Game started.')

    place_tower("HERO", "HERO_LOCATION")
    
    press_key("space")  # Start the game
    press_key("space")  # Fast forward the game

    place_tower("SUBMARINE", "SUBMARINE_LOCATION")
    upgrade_tower(',', "SUBMARINE_LOCATION")
    upgrade_tower('/', "SUBMARINE_LOCATION")
    upgrade_tower('/', "SUBMARINE_LOCATION")
    upgrade_tower(',', "SUBMARINE_LOCATION")
    place_tower("NINJA", "NINJA_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")
    upgrade_tower('/', "NINJA_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")
    upgrade_tower('/', "SUBMARINE_LOCATION")
    upgrade_tower('/', "SUBMARINE_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")

    levelup_tower("BOOMERANG")