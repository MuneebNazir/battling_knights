# game/settings.py

# Board dimensions
BOARD_SIZE = 8

# Initial positions of knights
KNIGHT_POSITIONS = {
    'R': (0, 0),
    'B': (7, 0),
    'G': (7, 7),
    'Y': (0, 7)
}

# Initial positions of items
ITEM_POSITIONS = {
    'A': (2, 2),
    'D': (2, 5),
    'M': (5, 2),
    'H': (5, 5)
}

# Item bonuses
ITEM_BONUSES = {
    'A': {'attack': 2, 'defense': 0},
    'M': {'attack': 1, 'defense': 1},
    'D': {'attack': 1, 'defense': 0},
    'H': {'attack': 0, 'defense': 1}
}

# Movement directions
DIRECTIONS = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}
