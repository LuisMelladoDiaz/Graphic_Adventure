from util import *
from room import *
import os


def start_game():
    os.system("cls" if os.name == "nt" else "clear")
    print_slow("You find yourself in a dark and mysterious mansion.")

if __name__ == "__main__":
    play_ost()
    start_game()
    hall_room()
