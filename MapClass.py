from abc import ABC, abstractmethod
from email.policy import default
import pyautogui
from time import sleep
from colorama import Fore
from gameutils import *
from mouseUtils import click, press_key

class Map(ABC):
    def __init__(self, mapName: str, heroName: str, towerLocations: dict, difficulty: str, mapLevel = "expert"):
        self.mapName = mapName
        self.heroName = heroName
        self.towerLocations = towerLocations
        self.mapLevel = self.menu_paths[mapLevel]
        self.difficulty = self.menu_paths[difficulty]
        self.heroLocation = "pictures\\heroes\\"+heroName+".png"

    default_positions = {
        "HOME_MENU_START": [842, 936],
        "EXPERT_SELECTION": [1333, 978],
        "RIGHT_ARROW_SELECTION": [1644, 436],
        "OVERWRITE_SAVE": [1140, 730],
        "LEFT_INSTA": [805, 544],
        "RIGHT_INSTA": [1109, 543],
        "MID_INSTA": [957, 545],
        "EVENT_EXIT": [75, 80]
    }

    menu_paths = {
        "easy" : "pictures\\menus\\easy.png",
        "medium" : "pictures\\menus\\medium.png",
        "hard" : "pictures\\menus\\hard.png",
        "next" : "pictures\\menus\\next.png",
        "play" : "pictures\\menus\\play.png",
        "standard" : "pictures\\menus\\standard.png",
        "rightArrow" : "pictures\\menus\\rightArrow.png",
        "home" : "pictures\\menus\\home.png",
        "overwrite": "pictures\\menus\\overwrite.png",
        "begginer": "pictures\\menus\\begginer.png",
        "intermediate": "pictures\\menus\\intermediate.png",
        "advanced": "pictures\\menus\\advanced.png",
        "expert": "pictures\\menus\\expert.png"
    }

    event_images = {
        "collectEvent" : "pictures\\events\\4th_july\\colete.png",
        "levelUp" : "pictures\\levelup.png",
        "instaMonkey" : "pictures\\events\\insta_monkey.png"
    }

    default_images = {
        "victory" : "pictures\\victory.png",
        "defeat" : "pictures\\defeat.png",
        "playButton" : "pictures\\menus\\play.png",
        
        "obyn" : "pictures\\obyn.png",
        "next" : "pictures\\next.png",
        "startMenu" : "pictures\\start_button.png",

        "returnButton" : "pictures\\events\\return.png",
        "confirmHero" : "pictures\\heroes\\choose.png",
        "heroesMenu" : "pictures\\heroes\\heroes_menu.png"
    }

    monkeys = {
        "DART": "q",
        "BOOMERANG": "w",
        "BOMB": "e",
        "TACK": "r",
        "ICE": "t",
        "GLUE": "y",
        "SNIPER": "z",
        "SUBMARINE": "x",
        "BUCCANEER": "c",
        "ACE": "v",
        "HELI": "b",
        "MORTAR": "n",
        "DARTLING": "m",
        "WIZARD": "a",
        "SUPER": "s",
        "NINJA": "d",
        "ALCHEMIST": "f",
        "DRUID": "g",
        "BANANA": "h",
        "ENGINEER": "l",
        "SPIKE": "j",
        "VILLAGE": "k",
        "HERO": "u"
    }

    CONFIDENCE = 0.65

    def checkIfIsOnMenu(self):
        while True:
            menu_on = pyautogui.locateOnScreen(self.menu_paths["play"], grayscale=True, confidence=self.CONFIDENCE)
            if menu_on != None:
                print(f'{Fore.RED}Menu screen found. Continuing...')
                break
            else:
                print(f'{Fore.GREEN}Menu screen not found. Trying again...')
                sleep(2)

    def checkIfHeroIsSelected(self):
        if(pyautogui.locateOnScreen("pictures\\heroes\\" + self.heroName.lower() + "_picked.png", confidence = self.CONFIDENCE) == None):
            self.pickHero()

    def pickHero(self):
        findAndClick(self.default_images["heroesMenu"])
        sleep(0.5)
        findAndClick(self.heroLocation)
        sleep(0.5)
        findAndClick(self.default_images["confirmHero"])
        sleep(0.5)
        findAndClick(self.default_images["returnButton"])
        sleep(0.5)

    def goToMapSelection(self):
        findAndClick(self.menu_paths["play"])
        sleep(0.3)
        findAndClick(self.mapLevel)
        sleep(0.3)

    def selectMap(self):
        self.goToMapSelection()
        self.pickMap()
        self.finishSelection()

    def finishSelection(self):
        findAndClick(self.difficulty)
        sleep(0.5)
        findAndClick(self.menu_paths["standard"])
        sleep(0.5)
        isOverwrite = pyautogui.locateOnScreen(self.menu_paths["overwrite"])
        if(isOverwrite!=None):
            click(isOverwrite)
            sleep(0.5)

    def checkForEvents(self):
        event = pyautogui.locateOnScreen(self.default_positions["collectEvent"], confidence = self.CONFIDENCE)
        if(event != None):
            print("Event found!")
            pyautogui.click(event)
            sleep(3)
            insta_monkey = pyautogui.locateOnScreen(self.menu_paths["instaMonkey"], grayscale = True, confidence = self.CONFIDENCE)
            while(insta_monkey != None):
                pyautogui.click(insta_monkey)
                sleep(1)
                pyautogui.click(insta_monkey)
                sleep(1)
                insta_monkey = pyautogui.locateOnScreen(self.menu_paths["instaMonkey"], grayscale = True, confidence = self.CONFIDENCE)
            click(pyautogui.locateOnScreen(self.menu_paths["returnButton"], confidence = self.CONFIDENCE))
            sleep(3)

    def exit(self):
        Level_Up_Check(1)
        found = pyautogui.locateOnScreen(self.menu_paths["next"], grayscale=True, confidence=CONFIDENCE)

        while found == None:
            print('Next button not found.')
            found = pyautogui.locateOnScreen(self.menu_paths["next"], grayscale=True, confidence=CONFIDENCE)

        print(f'{Fore.CYAN}Game ended. Going back to homescreen...')
        click(found)
        sleep(2)
        back_btn = pyautogui.locateOnScreen(self.menu_paths["home"], grayscale = True, confidence = CONFIDENCE)
        click(back_btn)
        print(f'{Fore.CYAN}Back in homescreen. Checking for event notification...')
        sleep(2)

        reset_towers_levels()

        self.check_for_events()

    def check_for_events(self):
        event = pyautogui.locateOnScreen(self.event_images["collectEvent"], confidence = CONFIDENCE)
        if(event != None):
            print("Event found!")
            click(event)
            sleep(3)
            insta_monkey = pyautogui.locateOnScreen(self.event_images["instaMonkey"], grayscale = True, confidence = CONFIDENCE)
            while(insta_monkey != None):
                click(insta_monkey)
                sleep(1)
                click(insta_monkey)
                sleep(1)
                insta_monkey = pyautogui.locateOnScreen(self.event_images["instaMonkey"], grayscale = True, confidence = CONFIDENCE)
            sleep(3)
            click(pyautogui.locateOnScreen(self.default_images["returnButton"], confidence = CONFIDENCE))
            sleep(3)

    @abstractmethod
    def pickMap(self): # on map selection, pick the map
        pass

    @abstractmethod
    def startGame(self): # actual game script
        pass


    def start(self):
        self.checkIfHeroIsSelected()
        self.selectMap()
        self.startGame()
        self.exit()