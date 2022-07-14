from pyautogui import *
import pyautogui
from time import sleep, time
from colorama import Fore

from mouseUtils import move_mouse,press_key,click
from constants import *

keyPaths = {
    ',': "1",
    '.': "2",
    '/': "3"
}

towerUpgradeLevels = {}

def reset_towers_levels():
    global towerUpgradeLevels
    towerUpgradeLevels = {}

def place_tower(tower, location):

    while checkUntilMonkeyIsReady(tower) is False:
        print(f"Waiting for {tower} to be ready")
        levelUpCheck()

    levelUpCheck()
    print(f'{Fore.CYAN}Placing ' + tower + '...')
    click(location)
    print(f'{Fore.CYAN}' + tower + ' placed.')
    sleep(0.5)

## ADD +13
def levelup_tower(tower, locations):
    gameEnded = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=CONFIDENCE)
    levelup = 0
    while (gameEnded == None):
        levelUpCheck()
        if(checkUntilMonkeyIsReady(tower) and levelup < len(locations)):
            levelUpCheck()
            print(f'{Fore.CYAN}Placing ' + tower + '...')
            move_mouse(locations[levelup])
            print(f'{Fore.CYAN}Clicking ' + monkeys[tower] + '...')
            pyautogui.click()
            print(f'{Fore.CYAN}' + tower + ' placed.')
            sleep(0.5)
            levelup=levelup+1
        print('Level not finished!')
        gameEnded = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=CONFIDENCE)
    
    while gameEnded == None:
        print('Level not finished!')
        levelUpCheck()
        gameEnded = pyautogui.locateOnScreen(next_path, grayscale=True, confidence=CONFIDENCE)

def keepUpgrading(paths, towerName, location):
    click(location)
    for path in paths:
        upgrade_tower(path, towerName, location, singleUpgrade=False)
    press_key("esc")
    sleep(0.3)

def upgrade_tower(path, towerName, location, singleUpgrade=True):
    if(towerName in towerUpgradeLevels):
        if(path in towerUpgradeLevels[towerName]):
            towerUpgradeLevels[towerName][path] += 1
        else:
            towerUpgradeLevels[towerName][path] = 1
    else:
        towerUpgradeLevels[towerName] = {}
        towerUpgradeLevels[towerName][path] = 1

    if(singleUpgrade):
        click(location)
    while checkUntilUpgradeIsReady(path, towerName, towerUpgradeLevels[towerName][path]) is False:
        print(f"Waiting for {towerName} - path {keyPaths[path]} to be ready")
        levelUpCheck()

    print(f'{Fore.CYAN}Upgrading tower path ' + path + '...')
    levelUpCheck()
    press_key(path)
    sleep(0.2)
    if(singleUpgrade):
        levelUpCheck()
        press_key("esc")
    print(f'{Fore.CYAN}Path ' + path + ' upgraded.')
    sleep(0.5)
    print(f"Tower {towerName} is now {towerUpgradeLevels[towerName]}")

def checkUntilMonkeyIsReady(tower):
    path = "pictures\\selected.png"
    press_key(monkeys[tower])
    return pyautogui.locateOnScreen(path, confidence=CONFIDENCE) != None

def checkUntilUpgradeIsReady(key, towerLocation, level):
    tower = towerLocation.split("_")[0]
    upPath = keyPaths[key]
    path = f"pictures\\upgrades\\{tower}\\{upPath}\\{level}.png"
    return pyautogui.locateOnScreen(path, confidence=CONFIDENCE) != None

def sell_tower(towerLocation):
    click(towerLocation)
    press_key("backspace")

def findAndClick(image):
    print("PROCURANDO" + image)
    location = pyautogui.locateOnScreen(image, confidence = CONFIDENCE)
    print(location)
    sleep(0.2)
    pyautogui.click(location)

def pick_hero(hero):
    confirm_hero = "pictures\\heroes\\choose.png"
    heroes_menu = "pictures\\heroes\\heroes_menu.png"
    hero_location = ""
    match hero:
        case "OBYN":
            hero_location = "pictures\\heroes\\obyn.png"
        case "QUINCY":
            hero_location = "pictures\\heroes\\quincy.png"
    findAndClick(heroes_menu)
    sleep(0.5)
    findAndClick(hero_location)
    sleep(0.5)
    findAndClick(confirm_hero)
    sleep(0.5)
    findAndClick(return_button_path)


def levelUpCheck():
    found = pyautogui.locateOnScreen(level_up_path, grayscale=True, confidence=CONFIDENCE)
    if(found):
        pyautogui.moveTo(found)
        sleep(0.3)
        pyautogui.click()
        sleep(0.5)
        pyautogui.click()
        sleep(0.3)


def retarget_mortar(location):
    click(location)
    press_key('tab')
    press_key('tab')    
    click("BOMBER_TARGET")