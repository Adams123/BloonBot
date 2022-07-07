from pyautogui import *
import pyautogui
from time import sleep, time
from colorama import Fore

from mouseUtils import *
from constants import *

keyPaths = {
    ',': "1",
    '.': "2",
    '/': "3"
}

towerUpgradeLevels = {}

def place_tower(tower, location):

    while checkUntilMonkeyIsReady(tower) is False:
        print(f"Waiting for {tower} to be ready")
        Level_Up_Check(1)

    Level_Up_Check(1)
    print(f'{Fore.CYAN}Placing ' + tower + '...')
    move_mouse(button_positions[location])
    print(f'{Fore.CYAN}Clicking ' + monkeys[tower] + '...')
    pyautogui.click()
    print(f'{Fore.CYAN}' + tower + ' placed.')
    sleep(0.5)


def upgrade_tower(path, location):
    if(location in towerUpgradeLevels):
        if(path in towerUpgradeLevels[location]):
            towerUpgradeLevels[location][path] += 1
        else:
            towerUpgradeLevels[location][path] = 1
    else:
        towerUpgradeLevels[location] = {}
        towerUpgradeLevels[location][path] = 1

    click(location)
    while checkUntilUpgradeIsReady(path, location, towerUpgradeLevels[location][path]) is False:
        print(f"Waiting for {location}{path} to be ready")
        Level_Up_Check(1)

    print(f'{Fore.CYAN}Upgrading tower path ' + path + '...')
    press_key(path)
    sleep(1)
    press_key("esc")
    print(f'{Fore.CYAN}Path ' + path + ' upgraded.')
    sleep(0.5)
    print(f"Tower {location} is now {towerUpgradeLevels[location]}")

def checkUntilMonkeyIsReady(tower):
    path = "pictures\\selected.png"
    press_key(monkeys[tower])
    return pyautogui.locateOnScreen(path, confidence=CONFIDENCE) != None

def checkUntilUpgradeIsReady(key, towerLocation, level):
    tower = towerLocation.split("_")[0]
    upPath = keyPaths[key]
    path = f"pictures\\upgrades\\{tower}\\{upPath}\\{level}.png"
    return pyautogui.locateOnScreen(path, confidence=CONFIDENCE) != None
        

def Level_Up_Check(seconds):

    global overtime
    overtime = 0

    t_end = time() + seconds - 1

    while time() < t_end:
        found = pyautogui.locateOnScreen(level_up_path, grayscale=True, confidence=CONFIDENCE)

        if found != None:
            print(f'{Fore.RED}Level Up notification detected. Getting rid of it...')
            click("LEFT_INSTA")  # Accept lvl
            sleep(1)
            click("LEFT_INSTA")  # Accept knoledge
            sleep(1)
            
            click("LEFT_INSTA")  # unlock insta
            sleep(1)
            click("LEFT_INSTA")  # collect insta
            sleep(1)

            click("MID_INSTA")  # unlock insta
            sleep(1)
            click("MID_INSTA")  # collect insta
            sleep(1)

            click("RIGHT_INSTA")  # unlock r insta
            sleep(1)
            click("RIGHT_INSTA")  # collect r insta
            sleep(2)
            
            #press_key("space")  # Start the game
            print(f'{Fore.GREEN}Notification kyssed.')
        else:
            sleep(0.2)

    overtime = time() - t_end


def retarget_mortar(location):
    click(location)
    press_key('tab')
    press_key('tab')    
    click("BOMBER_TARGET")