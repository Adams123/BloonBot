from MapClass import Map
from gameutils import *
from mouseUtils import click, press_key

class Infernal(Map):

    def __init__(self):
        super().__init__("INFERNAL", "QUINCY", self.locations, difficulty="hard", mapLevel="expert")

    locations = {
        "MAP_LOCATION": [549, 557],

        "HERO_LOCATION" : [838,383],
        "NINJA_LOCATION": [836,695],
        "SUBMARINE_LOCATION_1": [1155,218],
        "SUBMARINE_LOCATION_2": [1231,185],
        "SUBMARINE_LOCATION_3": [469,879],
        "SUBMARINE_LOCATION_4": [1221,258],
        "ALCHEMIST_LOCATION": [838,755],
        "ACE_LOCATION": [1579,513],
        "VILLAGE_LOCATION": [1581,608],
        "BUCCANEER_LOCATION": [499,792],
        "SNIPER_LOCATION": [1605,697]
    }


    def pickMap(self): # on map selection, pick the map
        click(self.locations["MAP_LOCATION"])
        sleep(0.5)

    def startGame(self): # actual game script
        place_tower("HERO", self.locations["HERO_LOCATION"])
    
        press_key("space")  # Start the game
        press_key("space")  # Fast forward the game

        place_tower("NINJA", "NINJA_LOCATION")
        keepUpgrading([',','/',',',','], "NINJA_1", self.locations["NINJA_LOCATION"])

        place_tower("SUBMARINE", "SUBMARINE_LOCATION_1")
        keepUpgrading([",",",",".","."], "SUBMARINE_1", self.locations["SUBMARINE_LOCATION_1"])
        
        place_tower("SUBMARINE", self.locations["SUBMARINE_LOCATION_2"])
        keepUpgrading([",",",","/","/","/","/"], "SUBMARINE_2", self.locations["SUBMARINE_LOCATION_2"])
        
        keepUpgrading([',','/'], "NINJA_1", self.locations["NINJA_LOCATION"])
        
        place_tower("ALCHEMIST", self.locations["ALCHEMIST_LOCATION"])
        keepUpgrading([',',',',',','.','.',','], "ALCHEMIST_1", self.locations["ALCHEMIST_LOCATION"])
        
        place_tower("ACE", self.locations["ACE_LOCATION"])
        keepUpgrading(['/','/',',',',','/'], "ACE_1", self.locations["ACE_LOCATION"])
        
        place_tower("VILLAGE", self.locations["VILLAGE_LOCATION"])
        keepUpgrading(['.','.','/','/'], "VILLAGE_1", self.locations["VILLAGE_LOCATION"])
        
        sell_tower("ALCHEMIST_LOCATION")
        upgrade_tower('/', "ACE_1", self.locations["ACE_LOCATION"])
        place_tower("ALCHEMIST", self.locations["ALCHEMIST_LOCATION"])
        keepUpgrading([',',',',',','.','.',','], "ALCHEMIST_2", self.locations["ALCHEMIST_LOCATION"])

        place_tower("BUCCANEER","BUCCANEER_LOCATION")
        keepUpgrading([',',',','.','.',',',','], "BUCCANEER_1",self.locations["BUCCANEER_LOCATION"])
        
        place_tower("SUBMARINE", self.locations["SUBMARINE_LOCATION_3"])
        keepUpgrading([",",",","/","/","/","/"], "SUBMARINE_3", self.locations["SUBMARINE_LOCATION_3"])
        
        upgrade_tower('.', "SUBMARINE_1", self.locations["SUBMARINE_LOCATION_1"])

        place_tower("SUBMARINE", self.locations["SUBMARINE_LOCATION_4"])
        keepUpgrading([",",",","/","/","/","/"], "SUBMARINE_4", self.locations["SUBMARINE_LOCATION_4"])

        place_tower("SNIPER", self.locations["SNIPER_LOCATION"])
        keepUpgrading([",",",",",","/","/"], "SNIPER_1", self.locations["SNIPER_LOCATION"])
        

infernal = Infernal()
sleep(3)
Infernal.startGame()