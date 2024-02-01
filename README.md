# Graphic_Adventure
Puzzle oriented graphic adventure.
You are trapped in a misterious dark mansion and have to find your way out.

## Installation
This game requires Pygame. Make sure to install it before running the game.
- pip install pygame
Run main.py to start playing/testing.

### main.py
Just initialize the game
### util.py
Functions in charge of:
  - Sound effects
  - Choice system
  - Moving from/to rooms
  - Text printing
### room.py
Functions that describe what is and what can be done in each room

## const.py
- Constant that will be used globally
- Set of actions the player can do in each room
- Graphics of the rooms (migh be moved to a different file in the future graphics.py)
- Sound effects routes (migh be moved to a different file in the future sound.py)

### sound
- Contain the sound effect files .wav

## How to play
At this point the game is pretty basic. You can move around writting 'right' or 'lef't and explore the rooms by writting the name of the element you want to inspect.
Every action you can do is described with a single word, that is: 'right' is OK, 'move right' is WRONG.
All action words that can be performed in a room are shown in the screen or hinted in another place (there might be secret actions in a room). But the game will always show what the command word is somewhere.


