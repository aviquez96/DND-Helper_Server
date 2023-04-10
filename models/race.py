from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from ability import Ability, AbilityTypes
from constants import LanguageNames, SizeOptions
from proficiency import Proficiency, ProficiencyNames
from subrace import Subrace, SubraceNames
from trait import Trait, TraitNames


# Add all of them
class RaceNames(Enum):
    HUMAN = "human"
    VARIANT_HUMAN = "variant_human"
    DWARF = "dwarf"
    ELF = "elf"
    GNOME = "gnome"
    HALF_ELF = "half elf"
    HALF_ORC = "half orc"
    TIEFLING = "tiefling"


class AlignmentOptions(Enum):
    CHAOTIC_EVIL = "chaotic_evil"
    CHAOTIC_NEUTRAL = "chaotic_neutral"
    CHAOTIC_GOOD = "chaotic_good"
    NEUTRAL_EVIL = "neutral_evil"
    TRUE_NEUTRAL = "true_neutral"
    NEUTRAL_GOOD = "neutral_good"
    LAWFUL_EVIL = "lawful_evil"
    LAWFUL_NEUTRAL = "lawful_neutral"
    LAWFUL_GOOD = "lawful_good"
    UNALIGNED = "unaligned"


# @dataclass
# class RaceProficiencies:
#     source: str
#     list: List[Proficiency]


@dataclass
class BaseRace:
    name: RaceNames
    speed: int
    ability_bonuses: Optional[List[Ability]]
    size: int
    languages: Optional[List[LanguageNames]]
    language_description: str
    traits: Optional[List[Trait]]

    # Change the return types to other datclasses
    proficiencies: dict
    proficiency_options: dict
    subrace_options: dict

    # These are dynamic
    age: int
    alignment: str
    subrace: Optional[Subrace]


BaseRaces = {
    [RaceNames.DWARF]: BaseRace(
        name=RaceNames.DWARF,
        speed=25,
        ability_bonuses=[Ability(name=AbilityTypes.CONSITUTION, bonus=2)],
        size=SizeOptions.MEDIUM,
        proficiency={
            "source": "Dwarven Combat Training",
            "list": [
                Proficiency(ProficiencyNames.BATTLEAXE),
                Proficiency(ProficiencyNames.HANDAXE),
                Proficiency(ProficiencyNames.LIGHT_HAMMER),
                Proficiency(ProficiencyNames.WARHAMMER),
            ],
        },
        proficiency_options={
            "description": "You gain proficinecy with artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools.",
            "options": [
                ProficiencyNames.SMITHS_TOOLS,
                ProficiencyNames.BREWERS_SUPPLIES,
                ProficiencyNames.MASONS_TOOLS,
            ],
        },
        languages=[LanguageNames.COMMON, LanguageNames.DWARVISH],
        traits=[
            Trait(TraitNames.DARVISION),
            Trait(TraitNames.DWARVEN_RESILIENCE),
            Trait(TraitNames.STONECUNNING),
            Trait(TraitNames.DWARVEN_COMBAT_TRAINING),
            Trait(TraitNames.TOOL_PROFICIENCY),
        ],
        subrace_options=[Subrace(SubraceNames.HILL_DWARF), Subrace(SubraceNames.MOUNTAIN_DWARF)],
    )
    #   {
    #     # Idk if I need these cause of their use case
    #     "languages_description": "",
    #     # Idk if I need these cause they are dynamic
    #     "age": 0,
    #     "alignment": "",
    #     "subrace": "",
    # }
}


class Race(object):
    # TODO: potentially replace these properties w/ kwargs
    def __init__(self, name: RaceNames):
        race: BaseRace = BaseRace[name]
        self._name = race.name
        self._speed = race.speed
        self._ability_bonuses = race.ability_bonuses
        self._size = race.size
        #### Debating how to populate this field
        self._proficiencies = race.proficiencies
        ####
        self._proficiency_options = race.proficiency_options
        # TODO: add languages, trais, subrace_options, languages_description**, age, alignment, subrace

    @property
    def name(self) -> str:
        return self._name

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def ability_bonuses(self) -> Optional[List[Ability]]:
        return self._ability_bonuses

    @property
    def size(self) -> SizeOptions:
        return self._size

    ########################################
    # TODO: Decide if I want to make proficiencies a dynamic field and be the sum of things that come from traits, subrace, proficiencies
    # TODO: Determine the return type for proficiencies
    @property
    def proficiencies(self):
        return self._proficiencies

    # @property.setter
    # def proficiencies(self) -> SizeOptions:
    #     return self._size
    ############################################################

    # TODO: Determine the return type for proficiency_options
    @property
    def proficiency_options(self):
        return self._proficiency_options

    # ######### ######### ######### ########
    def add_proficiencies(self):
        pass

    def add_subrace(self):
        pass


# ######### ######### ######### ########
# Thought: what if I made a proficiency dependent on it's sub-components? So for a race, those proficiencies would come from the race itself, from the traits, from the proficiencies, from the subraces.

# Thoughts: any field here that's a list should have a <field>_options
