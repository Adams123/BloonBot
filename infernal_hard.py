from numpy import place
from pyautogui import *
import pyautogui
from time import sleep
import colorama
from colorama import Fore

from mouseUtils import *
from constants import * 
from gameutils import * 

colorama.init(autoreset=True)

def start():

    print(f'{Fore.CYAN}Game started.')

    place_tower("HERO", "HERO_LOCATION")
    
    press_key("space")  # Start the game
    press_key("space")  # Fast forward the game

    place_tower("NINJA", "NINJA_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")
    upgrade_tower('/', "NINJA_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")
    upgrade_tower(',', "NINJA_LOCATION")

    place_tower("SUBMARINE", "SUB_LOCATION_1")
    upgrade_tower(",", "SUB_LOCATION_1")
    upgrade_tower(",", "SUB_LOCATION_1")
    upgrade_tower(".", "SUB_LOCATION_1")
    upgrade_tower(".", "SUB_LOCATION_1")

    place_tower("SUBMARINE", "SUB_LOCATION_2")
    upgrade_tower(",", "SUB_LOCATION_2")
    upgrade_tower(",", "SUB_LOCATION_2")
    upgrade_tower("/", "SUB_LOCATION_2")
    upgrade_tower("/", "SUB_LOCATION_2")
    upgrade_tower("/", "SUB_LOCATION_2")
    upgrade_tower("/", "SUB_LOCATION_2")

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

    place_tower("BUCCANEER","BUCANEER_LOCATION")
    upgrade_tower(',', "BUCANEER_LOCATION")
    upgrade_tower(',', "BUCANEER_LOCATION")
    upgrade_tower('.', "BUCANEER_LOCATION")
    upgrade_tower('.', "BUCANEER_LOCATION")
    upgrade_tower(',', "BUCANEER_LOCATION")
    upgrade_tower(',', "BUCANEER_LOCATION")

    place_tower("SUBMARINE", "SUB_LOCATION_3")
    upgrade_tower(",", "SUB_LOCATION_3")
    upgrade_tower(",", "SUB_LOCATION_3")
    upgrade_tower("/", "SUB_LOCATION_3")
    upgrade_tower("/", "SUB_LOCATION_3")
    upgrade_tower("/", "SUB_LOCATION_3")
    upgrade_tower("/", "SUB_LOCATION_3")

    upgrade_tower('.', "SUB_LOCATION_1")

    place_tower("SUBMARINE", "SUB_LOCATION_4")
    upgrade_tower(",", "SUB_LOCATION_4")
    upgrade_tower(",", "SUB_LOCATION_4")
    upgrade_tower("/", "SUB_LOCATION_4")
    upgrade_tower("/", "SUB_LOCATION_4")
    upgrade_tower("/", "SUB_LOCATION_4")
    upgrade_tower("/", "SUB_LOCATION_4")

    place_tower("SNIPER", "SNIPER_LOCATION")
    upgrade_tower(",", "SNIPER_LOCATION")
    upgrade_tower(",", "SNIPER_LOCATION")
    upgrade_tower(",", "SNIPER_LOCATION")
    upgrade_tower("/", "SNIPER_LOCATION")
    upgrade_tower("/", "SNIPER_LOCATION")