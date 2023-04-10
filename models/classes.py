from enum import Enum


# Add all of them
class ClassNames(Enum):
    WIZARD = "wizard"


class DndClassManager(object):
    pass


class DndClass(object):
    def __init__(self, name, level=1, experience_points=0):
        self.name = name
        self.level = level
        self.experience_points = experience_points

        class_type = DndClassManager(name=name)
        self.hit_points = class_type.hit_points(level)
        self.max_hit_points = class_type.max_hit_points(level)
        self.hit_dice = class_type.hit_dice
        self.is_spell_caster = class_type.is_spell_caster
        # self.spells
        # self.proficiencies

    ### This method belongs somewhere else, it's not up to the class itself to determine what racename to use
    # def _determine_race(race_name) -> BaseRace:
    #     if race_name not in RaceNames:
    #         raise ValueError(f"{race_name} is not a valid race")

    #     match race_name:
    #         case RaceNames.DWARF:
    #             return Dwarf()
    #     pass
