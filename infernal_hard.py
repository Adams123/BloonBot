from numpy import place
from pyautogui import *
import pyautogui
from time import sleep
import colorama
from colorama import Fore

from mouseUtils import *
from constants import * 
from gameutils import * 
from menus import selected_map

colorama.init(autoreset=True)

def start():

    print(f'{Fore.CYAN}Game started.')

    global button_positions
    button_positions.update(default_positions)
    button_positions.update(selected_map_config[selected_map][0])

    place_tower("HERO", "HERO_LOCATION")
    
    press_key("space")  # Start the game
    press_key("space")  # Fast forward the game

    place_tower("NINJA", "NINJA_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")
    upgrade_tower('/', "NINJA_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")

    place_tower("SUBMARINE", "SUBMARINE_LOCATION_1")
    upgrade_tower(",", "SUBMARINE_LOCATION_1")
    upgrade_tower(",", "SUBMARINE_LOCATION_1")
    upgrade_tower(".", "SUBMARINE_LOCATION_1")
    upgrade_tower(".", "SUBMARINE_LOCATION_1")

    place_tower("SUBMARINE", "SUBMARINE_LOCATION_2")
    upgrade_tower(",", "SUBMARINE_LOCATION_2")
    upgrade_tower(",", "SUBMARINE_LOCATION_2")
    upgrade_tower("/", "SUBMARINE_LOCATION_2")
    upgrade_tower("/", "SUBMARINE_LOCATION_2")
    upgrade_tower("/", "SUBMARINE_LOCATION_2")
    upgrade_tower("/", "SUBMARINE_LOCATION_2")

    upgrade_tower(',', "NINJA_LOCATION")
    upgrade_tower('/', "NINJA_LOCATION")

    place_tower("ALCHEMIST", "ALCHEMIST_LOCATION")
    upgrade_tower(',', "ALCHEMIST_LOCATION")
    upgrade_tower(',', "ALCHEMIST_LOCATION")
    upgrade_tower(',', "ALCHEMIST_LOCATION")
    upgrade_tower('.', "ALCHEMIST_LOCATION")
    upgrade_tower('.', "ALCHEMIST_LOCATION")
    upgrade_tower(',', "ALCHEMIST_LOCATION")

    place_tower("ACE", "ACE_LOCATION")
    upgrade_tower('/',"ACE_LOCATION")
    upgrade_tower('/',"ACE_LOCATION")
    upgrade_tower(',',"ACE_LOCATION")
    upgrade_tower(',',"ACE_LOCATION")
    upgrade_tower('/',"ACE_LOCATION")

    place_tower("VILLAGE", "VILLAGE_LOCATION")
    upgrade_tower('.', "VILLAGE_LOCATION")
    upgrade_tower('.', "VILLAGE_LOCATION")
    upgrade_tower('/', "VILLAGE_LOCATION")
    upgrade_tower('/', "VILLAGE_LOCATION")

    sell_tower("ALCHEMIST_LOCATION")
    upgrade_tower('/',"ACE_LOCATION")
    place_tower("ALCHEMIST", "ALCHEMIST_LOCATION")
    upgrade_tower(',', "ALCHEMIST_LOCATION")
    upgrade_tower(',', "ALCHEMIST_LOCATION")
    upgrade_tower(',', "ALCHEMIST_LOCATION")
    upgrade_tower('.', "ALCHEMIST_LOCATION")
    upgrade_tower('.', "ALCHEMIST_LOCATION")
    upgrade_tower(',', "ALCHEMIST_LOCATION")

    place_tower("BUCCANEER","BUCCANEER_LOCATION")
    upgrade_tower(',', "BUCCANEER_LOCATION")
    upgrade_tower(',', "BUCCANEER_LOCATION")
    upgrade_tower('.', "BUCCANEER_LOCATION")
    upgrade_tower('.', "BUCCANEER_LOCATION")
    upgrade_tower(',', "BUCCANEER_LOCATION")
    upgrade_tower(',', "BUCCANEER_LOCATION")

    place_tower("SUBMARINE", "SUBMARINE_LOCATION_3")
    upgrade_tower(",", "SUBMARINE_LOCATION_3")
    upgrade_tower(",", "SUBMARINE_LOCATION_3")
    upgrade_tower("/", "SUBMARINE_LOCATION_3")
    upgrade_tower("/", "SUBMARINE_LOCATION_3")
    upgrade_tower("/", "SUBMARINE_LOCATION_3")
    upgrade_tower("/", "SUBMARINE_LOCATION_3")

    upgrade_tower('.', "SUBMARINE_LOCATION_1")

    place_tower("SUBMARINE", "SUBMARINE_LOCATION_4")
    upgrade_tower(",", "SUBMARINE_LOCATION_4")
    upgrade_tower(",", "SUBMARINE_LOCATION_4")
    upgrade_tower("/", "SUBMARINE_LOCATION_4")
    upgrade_tower("/", "SUBMARINE_LOCATION_4")
    upgrade_tower("/", "SUBMARINE_LOCATION_4")
    upgrade_tower("/", "SUBMARINE_LOCATION_4")

    place_tower("SNIPER", "SNIPER_LOCATION")
    upgrade_tower(",", "SNIPER_LOCATION")
    upgrade_tower(",", "SNIPER_LOCATION")
    upgrade_tower(",", "SNIPER_LOCATION")
    upgrade_tower("/", "SNIPER_LOCATION")
    upgrade_tower("/", "SNIPER_LOCATION")