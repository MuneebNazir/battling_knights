# game/item.py

class Item:
    def __init__(self, type, position):
        self.type = type
        self.position = position
        self.equipped = False
