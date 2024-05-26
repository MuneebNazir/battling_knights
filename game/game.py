# game/game.py

import json
from .settings import KNIGHT_POSITIONS, ITEM_POSITIONS, DIRECTIONS
from .knight import Knight
from .item import Item

class Game:
    def __init__(self):
        self.knights = {
            color: Knight(color, pos) for color, pos in KNIGHT_POSITIONS.items()
        }
        self.items = {
            type: Item(type, pos) for type, pos in ITEM_POSITIONS.items()
        }

    def move_knight(self, color, direction):
        knight = self.knights[color]
        if knight.status != "LIVE":
            return

        previous_position = knight.position
        knight.move(DIRECTIONS[direction])

        if knight.status == "LIVE":
            self.handle_item_pickup(knight)
            self.handle_battles(knight, previous_position)

    def handle_item_pickup(self, knight):
        items_on_tile = [
            item for item in self.items.values() if item.position == knight.position and not item.equipped
        ]

        if items_on_tile:
            best_item = self.get_best_item(items_on_tile)
            knight.equip_item(best_item)

    def get_best_item(self, items):
        priority = ['A', 'M', 'D', 'H']
        items.sort(key=lambda item: priority.index(item.type))
        return items[0]

    def handle_battles(self, knight, previous_position):
        for other_knight in self.knights.values():
            if other_knight != knight and other_knight.position == knight.position:
                knight.fight(other_knight)

    def get_final_state(self):
        knight_names = {
            "R": "red",
            "B": "blue",
            "G": "green",
            "Y": "yellow"
        }

        item_names = {
            "M": "magic_staff",
            "H": "helmet",
            "D": "dagger",
            "A": "axe"
        }
      
        final_state = {}
        for color, knight in self.knights.items():
            final_state[knight_names[color]] = [
                knight.position,
                knight.status,
                knight.item.type if knight.item else None,
                knight.attack_power(),
                knight.defense_power()
            ]
        for type, item in self.items.items():
            final_state[item_names[type]] = [item.position, item.equipped]
        return final_state

    def run_game(self, moves_file):
        with open(moves_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line == "GAME-START" or line == "GAME-END":
                    continue
                color, direction = line.split(':')
                self.move_knight(color, direction)

    def save_final_state(self, output_file):
        final_state = self.get_final_state()
        with open(output_file, 'w') as file:
            json.dump(final_state, file, indent=4)
