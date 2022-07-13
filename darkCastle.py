from MapClass import Map
from gameutils import *
from mouseUtils import click, press_key

class DarkCastle(Map):

    def __init__(self):
        super().__init__("DARK_CASTLE", "OBYN", self.locations, difficulty="easy", mapLevel="expert")

    locations = {
        "MAP_LOCATION": [960, 260],
        
        "HERO_LOCATION": [712, 431],
        "BOMBER_TARGET": [698,555],
        "SUBMARINE_LOCATION": [1090, 431],
        "NINJA_LOCATION": [553, 633]
    }

    levelup_locations = [[570,483]]


    def pickMap(self): # on map selection, pick the map
        click(super().menu_paths["rightArrow"])
        sleep(0.5)
        click(self.locations["MAP_LOCATION"])
        sleep(0.5)

    def startGame(self):
        place_tower("HERO", self.locations["HERO_LOCATION"])
        
        press_key("space")
        press_key("space")

        place_tower("SUBMARINE", self.locations["SUBMARINE_LOCATION"])
        keepUpgrading([',','/','/',','], "SUBMARINE_1", self.locations["SUBMARINE_LOCATION"])
        
        place_tower("NINJA", self.locations["NINJA_LOCATION"])
        keepUpgrading([',',',','/',','], "NINJA_1", self.locations["NINJA_LOCATION"])

        keepUpgrading(['/','/'], "SUBMARINE_1", self.locations["SUBMARINE_LOCATION"])
        upgrade_tower(',', "NINJA_1", self.locations["NINJA_LOCATION"])

        levelup_tower("BOOMERANG", self.levelup_locations)
        
        

darkCastle = DarkCastle()
sleep(3)
x = 0
while( x < 10 ):
    darkCastle.start()