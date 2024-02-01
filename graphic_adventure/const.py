from tkinter import LEFT


DIRECTIONS = ['right', 'left', 'back', 'forward']
CURRENT_ROOM_COORDINATES = (1,3)

MAP = [
    ['',            '',                 'attic',                'library'],
    ['wardrobe',    'room',             'corridor',             'office'],
    ['bathroom',    'living room',      'upstairs',             'secret passage'],
    ['kitchen',     'hall',             'garage',               'yard'],
    ['pantry',      '',                 'cursed crypt',         'botton of the well']
]

STEPS_CONCRETE = "sound\\footsteps_concrete.wav"
DOOR = "sound\\doorShut.wav"
SPOOKY_AMBIENT = "sound\\spooky.wav"
KNIFE = "sound\\knife.wav"
LEAKING = "sound\\leaking.wav"
FLY = "sound\\fly.wav"

LEFT = "left"
RIGHT = "right"
BACK = "back"
FORWARD = "forward"

KITCHEN = """
+---------------------+
|   ________________  |
|  |        ___    |  |
|  |________| |    |  |
|  |_Bar______|    |  |
|  |  _______      |  |
|  | |       |     |  |
|  | |       |     |  |
|  | | Table |     |  |
|  | |       |     |  |
|  | |       |     |  |
|  | |_______|         --> Right
|  |
|  |      ________ |  |
|  |     | Fridge ||  |
+---####--------------+
    | Down
    ▼
"""

GARAGE = """
        +---------------------------+
        |   ________________________
        |  |   _____                |
        |  |   |___|Rack             --> Right
        |  |   |___|
        |  |  _|   |_               |
        |  |                        |
        |  |         _______        |
        |  |    ___//___||__\____   |
        |  |   |_( )___Car__( )__|  |
        |  |                        |
        |  |                        |
<-- Left                       /\   |
                              ▓▓▓▓  |
        |  |              Tool Box  |
        +---------------------------+
"""

BACK_YARD = """
        +--------------------------------------+
        |                                       |
<-- Left                            v~~~~~~~    |
                    {{}}}}}}.                   |
        |         {{(`)}}}}}}}}                 |
        |       {{(`)}}}}}}}{}}}}               |
        |       {{(`)}Tree}}{}}}}               |
        |      {{{{{{{(`)}}}}}}}}}              |
        |       {{{{(`)   {{{{(`)   _____       |
        |       `""'" |   | "'"'`  /  +  \      |
        |            /     \       |Grave|      |
        |        ~~v~~~~~~~~~~~~~~~|_____|vv~~  |
        |  ~~~~                                 |
        |  ________         ~~vv~~v~~           |
        | |  Well  |                            |
        | |________|                      vvv   |
        +---------------------------------------+
"""

LIVING_ROOM = """
+---------------------+
|   ________________
|  |
|  |
|  |
|  |   _____
|  | __|___|__
|  | |       |
|  |
|  |


|  |
+---####--------------+
"""

KITCHEN_ACTIONS = [RIGHT, "bar", "table", "fridge"]
TABLE_ACTIONS = [RIGHT, "bar", "table", "fridge", "knife"]
