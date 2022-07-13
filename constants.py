import os
import pathlib

CONFIDENCE = 0.65
overtime = 0

level_up_path = "pictures\\events\\levelup\\levelup.png"
monkey_knowledge_path = "pictures\\events\\levelup\\knowledge.png"
victory_path = "pictures\\victory.png"
defeat_path = "pictures\\defeat.png"
menu_path = "pictures\\menu.png"
event_path = "pictures\\events\\4th_july\\colete.png"
obyn_hero_path = "pictures\\obyn.png"
next_path = "pictures\\menus\\next.png"
start_menu_path = "pictures\\start_button.png"

insta_monkey_path = "pictures\\events\\insta_monkey.png"
return_button_path = "pictures\\events\\return.png"



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

button_positions = {}

default_positions = {
    "HOME_MENU_START": [842, 936],
    "EXPERT_SELECTION": [1333, 978],
    "RIGHT_ARROW_SELECTION": [1644, 436],
    "EASY_MODE": [629, 413],
    "STANDARD_GAME_MODE": [635, 585],
    "OVERWRITE_SAVE": [1140, 730],
    "LEFT_INSTA": [805, 544],
    "RIGHT_INSTA": [1109, 543],
    "MID_INSTA": [957, 545],
    "EVENT_EXIT": [75, 80]
}

dark_castle = {
    "MAP_LOCATION": [960, 260],
    "DIFFICULTY": [629, 413],
    
    "HERO_LOCATION": [712, 431],
    "BOMBER_TARGET": [698,555],
    "SUBMARINE_LOCATION": [1090, 431],
    "NINJA_LOCATION": [553, 633]
}

infernal_hard = {
    "MAP_LOCATION": [549, 557],
    "DIFFICULTY": [629, 413],

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

levelup_locations = [[570,483],[496,467],[541,411],[465,397],[524,339],[410,351],
[504,274],[430,246],[412,106],[495,103],[572,128],[628,174]]

selected_map_config = {
    "INFERNAL_HARD": [infernal_hard, None, "QUINCY"],
    "DARK_CASTLE":[dark_castle, levelup_locations, "OBYN"]
}