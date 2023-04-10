from enum import Enum
from abc import ABC, abstractmethod
from typing import List, Optional
from classes import DndClass
from race import Race
from ability import Ability


class Character(object):
    def __init__(self, race: Race, dnd_class: DndClass, abilities: List[Ability]):
        self.race = race
        # self.dnd_class = dnd_class
        # self.abilities = abilities
        # self.profile = profile
        # self.background = background

    pass
