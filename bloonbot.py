from pyautogui import *
import pyautogui
import time
from time import sleep
import colorama
from colorama import Fore

from mouseUtils import *
from constants import * 
from gameutils import * 

from menus import Start_Select_Map

colorama.init(autoreset=True)

def Main_Game():

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
    place_tower("BOOMERANG", "MORTAR_LOCATION_1")
    place_tower("BOOMERANG", "MORTAR_LOCATION_2")
    place_tower("BOOMERANG", "MORTAR_LOCATION_3")
    place_tower("BOOMERANG", "MORTAR_LOCATION_4")

def Exit_Game():

    Level_Up_Check(1)

    found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=CONFIDENCE)

    while found == None:
        sleep(2)
        print('Next button not found.')
        found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=CONFIDENCE)

    print(f'{Fore.CYAN}Game ended. Going back to homescreen...')
    pyautogui.click(x=960, y=910)
    sleep(2)
    pyautogui.click(x=790, y=850)
    sleep(6)
    print(f'{Fore.CYAN}Back in homescreen. Checking for event notification...')
    sleep(2)
    for x in range(0, 4):  # checking for menu screen
        menu_on = pyautogui.locateOnScreen(menu_path, grayscale=True, confidence=CONFIDENCE)
        if menu_on != None:
            print(f'{Fore.CYAN}Menu screen found. Continuing...')
            break
        else:
            click("EVENT_EXIT")
            sleep(3)

#pyautogui.mouseInfo()
sleep(5)
while True:
    Start_Select_Map()
    Main_Game()
    Exit_Game()

