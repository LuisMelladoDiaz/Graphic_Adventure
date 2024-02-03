from const import *
from graphics import *
from soundEffects import *
from util import *


def hall_room():
    print_slow("You are in the hause hall.")
    print_slow("It so dark you cannot see.")
    print_slow("You feel that there is a door to your left and another to your right")

    performAction(DIRECTIONS)

def kitchen():
    roomEntry("kitchen", KITCHEN)
    performAction(KITCHEN_ACTIONS)

def bar():
    print_slow("You get closer to the bar.")
    play_sound(STEPS_CONCRETE, 4)
    print_slow("The sink is leaking.")
    play_sound(LEAKING, 5)

    performAction(TABLE_ACTIONS)

def table():
    print_slow("You get closer to the table.")
    play_sound(STEPS_CONCRETE, 4)
    print_slow("It seems that the table was set for a great dinner.")
    print_slow("A complete set of cutlery lies beside each empty plate.")

    global inventory
    if ("knife" in inventory): performAction(KITCHEN_ACTIONS)
    else: performAction(TABLE_ACTIONS)

def fridge():
    print_slow("You open the fridge.")
    print_slow("It is full of rotten food.")
    play_sound(FLY, 6)
    print_slow("You would never put your hand in a swarm of flies.")

    performAction(KITCHEN_ACTIONS)

def knife():
    pickItem("knife", KNIFE, 1)
    performAction(KITCHEN_ACTIONS)

## GARAGE
def garage():
    roomEntry("garage", GARAGE)
    performAction(GARAGE_ACTIONS)

def car():
    print_slow("It is an old car.")
    performAction(GARAGE_ACTIONS)
def box():
    print_slow("It is a tool box covered in dust.")
    print_slow("a sharp object like a knife could help here")
    performAction(GARAGE_ACTIONS)

def rack():
    print_slow("The shelf is very messy.")
    print_slow("There are chemicals products everywhere. From car oil to insecticide.")
    performAction(GARAGE_ACTIONS)


## YARD
def back_yard():
    roomEntry("backyard", BACK_YARD, message="You go out to")
    performAction(DIRECTIONS)

def grave(): pass
def tree(): pass
def well(): pass
def branch(): pass


def go(direction):

    global CURRENT_ROOM_COORDINATES
    position = CURRENT_ROOM_COORDINATES
    nextRoom, CURRENT_ROOM_COORDINATES = getNextRoom(direction, position[0], position[1])
    actionDictionary[nextRoom]()

def performAction(actionList):
    action = inputAction(actionList)
    if action in DIRECTIONS:
        go(action)
    else:
        actionDictionary[action]()

actionDictionary = {
## ROOMS
    "kitchen": kitchen,
    "garage": garage,
    "hall": hall_room,
    "yard": back_yard,
## KITCHEN
    "bar": bar,
    "table": table,
    "knife": knife,
    "fridge": fridge,
## GARAGE
    "car": car,
    "rack": rack,
    "box": box,
## YARD
    "grave": grave,
    "tree": tree,
    "branch": branch,
    "well": well
}

