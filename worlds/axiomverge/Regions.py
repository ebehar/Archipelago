from typing import Dict, List, Tuple, Callable, Set
from BaseClasses import MultiWorld, Region, Entrance, Location, RegionType
from .Options import is_option_enabled
from .Locations import LocationData

region_names: Set[str] = {
    'Eribu',
    'Lower Eribu',
    'Eribu Secret',

    'Absu',
    'Central Absu',
    'Inner Absu',

    'Zi',
    'Upper Zi',

    'Lower Kur',
    'Upper Kur',
    'Snowy Kur',

    'Indi',

    'Ukkin-Na',

    'Edin West',
    'Edin East',
    'Central Edin',
    'Edin Tower',

    'E-Kur-Mah',
    'Inner E-Kur-Mah',

    'Mar-Uru',
}


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


# You can always teleport back to Eribu via the main menu
def build_return_to_eribu_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    for region_name in region_names:
        if region_name == 'Eribu':
            continue

        _connect(world, player, used_names, region_name, 'Eribu',
                 lambda state: True)


# Eribu connects to Absu, Indi, and Ukkin-Na
def build_eribu_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Eribu', 'Lower Eribu',
            lambda state: (state._axiomverge_has_drill(world, player) or
                           state._axiomverge_can_grappleclip(world, player)),
            lambda state: state._axiomverge_has_drill(world, player)
            )

    connect(world, player, used_names, 'Eribu', 'Eribu Secret',
            lambda state: (state._axiomverge_has_redcoat(world, player) or
                           state._axiomverge_has_drone_teleport(world, player) or
                           ((state._axiomverge_has_grapple(world, player) or
                             state._axiomverge_has_highdash(world, player)) and
                            state._axiomverge_has_drill(world, player))),
            lambda state: state._axiomverge_has_drill(world, player))

    connect(world, player, used_names, 'Lower Eribu', 'Absu',
            lambda state: True,
            lambda state: True)

    connect(world, player, used_names, 'Lower Eribu', 'Indi',
            lambda state: state._axiomverge_has_high_reach(world, player),
            lambda state: state._axiomverge_has_high_reach(world, player))

    connect(world, player, used_names, 'Lower Eribu', 'Ukkin-Na',
            lambda state: (state._axiomverge_has_ad2(world, player) or
                           state._axiomverge_has_redcoat(world, player)),
            lambda state: (state._axiomverge_has_ad2(world, player) or
                           state._axiomverge_has_redcoat(world, player)))

# Absu connects to Eribu, Indi, and Zi


def build_absu_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Absu', 'Central Absu',
            lambda state: state._axiomverge_can_pass_laser_walls(
                world, player),
            lambda state: state._axiomverge_can_do_damage(world, player))
    connect(world, player, used_names, 'Central Absu', 'Indi',
            lambda state: state._axiomverge_has_high_reach(world, player),
            lambda state: True)
    connect(world, player, used_names, 'Central Absu', 'Inner Absu',
            lambda state: True,
            lambda state: True)
    connect(world, player, used_names, 'Inner Absu', 'Zi',
            lambda state: True,
            lambda state: state._axiomverge_has_high_reach(world, player))


# Zi connects to Absu, Indi, and Kur
def build_zi_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Zi', 'Upper Zi',
            lambda state: (state._axiomverge_can_do_damage(world, player) and
                           (state._axiomverge_has_highjump(world, player) or
                            state._axiomverge_has_high_reach(world, player))),
            lambda state: True)
    connect(world, player, used_names, 'Upper Zi', 'Indi',
            lambda state: state._axiomverge_has_high_reach(world, player),
            lambda state: True)
    connect(world, player, used_names, 'Zi', 'Lower Kur',
            lambda state: state._axiomverge_can_do_damage(world, player),
            lambda state: True)


# Kur connects to Zi, Indi, Edin, and E-Kur-Mah
def build_kur_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Lower Kur', 'Upper Kur',
            lambda state: state._axiomverge_has_wallwalk(world, player),
            lambda state: state._axiomverge_has_wallwalk(world, player))

    connect(world, player, used_names, 'Upper Kur', 'Snowy Kur',
            # This might be a little conservative
            lambda state: (state._axiomverge_has_drone_teleport(world, player) or
                           state._axiomverge_has_high_dash(world, player) or
                           (state._axiomverge_has_grapple(world, player) and
                            state._axiomverge_has_highjump(world, player))),
            lambda state: True)

    connect(world, player, used_names, 'Snowy Kur', 'E-Kur-Mah',
            lambda state: (state._axiomverge_has_drone_teleport(world, player) and
                           state._axiomverge_has_dash(world, player)),
            lambda state: (state._axiomverge_has_drone_teleport(world, player) and
                           state._axiomverge_has_dash(world, player)))

    connect(world, player, used_names, 'Upper Kur', 'Edin East',
            lambda state: (state._axiomverge_has_ad2(world, player) or
                           state._axiomverge_has_dash(world, player)),
            lambda state: (state._axiomverge_has_ad2(world, player) or
                           state._axiomverge_has_dash(world, player)))


# Ukkin-Na connects to Indi, Edin, and Mar-Uru
def build_ukkin_na_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Ukkin-Na', 'Edin West',
            lambda state: state._axiomverge_has_dash(world, player),
            lambda state: state._axiomverge_has_dash(world, player))

    connect(world, player, used_names, 'Ukkin-Na', 'Mar-Uru',
            lambda state: state._axiomverge_has_go_mode(world, player),
            lambda state: True)


# Edin connects to Ukkin-Na, Indi, and Kur
def build_edin_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    connect(world, player, used_names, 'Edin East', 'Central Edin',
            lambda state: state._axiomverge_has_bomb(world, player),
            lambda state: state._axiomverge_has_bomb(world, player))

    connect(world, player, used_names, 'Edin West', 'Central Edin',
            lambda state: (state._axiomverge_has_bomb(world, player) or
                           (state._axiomverge_has_dash(world, player) and
                            state._axiomverge_has_height_augment(world, player))),
            lambda state: (state._axiomverge_has_bomb(world, player) or
                           state._axiomverge_can_do_clone_backwards(world, player)))

    connect(world, player, used_names, 'Edin West', 'Edin Tower',
            lambda state: (state._axiomverge_has_dash(world, player) and
                           (state._axiomverge_has_bomb(world, player) or
                            state._axiomverge_has_height_augment(world, player))),
            lambda state: (state._axiomverge_has_dash(world, player) or
                           state._axiomverge_has_bomb(world, player)))


def build_connections(world: MultiWorld, player: int, used_names: Dict[str, int]):
    build_eribu_connections(world, player, used_names)
    build_absu_connections(world, player, used_names)
    build_zi_connections(world, player, used_names)
    build_kur_connections(world, player, used_names)
    build_ukkin_na_connections(world, player, used_names)
    build_edin_connections(world, player, used_names)
    build_return_to_eribu_connections(world, player, used_names)
