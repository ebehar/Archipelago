from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld
from .Options import is_option_enabled

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

    'Edin West',
    'Edin East',
    'Central Edin',
    'Edin Tower',

    'E-Kur-Mah',
    'Inner E-Kur-Mah',


    'Mar-Uru',
    }

connections: Dict[str, Dict[str, Callable]] = {key: {} for key in regions}

def connect(r1: str, r2: str, rule1: Callable, rule2: Callable):
    connections[r1][r2] = rule1
    connections[r2][r1] = rule2

# Eribu connects to Absu, Indi, and Ukkin-Na
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
                            state._axiomverge_has_drill(world, player))),
            lambda state: state._axiomverge_has_drill(world, player))
    
    connect('Lower Eribu', 'Absu',
            lambda state: True,
            lambda state: True)

    connect('Lower Eribu', 'Indi',
            lambda state: state._axiomverge_has_high_reach(world, player),
            lambda state: state._axiomverge_has_high_reach(world, player))

    connect('Lower Eribu', 'Ukkin-Na',
            lambda state: (state._axiomverge_has_ad2(world, player) or
                           state._axiomverge_has_redcoat(world, player)),
            lambda state: (state._axiomverge_has_ad2(world, player) or
                           state._axiomverge_has_redcoat(world, player)))

# Absu connects to Eribu, Indi, and Zi
def build_absu_connections():
    connect('Absu', 'Central Absu',
            lambda state: state._axiomverge_can_pass_laser_walls(world, player),
            lambda state: state._axiomverge_can_do_damage(world, player))
    connect('Central Absu', 'Indi',
            lambda state: state._axiomverge_has_high_reach(world, player),
            lambda state: True)
    connect('Central Absu', 'Inner Absu',
            lambda state: True,
            lambda state: True)
    connect('Inner Absu', 'Zi',
            lambda state: True,
            lambda state: state._axiomverge_has_high_reach(world, player))
    
    
# Zi connects to Absu, Indi, and Kur
def build_zi_connections():
    connect ('Zi', 'Upper Zi',
             lambda state: (state._axiomverge_can_do_damage(world, player) and
                            (state._axiomverge_has_highjump(world, player) or
                             state._axiomverge_has_high_reach(world, player))),
             lambda state: True)
    connect('Upper Zi', 'Indi',
            lambda state: state._axiomverge_has_high_reach(world, player),
            lambda state: True)
    connect('Zi', 'Lower Kur',
            lambda state: state._axiomverge_can_do_damage(world, player),
            lambda state: True)


# Kur connects to Zi, Indi, Edin, and E-Kur-Mah
def build_kur_connections():
    connect('Lower Kur', 'Upper Kur',
            lambda state: state._axiomverge_has_wallwalk(world, player),
            lambda state: state._axiomverge_has_wallwalk(world, player))

    connect('Upper Kur', 'Snowy Kur',
            # This might be a little conservative
            lambda state: (state._axiomverge_has_drone_teleport(world, player) or
                           state._axiomverge_has_high_dash(world, player) or
                           (state._axiomverge_has_grapple(world, player) and
                            state._axiomverge_has_highjump(world, player))),
            lambda state: True)

    connect('Snowy Kur', 'E-Kur-Mah',
            lambda state: (state._axiomverge_has_drone_teleport(world, player) and
                           state._axiomverge_has_dash(world, player)),
            lambda state: (state._axiomverge_has_drone_teleport(world, player) and
                           state._axiomverge_has_dash(world, player)))

    connect('Upper Kur', 'Edin East',
            lambda state: (state._axiomverge_has_ad2(world, player) or
                           state._axiomverge_has_dash(world, player)),
            lambda state: (state._axiomverge_has_ad2(world, player) or
                           state._axiomverge_has_dash(world, player)))


# Ukkin-Na connects to Indi, Edin, and Mar-Uru
def build_ukkin_na_connections():
    connect('Ukkin-Na', 'Edin West',
            lambda state: state._axiomverge_has_dash(world, player),
            lambda state: state._axiomverge_has_dash(world, player))

    connect('Ukkin-Na', 'Mar-Uru',
            lambda state: state._axiomverge_has_go_mode(world, player))


# Edin connects to Ukkin-Na, Indi, and Kur
def build_edin_connections():
    connect('Edin East', 'Central Edin',
            lambda state: state._axiomverge_has_bomb(world, player),
            lambda state: state._axiomverge_has_bomb(world, player))

    connect('Edin West', 'Central Edin',
            lambda state: (state._axiomverge_has_bomb(world, player) or
                           (state._axiomverge_has_dash(world,player) and
                            state._axiomverge_has_height_augment(world,player))),
            lambda state: (state._axiomverge_has_bomb(world, player) or
                           state._axiomverge_can_do_clone_backwards(world,player)))

    connect('Edin West', 'Edin Tower',
            lambda state: (state._axiomverge_has_dash(world, player) and
                           state._axiomverge_has_height_augment(world, player),
                           

    
