DIRECTIONS = ['right', 'left', 'back', 'forward']
CURRENT_ROOM_COORDINATES = (1,3)

MAP = [
    ['',            '',                 'attic',                'library'],
    ['wardrobe',    'room',             'corridor',             'office'],
    ['bathroom',    'living room',      'upstairs',             'secret passage'],
    ['kitchen',     'hall',             'garage',               'yard'],
    ['pantry',      '',                 'cursed crypt',         'botton of the well']
]

LEFT = "left"
RIGHT = "right"
BACK = "back"
FORWARD = "forward"

KITCHEN_ACTIONS = [RIGHT, "bar", "table", "fridge"]
TABLE_ACTIONS = [RIGHT, "bar", "table", "fridge", "knife"]
GARAGE_ACTIONS = [RIGHT, LEFT, "car", "rack", "box"]
YARD_ACTIONS = [LEFT, "tree", "branch", "grave", "well"]


