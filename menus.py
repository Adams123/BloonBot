from pyautogui import *
import pyautogui
from time import sleep
from colorama import Fore

from mouseUtils import *
from constants import *

def menu_check():
    while True:  # Not doing anything until menu screen is open
        menu_on = pyautogui.locateOnScreen(menu_path, grayscale=True, confidence=CONFIDENCE)
        if menu_on != None:
            print(f'{Fore.RED}Menu screen found. Continuing...')
            break
        else:
            print(f'{Fore.GREEN}Menu screen not found. Trying again...')
            sleep(2)

def Start_Select_Map():
    menu_check()
    print(f'{Fore.CYAN}Selecting map...')
    click("HOME_MENU_START")  # Move Mouse and click from Home Menu, Start
    click("EXPERT_SELECTION")  # Move Mouse to expert and click
    click("RIGHT_ARROW_SELECTION")  # Move Mouse to arrow and click
    click("DARK_CASTLE")  # Move Mouse to Dark Castle
    click("EASY_MODE")  # Move Mouse to select easy mode
    click("STANDARD_GAME_MODE")  # Move mouse to select Standard mode
    click("OVERWRITE_SAVE")  # Move mouse to overwrite save if exists
    print(f'{Fore.CYAN}Map selected.')