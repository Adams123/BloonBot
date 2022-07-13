from constants import *
import gameutils as gutils

import pydirectinput
import pyautogui
from time import sleep

def dragTo(location, duration=0.2,shouldSleep=True):
    pyautogui.dragTo(location, duration=duration)
    if(shouldSleep):
        sleep(0.1)

def click(location):
    pyautogui.moveTo(location)
    sleep(0.3)
    gutils.levelUpCheck()
    pyautogui.click()
    sleep(0.2)

def move_mouse(location):
    pyautogui.moveTo(location)
    sleep(0.2)

def press_key(key):
    gutils.levelUpCheck()
    pydirectinput.press(key)
    sleep(0.2)

def scrollUp():
    subLoc = pyautogui.locateOnScreen("pictures\\monkeys\\SUBMARINE.png", confidence=CONFIDENCE)
    heroLoc = pyautogui.locateOnScreen("pictures\\monkeys\\HERO.png", confidence=CONFIDENCE)
    if subLoc == None or heroLoc == None:
        print("Não deu pra scrollUp")
        return
    sleep(0.2)
    pyautogui.moveTo(subLoc)
    sleep(0.2)
    pyautogui.dragTo(heroLoc, duration=0.2, tween=pyautogui.easeInOutQuad)
    sleep(0.2)

def scrollDown():
    mortar = pyautogui.locateOnScreen("pictures\\monkeys\\MORTAR.png", confidence=CONFIDENCE)
    engineer = pyautogui.locateOnScreen("pictures\\monkeys\\ENGINEER.png", confidence=CONFIDENCE)
    if mortar == None or engineer == None:
        print("Não deu pra scrollDown")
        return
    sleep(0.2)
    pyautogui.moveTo(mortar)
    sleep(0.2)
    pyautogui.dragTo(engineer, duration=0.2, tween=pyautogui.easeInOutQuad)
    sleep(0.2)