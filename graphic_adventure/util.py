import time
from const import *
import pygame
from soundEffects import *


inventory = []


def print_slow(str, speed = 0.03):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(speed)
    print()

def inputAction(options):
    while True:
        choice = input("What will you do next: ").lower()
        if choice in options:
            return choice
        elif choice == "inventory":
            print_slow("You check you inventory.")
            print(inventory)
        else:
            print("... nothing happens ...")

def pickItem(itemName, soundEffect, soundEffectDuration):
    play_sound(soundEffect, soundEffectDuration)
    print_slow("You take a " + itemName + " and save it in your inventory.")

    global inventory
    inventory.append(itemName)

def roomEntry (roomName, roomGraphics, message = "You enter the ", soundEffect = DOOR, soundEffectDuration = 6):
    print_slow(message + roomName + ".")
    play_sound(soundEffect, soundEffectDuration)
    print_slow(roomGraphics, 0.02)

def getNextRoom(direction,x,y):
    if(direction==RIGHT):
        x+=1
        print_slow("You chose to go right.")
    if(direction==LEFT):
        x-=1
        print_slow("You chose to go left.")
    if(direction==BACK):
        y+=1
        print_slow("You chose to go back.")
    if(direction==FORWARD):
        y-=1
        print_slow("You chose to go forward.")
    play_sound(STEPS_CONCRETE)

    nextRoom = getRoom(x,y)
    return nextRoom, (x,y)

def getRoom(x,y):
    room = MAP[y][x]
    return room

def play_sound(sound_file, duration=3):
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    time.sleep(duration)
    sound.stop()

def play_ost():
    pygame.mixer.init()
    pygame.mixer.music.load(SPOOKY_AMBIENT)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

