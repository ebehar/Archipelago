from typing import NamedTuple

BASIC_LOCATION_OFFSET=4103000
SLUG_LOCATION=4103600
PASSCODE_LOCATION_OFFSET=4103700
ADDRESS_BOMB_LOCATION_OFFSET=4103800


ZONE_NAMES = {
    'Eribu',
    'Absu',
    'Zi',
    'Kur',
    'Indi',
    'Ukkin-Na',
    'Edin',
    'E-Kur-Mah',
    'Mar-Uru',
    'Slug'
    }

REGION_NAMES = {
    'Menu',

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

    'Slug',
}

VANILLA_REGION_CONNECTIONS = {
    ('Menu', 'Eribu'),
    
    ('Eribu', 'Lower Eribu'),
    ('Eribu', 'Eribu Secret',)
    ('Lower Eribu', 'Absu'),
    ('Lower Eribu', 'Ukkin-Na'),
    ('Lower Eribu', 'Indi'),

    ('Absu', 'Central Absu'),
    ('Central Absu', 'Indi'),
    ('Central Absu', 'Inner Absu'),
    ('Inner Absu', 'Zi'),

    ('Zi', 'Upper Zi'),
    ('Zi', 'Lower Kur'),
    ('Upper Zi', 'Indi'),

    ('Lower Kur', 'Upper Kur'),
    ('Lower Kur', 'Indi'),
    ('Lower Kur', 'Edin East'),
    ('Upper Kur', 'Snowy Kur'),
    ('Upper Kur', 'E-Kur-Mah'),
    ('Snowy Kur', 'E-Kur-Mah'),

    ('Ukkina-Na', 'Edin West'),
    ('Ukkin-Na', 'Mar-Uru'),

    ('Edin East', 'Central Edin'),
    ('Edin West', 'Central Edin'),
    ('Edin West', 'Edin Tower'),
    ('Central Edin', 'Indi'),
    }


class LocationData(NamedTuple):
    zone_name: str,
    region_name: str,
    location_name: str,


# 1 Item
SLUG_LOCATION = LocationData('Slug', 'Slug', 'Glitched Slug'),

BASIC_LOCATIONS = {
    # Eribu - 11 Items
    LocationData('Eribu', 'Eribu', 'Morph Ball'),
    LocationData('Eribu', 'Eribu', 'Nova'),
    LocationData('Eribu', 'Eribu', 'Bug Corridor'),
    LocationData('Eribu', 'Eribu', 'Shuttle Room'),
    LocationData('Eribu', 'Eribu', 'Xedur\'s Egg'),
    LocationData('Eribu', 'Eribu', 'Under Xedur'),

    LocationData('Eribu', 'Lower Eribu', 'Left of Absu'),
    LocationData('Eribu', 'Lower Eribu', 'Left of Left of Absu'),

    LocationData('Eribu', 'Eribu Secret', 'Drone Tunnel by the Sea'),
    LocationData('Eribu', 'Eribu Secret', 'Wheelchair Room'),

    LocationData('Eribu', 'Lower Eribu', 'Exit to Indi'),

    # 23 Items
    LocationData('Absu', 'Absu', 'Fallway Drill Blocks'),
    LocationData('Absu', 'Absu', 'Below Entry Fallway'),
    LocationData('Absu', 'Absu', 'Deep Below Entry Fallway'),
    LocationData('Absu', 'Absu', 'Broccoli Corridor'),
    LocationData('Absu', 'Absu', 'Fruit Loops Room 1'),
    LocationData('Absu', 'Absu', 'Leftmost Attic'),
    LocationData('Absu', 'Absu', 'Rightmost Attic'),
    LocationData('Absu', 'Absu', 'Below Pink Fallway'),
    LocationData('Absu', 'Absu', 'Elsenova'),

    LocationData('Absu', 'Central Absu', 'Prison Cell'),
    LocationData('Absu', 'Central Absu', 'Below Prison'),
    LocationData('Absu', 'Central Absu', 'Telal\'s Egg'),
    LocationData('Absu', 'Central Absu', 'Fruit Loops Room 2'),

    LocationData('Absu', 'Inner Absu', 'Fallway after Telal'),
    LocationData('Absu', 'Inner Absu', 'Last Stop Before Green Absu'),
    LocationData('Absu', 'Inner Absu', 'Blue Zombie Corridor'),
    LocationData('Absu', 'Inner Absu', 'Green Absu Entry Drill Blocks'),
    LocationData('Absu', 'Inner Absu', 'Below Green Absu Entry'),
    LocationData('Absu', 'Inner Absu', 'Bottom of Squid Room'),
    LocationData('Absu', 'Inner Absu', 'Green Absu Shuttle Room'),
    LocationData('Absu', 'Inner Absu', 'Green Absu Broccoli Room'),
    LocationData('Absu', 'Inner Absu', 'Last Stop Before Zi'),

    # 15 Items
    LocationData('Zi', 'Zi', 'Main Lobby'),
    LocationData('Zi', 'Zi', 'Above Main Lobby'),
    LocationData('Zi', 'Zi', 'Above Roly Poly Hall'),
    LocationData('Zi', 'Zi', 'Beyond Moss Corridor'),
    LocationData('Zi', 'Zi', 'YOLO Room'),
    LocationData('Zi', 'Zi', 'Under Demon Coral'),
    LocationData('Zi', 'Zi', 'Veruska\'s Basement Left'),
    LocationData('Zi', 'Zi', 'Veruska\'s Basement Right'),
    LocationData('Zi', 'Zi', 'Left of Demon Coral'),

    LocationData('Zi', 'Upper Zi', 'Hopper Hallway'),
    LocationData('Zi', 'Upper Zi', 'Uruku'),
    LocationData('Zi', 'Upper Zi', 'Power Filter Room'),
    LocationData('Zi', 'Upper Zi', 'Uruku\'s Egg'),
    LocationData('Zi', 'Upper Zi', 'Maintenance Tunnel 1'),
    LocationData('Zi', 'Upper Zi', 'Maintenance Tunnel 2'),

    # 22 Items
    LocationData('Kur', 'Lower Kur', 'Jordans'),
    LocationData('Kur', 'Lower Kur', 'Jordans Fallway'),
    LocationData('Kur', 'Lower Kur', 'Juicy Room'),
    LocationData('Kur', 'Lower Kur', 'After Room of Pain'),
    LocationData('Kur', 'Lower Kur', 'AD2 Room'),
    LocationData('Kur', 'Lower Kur', 'Mission Impossible'),

    LocationData('Kur', 'Upper Kur', 'Drone Mini-Dungeon'),
    LocationData('Kur', 'Upper Kur', 'Laser Armadillo Corridor'),
    LocationData('Kur', 'Upper Kur', 'Drone Room'),
    LocationData('Kur', 'Upper Kur', 'Behind Drone Room'),
    LocationData('Kur', 'Upper Kur', 'Zoo (Top)'),
    LocationData('Kur', 'Upper Kur', 'Zoo (Pedestal)'),
    LocationData('Kur', 'Upper Kur', 'Zoo (Above Pedestal)'),
    LocationData('Kur', 'Upper Kur', 'Big Room (Floating Ledge)'),
    LocationData('Kur', 'Upper Kur', 'Big Room (Red Coat Blocks)'),

    LocationData('Kur', 'Snowy Kur', 'Hedgehog Room (Top Ledge)'),
    LocationData('Kur', 'Snowy Kur', 'Hedgehog Room (Second Ledge)'),
    LocationData('Kur', 'Snowy Kur', 'Hedgehog Room (Pedestal)'),
    LocationData('Kur', 'Snowy Kur', 'Reflector Room'),
    LocationData('Kur', 'Snowy Kur', 'Left of Silkbugs'),
    LocationData('Kur', 'Snowy Kur', 'Enhanced Drone Launch'),
    LocationData('Kur', 'Snowy Kur', 'Temple Entrance'),

    # 2 Items
    LocationData('Indi', 'Indi', 'Edin Exit'),
    LocationData('Indi', 'Indi', 'Eribu Exit'),

    # 11 Items
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Below Slug Room Entrance'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Slug Room'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Trenchcoat Fallway (Top)'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Trenchcoat Fallway (Bottom)'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Glugg Hallway Hidden Item'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Drug Skip Room'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Bottom of Big Open Room'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Above Elevator Shaft'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Left of Above Elevator Shaft'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Bottom of Elevator Shaft'),
    LocationData('Ukkin-Na', 'Ukkin-Na', 'Below Elevator Shaft'),

    # 15 Items
    LocationData('Edin', 'Edin East', 'Zombie Alcove 1'),
    LocationData('Edin', 'Edin East', 'Zombie Alcove 2'),

    LocationData('Edin', 'Central Edin', 'Above the Worms'),
    LocationData('Edin', 'Central Edin', 'Bird Room Top'),
    LocationData('Edin', 'Central Edin', 'Bunker'),

    LocationData('Edin', 'Edin West', 'Axiom 1'),
    LocationData('Edin', 'Edin West', 'Bird Room Drill Blocks'),
    LocationData('Edin', 'Edin West', 'Secret Tunnel'),
    LocationData('Edin', 'Edin West', 'Owl City Needle Disposal'),
    LocationData('Edin', 'Edin West', 'Above Ukkina-Na Exit'),

    LocationData('Edin', 'Edin Tower', 'Drone Secret'),
    LocationData('Edin', 'Edin Tower', 'Drone-n-Coat Room'),
    LocationData('Edin', 'Edin Tower', 'Ukhu Antechamber'),
    LocationData('Edin', 'Edin Tower', 'After Ukhu'),
    LocationData('Edin', 'Edin Tower', 'Note Room'),

    # 9 Items
    LocationData('E-Kur-Mah', 'E-Kur-Mah', 'Lobby'),
    LocationData('E-Kur-Mah', 'E-Kur-Mah', 'Golden Door 1'),
    LocationData('E-Kur-Mah', 'E-Kur-Mah', 'Key Room (Lower)'),
    LocationData('E-Kur-Mah', 'E-Kur-Mah', 'Key Room (Upper)'),

    LocationData('E-Kur-Mah', 'Inner E-Kur-Mah', 'Long Fallway'),
    LocationData('E-Kur-Mah', 'Inner E-Kur-Mah', 'Green Hell (Drone Secret)'),
    LocationData('E-Kur-Mah', 'Inner E-Kur-Mah', 'Red Coat Room (Lower)'),
    LocationData('E-Kur-Mah', 'Inner E-Kur-Mah', 'Red Coat Room (Pedestal)'),

    # 8 Items
    LocationData('Mar-Uru', 'Mar-Uru', 'After Sentinel'),
    LocationData('Mar-Uru', 'Mar-Uru', 'Sentry Puzzle (Upper)'),
    LocationData('Mar-Uru', 'Mar-Uru', 'Sentry Puzzle (Lower)'),
    LocationData('Mar-Uru', 'Mar-Uru', 'Sentry Puzzle (Drill Blocks)'),
    LocationData('Mar-Uru', 'Mar-Uru', 'Sentry Hallway'),
    LocationData('Mar-Uru', 'Mar-Uru', 'Left of Disco Hell Exit'),
    LocationData('Mar-Uru', 'Mar-Uru', 'Tie Flighter Puzzle'),
    LocationData('Mar-Uru', 'Mar-Uru', 'Disco Hell'),
    }

PASSCODE_LOCATIONS = {
    # 3 Items
    LocationData('Eribu', 'Lower Eribu', 'Passcode Left of Absu'),
    LocationData('Eribu', 'Eribu', 'Beyond Thriller Room'),
    LocationData('Eribu', 'Eribu Secret', 'Cave by the Crashing Waves'),

    # 1 Item
    LocationData('E-Kur-Mah', 'Inner E-Kur-Mah', 'Green Hell (Passcode)'),
    }

ADDRESS_BOMB_LOCATIONS = {
    # 2 Items
    LocationData('Eribu', 'Eribu', 'Above Nova Corridor'),
    LocationData('Eribu', 'Eribu', 'Sentry Alley'),

    # 2 Items
    LocationData('Absu', 'Absu', 'Left-Center Attic'),
    LocationData('Absu', 'Absu', 'Right-Center Attic'),

    # 1 Item
    LocationData('Edin', 'Edin', 'Owl City Glitch Tunnel'),
    }
