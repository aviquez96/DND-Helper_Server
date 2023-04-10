from enum import Enum
from typing import List, Optional
from ability import Ability, AbilityTypes
from trait import Trait, TraitNames
from race import RaceNames
from proficiency import Proficiency, ProficiencyNames
from constants import LanguageNames


class SubraceNames(Enum):
    HILL_DWARF = "hill dwarf"
    MOUNTAIN_DWARF = "mountain dwarf"


AllSubraces = {
    [SubraceNames.HILL_DWARF]: {
        "name": SubraceNames.HILL_DWARF,
        "race": [RaceNames.DWARF],
        "description": "As a hill dwarf, you have keen senses, deep intuition, and remarkable resilience.",
        "ability_bonuses": [Ability(name=AbilityTypes.WISDOM, bonus=1)],
        "proficiencies": [],
        "proficiency_options": [],
        "traits": [Trait(TraitNames.DWARVEN_TOUGHNESS)],
        "trait_options": [],
        "languages": [],
        "language_options": [],
    },
    [SubraceNames.MOUNTAIN_DWARF]: {
        "name": SubraceNames.MOUNTAIN_DWARF,
        "race": [RaceNames.DWARF],
        "description": "As a mountain dwarf, you’re strong and hardy, accustomed to a difficult life in rugged terrain. You’re probably on the tall side (for a dwarf), and tend toward lighter coloration.",
        "ability_bonuses": [Ability(name=AbilityTypes.STRENGTH, bonus=2)],
        "proficiencies": [Proficiency(ProficiencyNames)],
        "proficiency_options": [],
        "traits": [],
        "trait_options": [],
        "languages": [],
        "language_options": [],
    },
}


class Subrace:
    def __init__(self, name: SubraceNames):
        trait = AllSubraces[name]
        self._name = trait["name"]
        self._race = trait["race"]
        self._description = trait["description"]
        self._ability_bonuses = trait["ability_bonuses"]
        self._proficiencies = trait["proficiencies"]
        self._proficiencies_options = trait["proficiencies_options"]
        self._traits = trait["traits"]
        self._trait_options = trait["trait_options"]
        self._languages = trait["languages"]
        self._language_options = trait["language_options"]

    @property
    def name(self) -> SubraceNames:
        return self._name

    @property
    def race(self) -> RaceNames:
        return self._race

    @property
    def description(self) -> str:
        return self._description

    @property
    def ability_bonuses(self) -> Optional[List[Ability]]:
        return self._ability_bonuses

    @property
    def proficiencies(self) -> Optional[List[ProficiencyNames]]:
        return self._proficiencies

    @property
    def proficiency_options(self) -> Optional[List[ProficiencyNames]]:
        return self._proficiency_options

    @property
    def traits(self) -> Optional[List[TraitNames]]:
        return self._traits

    @property
    def trait_options(self) -> Optional[List[TraitNames]]:
        return self._trait_options

    @property
    def languages(self) -> Optional[List[LanguageNames]]:
        return self._languages

    @property
    def language_options(self) -> Optional[List[LanguageNames]]:
        return self._language_options
