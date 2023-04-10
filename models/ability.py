from enum import Enum
from math import floor


class AbilityTypes(Enum):
    STRENGTH = "strength"
    DEXTERITY = "dexterity"
    CONSITUTION = "constitution"
    INTELLIGENCE = "intelligence"
    WISDOM = "wisdom"
    CHARISMA = "charisma"


class Ability(object):
    def __init__(self, name: AbilityTypes, score: int = 0, bonus: int = 0):
        self.name = name
        self.score = score
        self.bonus = bonus

    @property
    def _modifier(self):
        return floor((self.score - 10) / 2)
