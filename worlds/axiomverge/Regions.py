from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld
from .Options import is_option_enabled



zones: List[str] = [
        'Eribu',
        'Absu',
        'Zi',
        'Kur',
        'Indi',
        'Ukkin-Na',
        'Edin',
        'E-Kur-Mah',
        'Mar-Uru',
    ]

regions: List[str] = {
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

    'Edin',
    'Edin Tower',

    'E-Kur-Mah',
    'Inner E-Kur-Mah',


    'Mar-Uru',
    }

connections: Dict[str, Dict[str, Callable]] = {key: {} for key in regions}

def connect(r1: str, r2: str, rule1: Callable, rule2: Callable):
    connections[r1][r2] = rule1
    connections[r2][r1] = rule2

# Eribu connects to Absu and Indi
def build_eribu_connections():
    connect('Eribu', 'Lower Eribu',
            lambda state: (state._axiomverge_has_drill(world, player) or
                           state._axiomverge_can_grappleclip(world, player)),
            lambda state: state._axiomverge_has_drill(world, player)
            )
    
    connect('Eribu', 'Eribu Secret',
            lambda state: (state._axiomverge_has_redcoat(world, player) or
                           state._axiomverge_has_drone_teleport(world, player) or
                           ((state._axiomverge_has_grapple(world, player) or
                             state._axiomverge_has_highdash(world, player)) and
                            state._axiomverge_has_drill(world,player))),
            lambda state: state._axiomverge_has_drill(world, player))
    
    connect('Lower Eribu', 'Absu',
            lambda state: True,
            lambda state: True)

    connect('Lower Eribu', 'Indi',
            lambda state: (state._axiomverge_has_dash(world, player) or
                           state._axiomverge_has_grapple(world, player) or
                           state._axiomverge_has_drone_teleport(world, player)),
            lambda state: (state._axiomverge_has_dash(world, player) or
                           state._axiomverge_has_grapple(world, player) or
                           state._axiomverge_has_drone_teleport(world, player)))

# Absu connects to Eribu, Indi, and Zi
def build_absu_connections():
    connect('Absu', 'Central Absu',
            lambda state: state._axiomverge_can_pass_laser_walls(world, player),
            lambda state: True)

# Zi connects to Absu, Indi, and Kur
def build_zi_connections():
    pass

# Kur connects to Zi, Indi, Edin, and E-Kur-Mah
def build_kur_connections():

# Ukkin-Na connects to Indi, Edin, and Mar-Uru
def build_ukkin_na_connections():

# Edin connects to Ukkin-Na, Indi, and Kur
def build_edin_connections():
