from pyautogui import *
import threading
import pyautogui
import time
from time import sleep
import colorama
from colorama import Fore, Back, Style

from mouseUtils import *
from constants import *

colorama.init(autoreset=True)


def menu_check():
    while True:  # Not doing anything until menu screen is open
        menu_on = pyautogui.locateOnScreen(menu_path, grayscale=True, confidence=CONFIDENCE)
        if menu_on != None:
            print(f'{Fore.RED}Menu screen found. Continuing...')
            break
        else:
            print(f'{Fore.GREEN}Menu screen not found. Trying again...')
            sleep(2)


def hero_obyn_check():

    menu_check()

    print(f'{Fore.CYAN}Checking for OBYN...')
    found = pyautogui.locateOnScreen(obyn_hero_path, grayscale=True, confidence=CONFIDENCE)

    if found == None:
        print(f'{Fore.CYAN}Not found. Selecting OBYN...')
        click("HERO_SELECT")
        click("SELECT_OBYN")
        click("CONFIRM_HERO")
        press_key("esc")
        print(f'{Fore.CYAN}OBYN selected.')


def place_tower(tower, location):

    Level_Up_Check(1)
    print(f'{Fore.CYAN}Placing ' + tower + '...')
    move_mouse(button_positions[location])
    print(f'{Fore.CYAN}Clicking ' + monkeys[tower] + '...')
    press_key(monkeys[tower])
    pyautogui.click()
    print(f'{Fore.CYAN}' + tower + ' placed.')
    sleep(0.5)


def upgrade_tower(path, location):

    Level_Up_Check(1)
    print(f'{Fore.CYAN}Upgrading tower path ' + path + '...')
    click(location)
    press_key(path)
    time.sleep(1)
    press_key("esc")
    print(f'{Fore.CYAN}Path ' + path + ' upgraded.')
    sleep(0.5)

def CheckUntilMonkeyIsReady(monkey):
    path = "pictures\\monkeys\\{monkey}.png"
    while(pyautogui.locateOnScreen(path, grayscale=True, confidence=CONFIDENCE) != None):
        Level_Up_Check(1)
    return pyautogui.locateOnScreen(path, grayscale=True, confidence=CONFIDENCE)


def Level_Up_Check(seconds):

    global overtime
    overtime = 0

    t_end = time.time() + seconds - 1

    while time.time() < t_end:
        found = pyautogui.locateOnScreen(level_up_path, grayscale=True, confidence=CONFIDENCE)

        if found != None:
            print(f'{Fore.RED}Level Up notification detected. Getting rid of it...')
            click("LEFT_INSTA")  # Accept lvl
            time.sleep(1)
            click("LEFT_INSTA")  # Accept knoledge
            time.sleep(1)
            
            click("LEFT_INSTA")  # unlock insta
            time.sleep(1)
            click("LEFT_INSTA")  # collect insta
            time.sleep(1)

            click("MID_INSTA")  # unlock insta
            time.sleep(1)
            click("MID_INSTA")  # collect insta
            time.sleep(1)

            click("RIGHT_INSTA")  # unlock r insta
            time.sleep(1)
            click("RIGHT_INSTA")  # collect r insta
            time.sleep(2)
            
            #press_key("space")  # Start the game
            print(f'{Fore.GREEN}Notification kyssed.')
        else:
            sleep(0.2)

    overtime = time.time() - t_end


def event_check():

    found = pyautogui.locateOnScreen(event_path, grayscale=True, confidence=CONFIDENCE)

    if found != None:
        print(f"{Fore.RED}Event notification detected. Getting rid of it...")
        click("EVENT_COLLECTION")  # DUE TO EVENT:
        time.sleep(1)
        click("LEFT_INSTA")  # unlock insta
        time.sleep(1)
        click("LEFT_INSTA")  # collect insta
        time.sleep(1)
        click("RIGHT_INSTA")  # unlock r insta
        time.sleep(1)
        click("RIGHT_INSTA")  # collect r insta
        time.sleep(1)
        click("F_LEFT_INSTA")
        time.sleep(1)
        click("F_LEFT_INSTA")
        time.sleep(1)
        click("MID_INSTA")  # unlock insta
        time.sleep(1)
        click("MID_INSTA")  # collect insta
        time.sleep(1)
        click("F_RIGHT_INSTA")
        time.sleep(1)
        click("F_RIGHT_INSTA")
        time.sleep(1)

        time.sleep(1)
        click("EVENT_CONTINUE")

        # awe try to click 3 quick times to get out of the event mode, but also if event mode not triggered, to open and close profile quick
        click("EVENT_EXIT")
        print(f'{Fore.GREEN}Event notification kyssed.')
        time.sleep(1)


def retarget_mortar(location):
    click(location)
    press_key('tab')
    press_key('tab')    
    click("BOMBER_TARGET")


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
    
def castFirst():
    count = 0
    while count<27:
        press_key('1')
        count = count + 1
        print(f'Casted {count}')
        sleep(14)
    
def castSkill():
    t = threading.Thread(target=castFirst)
    t.start()
    return t
    


def Main_Game():

    sleep(3)

    print(f'{Fore.CYAN}Game started.')

    place_tower("HERO", "HERO_LOCATION")
    
    press_key("space")  # Start the game
    press_key("space")  # Fast forward the game

    Level_Up_Check(20 - overtime)
    place_tower("SUBMARINE", "SUBMARINE_LOCATION")  # 8.5
    Level_Up_Check(10 - overtime)
    upgrade_tower(',', "SUBMARINE_LOCATION")  # 18
    Level_Up_Check(18 - overtime)
    upgrade_tower('/', "SUBMARINE_LOCATION")  # 45
    Level_Up_Check(48 - overtime)
    upgrade_tower('/', "SUBMARINE_LOCATION")  # 24
    Level_Up_Check(24 - overtime)
    upgrade_tower(',', "SUBMARINE_LOCATION")  # 15
    Level_Up_Check(21 - overtime)
    place_tower("NINJA", "NINJA_LOCATION")  # 11.5
    Level_Up_Check(13 - overtime)
    upgrade_tower(',', "NINJA_LOCATION")  # 11.5
    Level_Up_Check(11 - overtime)
    upgrade_tower(',', "NINJA_LOCATION")  # 4
    Level_Up_Check(7 - overtime)
    upgrade_tower('/', "NINJA_LOCATION")  # 12
    Level_Up_Check(14 - overtime)
    upgrade_tower(',', "NINJA_LOCATION")  # 23
    Level_Up_Check(20 - overtime)
    upgrade_tower('/', "SUBMARINE_LOCATION")  # 39
    Level_Up_Check(49 - overtime)
    upgrade_tower('/', "SUBMARINE_LOCATION")  # 40
    Level_Up_Check(47 - overtime)
    upgrade_tower(',', "NINJA_LOCATION")
    Level_Up_Check(18 - overtime)
    place_tower("HELI", "MORTAR_LOCATION_1")
    retarget_mortar("MORTAR_LOCATION_1")
    Level_Up_Check(14 - overtime)
    place_tower("HELI", "MORTAR_LOCATION_2")
    retarget_mortar("MORTAR_LOCATION_2")
    Level_Up_Check(17 - overtime)
    place_tower("HELI", "MORTAR_LOCATION_3")
    retarget_mortar("MORTAR_LOCATION_3")
    Level_Up_Check(16 - overtime)
    place_tower("HELI", "MORTAR_LOCATION_4")
    retarget_mortar("MORTAR_LOCATION_4")
    Level_Up_Check(15 - overtime)
    


def Exit_Game():

    Level_Up_Check(1)

    found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=CONFIDENCE)

    while found == None:
        sleep(2)
        print('Next button not found.')
        found = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=CONFIDENCE)

    print(f'{Fore.CYAN}Game ended. Going back to homescreen...')
    pyautogui.click(x=960, y=910)
    time.sleep(2)
    pyautogui.click(x=790, y=850)
    time.sleep(6)
    print(f'{Fore.CYAN}Back in homescreen. Checking for event notification...')
    event_check()
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

#while True:
    #Start_Select_Map()
    #Main_Game()
    #Exit_Game()

