from pyautogui import *
import pyautogui
import time
from time import sleep
import colorama
from colorama import Fore

import dark_castle_easy
import infernal_hard as infernal

from mouseUtils import *
from constants import * 
from gameutils import *
from menus import selected_map


from menus import Start_Select_Map, check_for_events

colorama.init(autoreset=True)

def Main_Game():
    if(selected_map == "DARK_CASTLE"):
        dark_castle_easy.start()
    elif(selected_map == "INFERNAL_HARD"):
        infernal.start()

def Exit_Game():

    Level_Up_Check(1)

    found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=CONFIDENCE)

    while found == None:
        sleep(2)
        print('Next button not found.')
        found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=CONFIDENCE)

    print(f'{Fore.CYAN}Game ended. Going back to homescreen...')
    sleep(2)
    back_btn = pyautogui.locateOnScreen(start_menu_path, grayscale = True, confidence = CONFIDENCE)
    pyautogui.click(back_btn)
    print(f'{Fore.CYAN}Back in homescreen. Checking for event notification...')
    sleep(2)

    reset_towers_levels()

    check_for_events()

    for x in range(0, 4):  # checking for menu screen
        menu_on = pyautogui.locateOnScreen(menu_path, grayscale=True, confidence=CONFIDENCE)
        if menu_on != None:
            print(f'{Fore.CYAN}Menu screen found. Continuing...')
            break
        else:
            click("EVENT_EXIT")
            sleep(3)

sleep(5)

#pyautogui.mouseInfo()

#while True:
Start_Select_Map("INFERNAL_HARD")
Main_Game()
Exit_Game()
