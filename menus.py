from pyautogui import *
import pyautogui
from time import sleep
from colorama import Fore
from gameutils import pick_hero

from mouseUtils import *
from constants import *

selected_map = "INFERNAL_HARD"

def menu_check():
    while True:
        menu_on = pyautogui.locateOnScreen(menu_path, grayscale=True, confidence=CONFIDENCE)
        if menu_on != None:
            print(f'{Fore.RED}Menu screen found. Continuing...')
            break
        else:
            print(f'{Fore.GREEN}Menu screen not found. Trying again...')
            sleep(2)

def hero_check(map):
    if(pyautogui.locateOnScreen("pictures\\heroes\\quincy_picked.png", confidence = CONFIDENCE) == None):
        pick_hero(selected_map_config[map][2])

def Start_Select_Map(map):
    global selected_map
    selected_map = map
    menu_check()
    hero_check(map)
    print(f'{Fore.CYAN}Selecting map...')
    click("HOME_MENU_START")
    sleep(0.3)
    click("EXPERT_SELECTION")
    sleep(0.3)
    if(map == "DARK_CASTLE"):
        click("RIGHT_ARROW_SELECTION")

    pyautogui.click(infernal_hard["MAP_LOCATION"]) #TODO generic
    sleep(0.5)
    pyautogui.click(1307,415)
    sleep(0.5)
    click("STANDARD_GAME_MODE")
    sleep(0.5)
    click("OVERWRITE_SAVE")
    print(f'{Fore.CYAN}Map selected.')

def check_for_events():
    event = pyautogui.locateOnScreen(event_path, confidence = CONFIDENCE)
    if(event != None):
        print("Event found!")
        pyautogui.click(event)
        sleep(3)
        insta_monkey = pyautogui.locateOnScreen(insta_monkey_path, grayscale = True, confidence = CONFIDENCE)
        while(insta_monkey != None):
            pyautogui.click(insta_monkey)
            sleep(1)
            pyautogui.click(insta_monkey)
            sleep(1)
            insta_monkey = pyautogui.locateOnScreen(insta_monkey_path, grayscale = True, confidence = CONFIDENCE)
        click(pyautogui.locateOnScreen(return_button_path, confidence = CONFIDENCE))
        sleep(3)
