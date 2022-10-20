from typing import Dict, Union
from BaseClasses import MultiWorld
from Options import Toggle, DefaultOnToggle, DeathLink, Choice, Range, Option, OptionDict
from schema import Schema, And, Optional


class Masochist(Toggle):
    "Place the Drone Teleport in Disco Hell, requiring the Disco Hell Rocket Jump"
    display_name = "Masochist"


class PasscodeChecks(Toggle):
    "Passcode Tool checks can contain progression items"
    display_name = "Passcode Checks"


class ReplaceNotes(Choice):
    "Notes will be replaced with something else"
    display_name = "ReplaceNotes"
    option_off = 0
    option_fragments = 1
    option_size_range_nodes = 2
    option_health_power_nodes = 3
    option_nothing = 4


# Blatantly stolen from Timespinner Rando, sorry!
class DamageRando(Choice):
    "Randomly nerfs and buffs some weapons"
    display_name = "Damage Rando"
    option_off = 0
    option_allnerfs = 1
    option_mostlynerfs = 2
    option_balanced = 3
    option_mostlybuffs = 4
    option_allbuffs = 5


class AllowBlindNavigation(Toggle):
    "Glitches that place the player outside the current room will be considered logical access to items"
    display_name = "Allow Blind Navigation"


class GrappleClips(Toggle):
    "Grapple clipping will be considered logical access to items"
    display_name = "Grapple Clips"


class VoidWarps(Toggle):
    "Void warps (teleporting the drone by hatching it out of bounds) will be considered logical access to items"
    display_name = "Void Warps"


class BossRandomizer(Toggle):
    "Randomize which boss appears in which location"
    display_name = "Boss Randomizer"


class YouAintGoinNowhere(Toggle):
    "Add laser barriers to Xedur Hul's room"
    display_name = "You Ain't Goin' Nowhere"


axiomverge_options: Dict[str, Option] = {
    "Masochist": Masochist,
    "PasscodeChecks": PasscodeChecks,
    "ReplaceNotes": ReplaceNotes,
    #"DamageRando": DamageRando,
    #"AllowBlindNavigation": AllowBlindNavigation,
    #"GrappleClips": GrappleClips,
    #"VoidWarps": VoidWarps,
    #"BossRandomizer": BossRandomizer,
    #"YouAintGoinNowhere": YouAintGoinNowhere,
    }

def is_option_enabled(world: MultiWorld, player: int, name: str) -> bool:
    return get_option_value(world, player, name) > 0


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, dict]:
    option = getattr(world, name, None)
    if option is None:
        return 0

    return option[player].value
