from typing import Callable, Dict, List, NamedTuple, Tuple, Set
from BaseClasses import MultiWorld, Region, Entrance, Location, RegionType
from .Options import is_option_enabled
from Constants.RegionsAndLocations import REGION_NAMES
from .Locations import LocationData


class EntranceData(NamedTuple):
    source: int
    vanilla_dest: int
    exit_rule: Callable


entrance_table: List[List[EntranceData]] = []

def generate_entrance_data(world: MultiWorld, player: int):
        # Region 0 is 'Menu', Region 1 is Eribu
        entrance_table = [
            [EntranceData(0, 1, lambda state: True, lambda state: True)],

            # Eribu
            [
                EntranceData(1, 2,
                    lambda state: (state.has_drill(world, player) or
                        state.can_grappleclip(world, player)),
                    lambda state: state.has_drill(world, player)),

                EntranceData(1, 3, 
                    lambda state: state.can_reach_eribu_secret(world, player),
                    lambda state: state.has_drill(world, player)),
                ]

            # Lower Eribu
            [
                EntranceData(2, 13,
                    lambda state: state.can_pass_thick_glitch_walls(world, player),
                    lambda state: state.can_pass_thick_glitch_walls(world, player)),
                EntranceData(2, 12,
                    lambda state: state.has_high_reach(world, player),
                    lambda state: state.has_high_reach(world, player)),
                ]


def create_regions(world: MultiWorld, player: int, locations: Tuple[LocationData, ...],
                   location_cache: List[Location]):
    locations_per_region = get_locations_per_region(locations)

    regions = [create_region(world, player, locations_per_region, location_cache, region_name) for
               region_name in region_names]

    world.regions += regions

    names: Dict[str, int] = {}

    build_connections(world, player, names)


def get_locations_per_region(locations: Tuple[LocationData, ...]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.region, []).append(location)

    return per_region


def create_location(player: int, location_data: LocationData, region: Region,
                    location_cache: List[Location]) -> Location:
    location = Location(player, location_data.name, location_data.code, region)
    location.access_rule = location_data.rule

    location_cache.append(location)

    return location


def create_region(world: MultiWorld, player: int, locations_per_region: Dict[str, List[LocationData]],
                  location_cache: List[Location], name: str) -> Region:
    region = Region(name, RegionType.Generic, name, player)
    region.world = world

    if name in locations_per_region:
        for location_data in locations_per_region[name]:
            location = create_location(
                player, location_data, region, location_cache)
            region.locations.append(location)

    return region


def _connect(world: MultiWorld, player: int, used_names: Dict[str, int], source: str, target: str,
             rule: Callable):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    if target not in used_names:
        used_names[target] = 1
        name = target
    else:
        used_names[target] += 1
        name = target + (' ' * used_names[target])

    connection = Entrance(player, name, source_region)

    connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def connect(world: MultiWorld, player: int, used_names: Dict[str, int], source: str, target: str,
            exit_rule: Callable, return_rule: Callable):
    _connect(world, player, used_names, source, target, exit_rule)
    _connect(world, player, used_names, target, source, return_rule)


# Eribu connects to Absu, Indi, and Ukkin-Na
def build_eribu_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    _connect(world, player, used_names, 'Menu', 'Eribu',
            lambda state: True)

    connect(world, player, used_names, 'Eribu', 'Lower Eribu',
            lambda state: (state.has_drill(world, player) or
                           state.can_grappleclip(world, player)),
            lambda state: state.has_drill(world, player)
            )

    connect(world, player, used_names, 'Eribu', 'Eribu Secret',
            lambda state: (state.has_redcoat(world, player) or
                           state.has_drone_teleport(world, player) or
                           ((state.has_grapple(world, player) or
                             state.has_highdash(world, player)) and
                            state.has_drill(world, player))),
            lambda state: state.has_drill(world, player))

    connect(world, player, used_names, 'Lower Eribu', 'Absu',
            lambda state: True,
            lambda state: True)

    connect(world, player, used_names, 'Lower Eribu', 'Indi',
            lambda state: state.has_high_reach(world, player),
            lambda state: state.has_high_reach(world, player))

    connect(world, player, used_names, 'Lower Eribu', 'Ukkin-Na',
            lambda state: (state.can_pass_thick_glitch_walls(world, player) and
                           state.has_wallwalk(world, player)),
            lambda state: (state.can_pass_thick_glitch_walls(world, player) and
                           state.has_dash(world,player)))


# Absu connects to Eribu, Indi, and Zi
def build_absu_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Absu', 'Central Absu',
            lambda state: state.can_pass_laser_walls(
                world, player),
            lambda state: state.can_do_damage(world, player))
    connect(world, player, used_names, 'Central Absu', 'Indi',
            lambda state: state.has_high_reach(world, player),
            lambda state: True)
    connect(world, player, used_names, 'Central Absu', 'Inner Absu',
            lambda state: state.has_ad1(world, player),
            lambda state: True)
    connect(world, player, used_names, 'Inner Absu', 'Zi',
            lambda state: True,
            lambda state: state.has_high_reach(world, player))


# Zi connects to Absu, Indi, and Kur
def build_zi_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Zi', 'Upper Zi',
            lambda state: (state.can_do_damage(world, player) and
                           (state.has_highjump(world, player) or
                            state.has_high_reach(world, player))),
            lambda state: True)
    connect(world, player, used_names, 'Upper Zi', 'Indi',
            lambda state: state.has_high_reach(world, player),
            lambda state: True)
    connect(world, player, used_names, 'Zi', 'Lower Kur',
            lambda state: state.can_do_damage(world, player),
            lambda state: True)


# Kur connects to Zi, Indi, Edin, and E-Kur-Mah
def build_kur_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Lower Kur', 'Upper Kur',
            lambda state: state.has_wallwalk(world, player),
            lambda state: state.has_wallwalk(world, player))

    connect(world, player, used_names, 'Upper Kur', 'Snowy Kur',
            # This might be a little conservative
            lambda state: (state.has_drone_teleport(world, player) or
                           state.has_high_dash(world, player) or
                           (state.has_grapple(world, player) and
                            state.has_highjump(world, player))),
            lambda state: True)

    connect(world, player, used_names, 'Snowy Kur', 'E-Kur-Mah',
            lambda state: state.can_pass_temple_entrance(world, player),
            lambda state: state.can_pass_temple_entrance(world, player))

    connect(world, player, used_names, 'Upper Kur', 'Edin East',
            lambda state: (state.has_ad2(world, player) or
                           state.has_dash(world, player)),
            lambda state: (state.has_ad2(world, player) or
                           state.has_dash(world, player)))

    connect(world, player, used_names, 'Upper Kur', 'E-Kur-Mah',
            lambda state: state.has_redcoat(world, player),
            lambda state: state.has_redcoat(world, player))


# Ukkin-Na connects to Indi, Edin, and Mar-Uru
def build_ukkin_na_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Ukkin-Na', 'Edin West',
            lambda state: state.has_dash(world, player),
            lambda state: state.has_dash(world, player))

    connect(world, player, used_names, 'Ukkin-Na', 'Mar-Uru',
            lambda state: state.has_go_mode(world, player),
            lambda state: True)


# Edin connects to Ukkin-Na, Indi, and Kur
def build_edin_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Edin East', 'Central Edin',
            lambda state: state.has_bomb(world, player),
            lambda state: state.has_bomb(world, player))

    connect(world, player, used_names, 'Edin West', 'Central Edin',
            lambda state: (state.has_bomb(world, player) or
                           (state.has_dash(world, player) and
                            state.has_height_augment(world, player))),
            lambda state: (state.has_bomb(world, player) or
                           state.can_do_clone_backwards(world, player)))

    connect(world, player, used_names, 'Edin West', 'Edin Tower',
            lambda state: (state.has_dash(world, player) and
                           (state.has_bomb(world, player) or
                            state.has_height_augment(world, player))),
            lambda state: (state.has_dash(world, player) or
                           state.has_bomb(world, player)))


def build_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    build_eribu_connections(world, player, used_names)
    build_absu_connections(world, player, used_names)
    build_zi_connections(world, player, used_names)
    build_kur_connections(world, player, used_names)
    build_ukkin_na_connections(world, player, used_names)
    build_edin_connections(world, player, used_names)
    build_return_to_eribu_connections(world, player, used_names)
