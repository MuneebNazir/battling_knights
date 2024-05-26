# game/knight.py

from .settings import ITEM_BONUSES

class Knight:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.status = "LIVE"
        self.item = None
        self.base_attack = 1
        self.base_defense = 1

    def move(self, direction):
        if self.status != "LIVE":
            return
        dx, dy = direction
        x, y = self.position
        new_position = (x + dx, y + dy)
        if self.is_valid_position(new_position):
            self.position = new_position
            if self.item:
                self.item.position = new_position
        else:
            self.drown()

    def is_valid_position(self, position):
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8

    def drown(self):
        self.status = "DROWNED"
        if self.item:
            self.item.position = self.position
            self.item.equipped = False
        self.position = None
        self.item = None

    def equip_item(self, item):
        if self.status == "LIVE" and self.item is None:
            self.item = item
            item.equipped = True
            item.position = self.position

    def drop_item(self):
        if self.item:
            item = self.item
            item.position = self.position
            item.equipped = False
            self.item = None
            return item
        return None

    def attack_power(self):
        if self.status != "LIVE":
            return 0
        return self.base_attack + (ITEM_BONUSES[self.item.type]['attack'] if self.item else 0)

    def defense_power(self):
        if self.status != "LIVE":
            return 0
        return self.base_defense + (ITEM_BONUSES[self.item.type]['defense'] if self.item else 0)

    def fight(self, defender):
        if self.status != "LIVE" or defender.status != "LIVE":
            return
        attacker_power = self.attack_power() + 0.5
        defender_power = defender.defense_power()
        if attacker_power > defender_power:
            defender.status = "DEAD"
            defender.drop_item()
        else:
            self.status = "DEAD"
            self.drop_item()
