from constants import *

import pydirectinput
import pyautogui
from time import sleep

def click(location):
    loc = button_positions[location]
    pyautogui.moveTo(loc)
    pyautogui.click(loc)
    sleep(0.2)

def move_mouse(location):
    pyautogui.moveTo(location)
    sleep(0.2)


def press_key(key):
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