from enum import Enum
from typing import List, Optional
from race import Race, RaceNames
from subrace import SubraceNames
from proficiency import Proficiency, ProficiencyNames


class TraitNames(Enum):
    DARVISION = "darvision"
    DWARVEN_RESILIENCE = "dwarven resilience"
    STONECUNNING = "stonecunning"
    DWARVEN_COMBAT_TRAINING = "dwarven combat training"
    TOOL_PROFICIENCY = "tool proficiency"
    DWARVEN_TOUGHNESS = "dwarven toughness"


AllTraits = {
    [TraitNames.DARVISION]: {
        "name": TraitNames.DARVISION,
        "races": [
            RaceNames.DWARF,
            RaceNames.ELF,
            RaceNames.GNOME,
            RaceNames.HALF_ELF,
            RaceNames.HALF_ORC,
            RaceNames.TIEFLING,
        ],
        "subraces": [],
        "description": "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.",
        # Potential field
        "short_description": "",
        "proficiencies": [],
        "proficiency_options": [],
    },
    [TraitNames.DWARVEN_RESILIENCE]: {
        "name": TraitNames.DWARVEN_RESILIENCE,
        "races": [RaceNames.DWARF],
        "subraces": [],
        "description": "You have advantage on saving throws against poison, and you have resistance against poison damage.",
        # Potential field
        "short_description": "",
        "proficiencies": [],
        "proficiency_options": [],
    },
    [TraitNames.DWARVEN_TOUGHNESS]: {
        "name": TraitNames.DWARVEN_TOUGHNESS,
        "races": [],
        "subraces": [SubraceNames.HILL_DWARF],
        # TODO: find a way to integrate this to automatically add this to your character
        "description": "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level",
        # Potential field
        "short_description": "",
        "proficiencies": [],
        "proficiency_options": [],
    },
    [TraitNames.STONECUNNING]: {
        "name": TraitNames.STONECUNNING,
        "races": [RaceNames.DWARF],
        "subraces": [],
        "description": "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.",
        # Potential field
        "short_description": "",
        "proficiencies": [],
        "proficiency_options": [],
    },
    [TraitNames.DWARVEN_COMBAT_TRAINING]: {
        "name": TraitNames.DWARVEN_COMBAT_TRAINING,
        "races": [RaceNames.DWARF],
        "subraces": [],
        "description": "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.",
        # Potential field
        "short_description": "",
        "proficiencies": [
            ProficiencyNames.BATTLEAXE,
            ProficiencyNames.HANDAXE,
            ProficiencyNames.LIGHT_HAMMER,
            ProficiencyNames.WARHAMMER,
        ],
        "proficiency_options": [],
    },
    [TraitNames.TOOL_PROFICIENCY]: {
        "name": TraitNames.TOOL_PROFICIENCY,
        "races": [RaceNames.DWARF],
        "subraces": [],
        "description": "You gain proficiency with the artisan’s tools of your choice: smith’s tools, brewer’s supplies, or mason’s tools.",
        # Potential field
        "short_description": "",
        "proficiencies": [],
        "proficiency_options": [
            ProficiencyNames.SMITHS_TOOLS,
            ProficiencyNames.BREWERS_SUPPLIES,
            ProficiencyNames.MASONS_TOOLS,
        ],
    },
}


class Trait:
    def __init__(self, name: TraitNames):
        trait = AllTraits[name]
        self._name = trait["name"]
        self._races = trait["races"]
        self._subraces = trait["subraces"]
        self._description = trait["description"]
        self._proficiencies = trait["proficiencies"]
        self._proficiency_options = trait["proficiency_options"]

    @property
    def name(self) -> TraitNames:
        return self._name

    @property
    def races(self) -> Optional[List[RaceNames]]:
        return self._races

    @property
    def subraces(self) -> Optional[List[SubraceNames]]:
        return self._subraces

    @property
    def description(self) -> str:
        return self._description

    @property
    def proficiencies(self) -> Optional[List[ProficiencyNames]]:
        return self._proficiencies

    @property
    def proficiency_options(self) -> Optional[List[ProficiencyNames]]:
        return self._proficiency_options
