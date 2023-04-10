from enum import Enum
from typing import Optional

from classes import ClassNames
from race import RaceNames
from subrace import SubraceNames


class ProficiencyTypes(Enum):
    ARMOR = "armor"
    ARTISANS_TOOLS = "artisan's tools"
    WEAPONS = "weapons"


class ProficiencyNames(Enum):
    # Armor
    DWARVEN_ARMOR_TRAINING = "dwarven armor training"

    # Tools
    BREWERS_SUPPLIES = "brewer's supplies"
    MASONS_TOOLS = "mason's tools"
    SMITHS_TOOLS = "smith's tools"

    # Weapons
    BATTLEAXE = "battleaxe"
    HANDAXE = "handaxe"
    LIGHT_HAMMER = "light hammer"
    WARHAMMER = "warhammer"


AllProficiencies = {
    # Armor
    [ProficiencyNames.DWARVEN_ARMOR_TRAINING]: {
        "name": ProficiencyNames.DWARVEN_ARMOR_TRAINING,
        "dnd_type": ProficiencyTypes.ARMOR,
        "classes": [],
        "races": [],
        "subraces": [],
    },
    # Artisan's Tools
    [ProficiencyNames.SMITHS_TOOLS]: {
        "name": ProficiencyNames.SMITHS_TOOLS,
        "dnd_type": ProficiencyTypes.ARTISANS_TOOLS,
        "classes": [],
        "races": [],
        "subraces": [],
    },
    [ProficiencyNames.BREWERS_SUPPLIES]: {
        "name": ProficiencyNames.BREWERS_SUPPLIES,
        "dnd_type": ProficiencyTypes.ARTISANS_TOOLS,
        "classes": [],
        "races": [],
        "subraces": [],
    },
    [ProficiencyNames.MASONS_TOOLS]: {
        "name": ProficiencyNames.MASONS_TOOLS,
        "dnd_type": ProficiencyTypes.ARTISANS_TOOLS,
        "classes": [],
        "races": [],
        "subraces": [],
    },
    # Weapons
    [ProficiencyNames.BATTLEAXE]: {
        "name": ProficiencyNames.BATTLEAXE,
        "dnd_type": ProficiencyTypes.WEAPONS,
        "classes": [],
        "races": [RaceNames.DWARF],
        "subraces": [],
    },
    [ProficiencyNames.HANDAXE]: {
        "name": ProficiencyNames.HANDAXE,
        "dnd_type": ProficiencyTypes.WEAPONS,
        "classes": [],
        "races": [RaceNames.DWARF],
        "subraces": [],
    },
    [ProficiencyNames.LIGHT_HAMMER]: {
        "name": ProficiencyNames.LIGHT_HAMMER,
        "dnd_type": ProficiencyTypes.WEAPONS,
        "classes": [],
        "races": [RaceNames.DWARF],
        "subraces": [],
    },
    [ProficiencyNames.WARHAMMER]: {
        "name": ProficiencyNames.WARHAMMER,
        "dnd_type": ProficiencyTypes.WEAPONS,
        "classes": [],
        "races": [RaceNames.DWARF],
        "subraces": [],
    },
}


class Proficiency:
    def __init__(self, name: ProficiencyNames):
        proficiency = AllProficiencies[name]
        self._name = proficiency["name"]
        self._dnd_type = proficiency["dnd_type"]
        self._classes = proficiency["classes"]
        self._races = proficiency["races"]
        self._subraces = proficiency["subraces"]

    @property
    def name(self) -> AllProficiencies:
        return self._name

    @property
    def dnd_type(self) -> ProficiencyTypes:
        return self._dnd_type

    @property
    def classes(self) -> Optional[ClassNames]:
        return self._classes

    @property
    def races(self) -> Optional[RaceNames]:
        return self._races

    @property
    def subraces(self) -> Optional[SubraceNames]:
        return self._subraces
