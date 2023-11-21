from typing import NamedTuple

BASIC_LOCATION_OFFSET=4103000
SLUG_LOCATION=4103600
PASSCODE_LOCATION_OFFSET=4103700
ADDRESS_BOMB_LOCATION_OFFSET=4103800


REGION_NAMES = [
    'Menu',

    'Eribu',
    'Lower Eribu',
    'Eribu Secret',
    'Ukkin-Na Corridor',
    'Indi Corridor',

    'Absu',
    'Central Absu',
    'Inner Absu',

    'Zi',
    'Upper Zi',

    'Lower Kur',
    'Upper Kur',
    'Snowy Kur',

    'Indi',

    'Eribu Doorway',
    'Ukkin-Na',
    'Indi Doorway',
    'Edin Doorway',

    'Edin West',
    'Edin East',
    'Central Edin',
    'Edin Tower',

    'E-Kur-Mah',
    'Inner E-Kur-Mah',

    'Mar-Uru',

    'Slug',
    ]


class LocationData(NamedTuple):
    region_name: str,
    location_name: str,


# 1 Item
SLUG_LOCATION = LocationData('Slug', 'Glitched Slug'),

BASIC_LOCATIONS = {
    # Eribu - 11 Items
    LocationData('Eribu', 'Morph Ball'),
    LocationData('Eribu', 'Nova'),
    LocationData('Eribu', 'Bug Corridor'),
    LocationData('Eribu', 'Shuttle Room'),
    LocationData('Eribu', 'Xedur\'s Egg'),
    LocationData('Eribu', 'Under Xedur'),

    LocationData('Lower Eribu', 'Left of Absu'),
    LocationData('Lower Eribu', 'Left of Left of Absu'),

    LocationData('Eribu Secret', 'Drone Tunnel by the Sea'),
    LocationData('Eribu Secret', 'Wheelchair Room'),

    LocationData('Lower Eribu', 'Exit to Indi'),

    # 23 Items
    LocationData('Absu', 'Fallway Drill Blocks'),
    LocationData('Absu', 'Below Entry Fallway'),
    LocationData('Absu', 'Deep Below Entry Fallway'),
    LocationData('Absu', 'Broccoli Corridor'),
    LocationData('Absu', 'Fruit Loops Room 1'),
    LocationData('Absu', 'Leftmost Attic'),
    LocationData('Absu', 'Rightmost Attic'),
    LocationData('Absu', 'Below Pink Fallway'),
    LocationData('Absu', 'Elsenova'),

    LocationData('Central Absu', 'Prison Cell'),
    LocationData('Central Absu', 'Below Prison'),
    LocationData('Central Absu', 'Telal\'s Egg'),
    LocationData('Central Absu', 'Fruit Loops Room 2'),

    LocationData('Inner Absu', 'Fallway after Telal'),
    LocationData('Inner Absu', 'Last Stop Before Green Absu'),
    LocationData('Inner Absu', 'Blue Zombie Corridor'),
    LocationData('Inner Absu', 'Green Absu Entry Drill Blocks'),
    LocationData('Inner Absu', 'Below Green Absu Entry'),
    LocationData('Inner Absu', 'Bottom of Squid Room'),
    LocationData('Inner Absu', 'Green Absu Shuttle Room'),
    LocationData('Inner Absu', 'Green Absu Broccoli Room'),
    LocationData('Inner Absu', 'Last Stop Before Zi'),

    # 15 Items
    LocationData('Zi', 'Main Lobby'),
    LocationData('Zi', 'Above Main Lobby'),
    LocationData('Zi', 'Above Roly Poly Hall'),
    LocationData('Zi', 'Beyond Moss Corridor'),
    LocationData('Zi', 'YOLO Room'),
    LocationData('Zi', 'Under Demon Coral'),
    LocationData('Zi', 'Veruska\'s Basement Left'),
    LocationData('Zi', 'Veruska\'s Basement Right'),
    LocationData('Zi', 'Left of Demon Coral'),

    LocationData('Upper Zi', 'Hopper Hallway'),
    LocationData('Upper Zi', 'Uruku'),
    LocationData('Upper Zi', 'Power Filter Room'),
    LocationData('Upper Zi', 'Uruku\'s Egg'),
    LocationData('Upper Zi', 'Maintenance Tunnel 1'),
    LocationData('Upper Zi', 'Maintenance Tunnel 2'),

    # 22 Items
    LocationData('Lower Kur', 'Jordans'),
    LocationData('Lower Kur', 'Jordans Fallway'),
    LocationData('Lower Kur', 'Juicy Room'),
    LocationData('Lower Kur', 'After Room of Pain'),
    LocationData('Lower Kur', 'AD2 Room'),
    LocationData('Lower Kur', 'Mission Impossible'),

    LocationData('Upper Kur', 'Drone Mini-Dungeon'),
    LocationData('Upper Kur', 'Laser Armadillo Corridor'),
    LocationData('Upper Kur', 'Drone Room'),
    LocationData('Upper Kur', 'Behind Drone Room'),
    LocationData('Upper Kur', 'Zoo (Top)'),
    LocationData('Upper Kur', 'Zoo (Pedestal)'),
    LocationData('Upper Kur', 'Zoo (Above Pedestal)'),
    LocationData('Upper Kur', 'Big Room (Floating Ledge)'),
    LocationData('Upper Kur', 'Big Room (Red Coat Blocks)'),

    LocationData('Snowy Kur', 'Hedgehog Room (Top Ledge)'),
    LocationData('Snowy Kur', 'Hedgehog Room (Second Ledge)'),
    LocationData('Snowy Kur', 'Hedgehog Room (Pedestal)'),
    LocationData('Snowy Kur', 'Reflector Room'),
    LocationData('Snowy Kur', 'Left of Silkbugs'),
    LocationData('Snowy Kur', 'Enhanced Drone Launch'),
    LocationData('Snowy Kur', 'Temple Entrance'),

    # 2 Items
    LocationData('Indi', 'Edin Exit'),
    LocationData('Indi', 'Eribu Exit'),

    # 11 Items
    LocationData('Ukkin-Na', 'Below Slug Room Entrance'),
    LocationData('Ukkin-Na', 'Slug Room'),
    LocationData('Ukkin-Na', 'Trenchcoat Fallway (Top)'),
    LocationData('Ukkin-Na', 'Trenchcoat Fallway (Bottom)'),
    LocationData('Ukkin-Na', 'Glugg Hallway Hidden Item'),
    LocationData('Ukkin-Na', 'Drug Skip Room'),
    LocationData('Ukkin-Na', 'Bottom of Big Open Room'),
    LocationData('Ukkin-Na', 'Above Elevator Shaft'),
    LocationData('Ukkin-Na', 'Left of Above Elevator Shaft'),
    LocationData('Ukkin-Na', 'Bottom of Elevator Shaft'),
    LocationData('Ukkin-Na', 'Below Elevator Shaft'),

    # 15 Items
    LocationData('Edin East', 'Zombie Alcove 1'),
    LocationData('Edin East', 'Zombie Alcove 2'),

    LocationData('Central Edin', 'Above the Worms'),
    LocationData('Central Edin', 'Bird Room Top'),
    LocationData('Central Edin', 'Bunker'),

    LocationData('Edin West', 'Axiom 1'),
    LocationData('Edin West', 'Bird Room Drill Blocks'),
    LocationData('Edin West', 'Secret Tunnel'),
    LocationData('Edin West', 'Owl City Needle Disposal'),
    LocationData('Edin West', 'Above Ukkina-Na Exit'),

    LocationData('Edin Tower', 'Drone Secret'),
    LocationData('Edin Tower', 'Drone-n-Coat Room'),
    LocationData('Edin Tower', 'Ukhu Antechamber'),
    LocationData('Edin Tower', 'After Ukhu'),
    LocationData('Edin Tower', 'Note Room'),

    # 9 Items
    LocationData('E-Kur-Mah', 'Lobby'),
    LocationData('E-Kur-Mah', 'Golden Door 1'),
    LocationData('E-Kur-Mah', 'Key Room (Lower)'),
    LocationData('E-Kur-Mah', 'Key Room (Upper)'),

    LocationData('Inner E-Kur-Mah', 'Long Fallway'),
    LocationData('Inner E-Kur-Mah', 'Green Hell (Drone Secret)'),
    LocationData('Inner E-Kur-Mah', 'Red Coat Room (Lower)'),
    LocationData('Inner E-Kur-Mah', 'Red Coat Room (Pedestal)'),

    # 8 Items
    LocationData('Mar-Uru', 'After Sentinel'),
    LocationData('Mar-Uru', 'Sentry Puzzle (Upper)'),
    LocationData('Mar-Uru', 'Sentry Puzzle (Lower)'),
    LocationData('Mar-Uru', 'Sentry Puzzle (Drill Blocks)'),
    LocationData('Mar-Uru', 'Sentry Hallway'),
    LocationData('Mar-Uru', 'Left of Disco Hell Exit'),
    LocationData('Mar-Uru', 'Tie Flighter Puzzle'),
    LocationData('Mar-Uru', 'Disco Hell'),
    }


PASSCODE_LOCATIONS = {
    # 3 Items
    LocationData('Lower Eribu', 'Passcode Left of Absu'),
    LocationData('Eribu', 'Beyond Thriller Room'),
    LocationData('Eribu Secret', 'Cave by the Crashing Waves'),

    # 1 Item
    LocationData('Inner E-Kur-Mah', 'Green Hell (Passcode)'),
    }


ADDRESS_BOMB_LOCATIONS = {
    # 2 Items
    LocationData('Eribu', 'Above Nova Corridor'),
    LocationData('Eribu', 'Sentry Alley'),

    # 2 Items
    LocationData('Absu', 'Left-Center Attic'),
    LocationData('Absu', 'Right-Center Attic'),

    # 1 Item
    LocationData('Edin', 'Owl City Glitch Tunnel'),
    }
