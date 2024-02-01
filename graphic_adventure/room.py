from const import *
from util import *


def hall_room():
    print_slow("You are in the hause hall.")
    print_slow("It so dark you cannot see.")
    print_slow("You feel that there is a door to your left and another to your right")

    action = choice(DIRECTIONS)
    performAction(action)

def kitchen():
    print_slow("You enter the kitchen.")
    play_sound(DOOR, 6)
    print_slow(KITCHEN, 0.02)

    action = choice(KITCHEN_ACTIONS)
    performAction(action)

def bar():
    print_slow("You get closer to the bar.")
    play_sound(STEPS_CONCRETE, 4)
    print_slow("The sink is leaking.")
    play_sound(LEAKING, 5)
    action = choice(TABLE_ACTIONS)
    performAction(action)

def table():
    print_slow("You get closer to the table.")
    play_sound(STEPS_CONCRETE, 4)
    print_slow("It seems that the table was set for a great dinner.")
    print_slow("A complete set of cutlery lies beside each empty plate.")

    global inventory
    if ("knife" in inventory): action = choice(KITCHEN_ACTIONS)
    else: action = choice(TABLE_ACTIONS)

    performAction(action)

def fridge():
    print_slow("You open the fridge.")
    print_slow("It is full of rotten food.")
    play_sound(FLY, 6)
    print_slow("You would never put your hand in a swarm of flies.")

    action = choice(KITCHEN_ACTIONS)
    performAction(action)

def knife():
    play_sound(KNIFE,1)
    print_slow("You take a knife and save it in your inventory.")

    global inventory
    inventory.append("knife")

    action = choice(KITCHEN_ACTIONS)
    performAction(action)


def garage():
    print_slow("You enter the garage.")
    play_sound(DOOR, 6)
    print_slow(GARAGE, 0.02)

    action = choice(DIRECTIONS)
    performAction(action)

def back_yard():
    print_slow("You go out to the backyard.")
    play_sound(DOOR, 6)
    print_slow(BACK_YARD, 0.02)

    action = choice(DIRECTIONS)
    performAction(action)


def go(direction):

    global CURRENT_ROOM_COORDINATES
    position = CURRENT_ROOM_COORDINATES
    nextRoom, CURRENT_ROOM_COORDINATES = getNextRoom(direction, position[0], position[1])

    if (nextRoom == 'kitchen'): kitchen()
    if (nextRoom == 'garage'): garage()
    if (nextRoom == 'hall'): hall_room()
    if (nextRoom == 'yard'): back_yard()

def performAction(action):
    if action in DIRECTIONS:
        go(action)
    else:
        if (action == "bar"): bar()
        if (action == "table"): table()
        if (action == "knife"): knife()
        if (action == "fridge"): fridge()



