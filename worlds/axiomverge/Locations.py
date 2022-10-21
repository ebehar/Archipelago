from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld
from .Options import is_option_enabled


class LocationData(NamedTuple):
    region: str
    name: str
    # 4103600 - Slug Item
    # 41037xx - Passcode Locations
    # 41038xx - Address Bomb Locations
    code: Optional[int]
    rule: Callable = lambda state: True


def get_locations(world: Optional[MultiWorld], player: Optional[int]) -> Tuple[LocationData, ...]:
    location_table: List[LocationData] = [
        # This item can be obtained in multiple areas, but only once globally
        LocationData('Slug', 'Glitched Slug', 4103600,
                     lambda state: state._axiomverge_has_ad2(world, player) and
                     (state.can_reach('Indi', 'Region', player) or
                      state.can_reach_slug_room(player))),

        # 4103000 - 4103010
        # 10 Items
        LocationData('Eribu', 'Eribu: Morph Ball', 4103000),
        LocationData('Eribu', 'Eribu: Nova', 4103001,
                     lambda state: state.can_do_damage(world, player)),
        LocationData('Eribu', 'Eribu: Bug Corridor', 4103002,
                     lambda state: state._axiomverge_can_hit_distant_switches(world, player)),
        LocationData('Eribu', 'Eribu: Shuttle Room', 4103003,
                     lambda state: state._axiomverge_has_drill(world, player)),
        LocationData('Eribu', 'Eribu: Xedur\'s Egg', 4103004,
                     lambda state: state._axiomverge_can_hit_distant_switches(world, player)),
        LocationData('Eribu', 'Eribu: Under Xedur', 4103005,
                     lambda state: state._axiomverge_has_drill(world, player)),

        LocationData('Lower Eribu', 'Eribu (Lower): Left of Absu', 4103006,
                     lambda state: state.can_reach('Lower Eribu', 'Region', player)),
        LocationData('Lower Eribu', 'Eribu (Lower): Left of Left of Absu', 4103007,
                     lambda state: (state._axiomverge_has_ad1(world, player) and
                                    state.can_reach('Lower Eribu', 'Region', player))),

        LocationData('Eribu Secret', 'Eribu (Secret): Drone Tunnel by the Sea', 4103008,
                     lambda state: (state._axiomverge_has_drone(world, player) and

                                    (state._axiomverge_has_ad2(world, player) or
                                     state._axiomverge_has_redcoat(world, player)) and

                                    state.can_reach('Eribu Secret', player))),

        LocationData('Eribu Secret', 'Eribu (Secret): Wheelchair Room', 4103009,
                     lambda state: (state._axiomverge_has_drone_teleport and
                                    state.can_reach('Eribu Secret', player))),

        LocationData('Lower Eribu', 'Eribu (Lower): Exit to Indi', 4103020,
                     lambda state: (
                         (state._axiomverge_has_drone_teleport(world, player) and
                          state._axiomverge_has_dash(world, player)) or

                         (state._axiomverge_has_grapple(world, player) and
                          state._axiomverge_has_redcoat(world, player))
                     )
                     ),

        # 4103700 - 4103702
        # 3 Items
        LocationData('Lower Eribu', 'Eribu (Lower): Passcode Left of Absu', 4103700,
                     lambda state: (
                         state._axiomverge_has_passcode_tool(world, player) and
                         (state._axiomverge_has_highjump(world, player) or
                          state._axiomverge_has_grapple(world, player) or
                          state._axiomverge_has_ad1(world, player)))),

        LocationData('Eribu', 'Eribu: Beyond Thriller Room', 4103701,
                     lambda state: state._axiomverge_has_passcode_tool(world, player) and
                     (state._axiomverge_has_grapple(world, player) or
                      state._axiomverge_can_drone_fly(world, player) or
                      state._axiomverge_has_long_drone_teleport)),

        LocationData('Eribu Secret', 'Eribu (Secret): Cave by the Crashing Waves', 4103702,
                     lambda state: (state._axiomverge_has_passcode_tool(world, player) and

                                    (state._axiomverge_has_ad2(world, player) or
                                     state._axiomverge_has_redcoat(world, player)) and

                                    state._axiomverge_can_drone_fly(world, player) and
                                    state.can_reach('Eribu Secret', player))),

        # 4103800 - 4103801
        # 2 Items
        LocationData('Eribu', 'Eribu: Above Nova Corridor', 4103800,
                     lambda state: state._axiomverge_has_bomb(world, player) and
                     state._axiomverge_has_highjump(world, player)),
        LocationData('Eribu', 'Eribu: Sentry Alley', 4103801,
                     lambda state: state._axiomverge_has_bomb(world, player) and
                     (state._axiomverge_has_drone(world, player) or
                      state._axiomverge_has_redcoat(world, player))),


        # 4103011 - 4103033
        # 23 Items
        LocationData('Absu', 'Absu: Fallway Drill Blocks', 4103011,
                     lambda state: (state._axiomverge_has_drill(world, player) and
                                    state.can_reach('Absu', player))),
        LocationData('Absu', 'Absu: Broccoli Corridor', 4103012,
                     lambda state: (state.can_reach('Absu', player) and
                                    state._axiomverge_can_pass_laser_walls(world, player))),
        LocationData('Absu', 'Absu: Fruit Loops Room 1', 4103013,
                     lambda state: (state.can_reach('Absu', player) and
                                    (state._axiomverge_has_redcoat(world, player) or
                                     (state._axiomverge_has_ad1(world, player) and
                                      state._axiomverge_can_pass_laser_walls(world, player))))),
        LocationData('Absu', 'Absu: Elsenova', 4103014,
                     lambda state: (state.can_reach('Absu', player))),
        LocationData('Absu', 'Absu: Below Fallway', 4103015,
                     lambda state: (state.can_reach('Absu', player) and
                                    state._axiomverge_has_drone(world, player))),
        LocationData('Absu', 'Absu: Deep Below Fallway', 4103016,
                     lambda state: (state.can_reach('Absu', player) and
                                    state._axiomverge_has_drone_teleport(world, player) and
                                    (state._axiomverge_has_dash(world, player) or
                                     state.__axiomverge_can_grappleclip(world, player)))),
        LocationData('Central Absu', 'Central Absu: Prison Cell', 4103017,
                     lambda state: (state.can_reach('Central Absu', player) and
                                    (state._axiomverge_has_wallwalk(world, player) or
                                     state._axiomverge_can_grappleclip(world, player)))),
        LocationData('Central Absu', 'Central Absu: Below Prison', 4103018,
                     lambda state: (state.can_reach('Central Absu', player) and
                                    (state._axiomverge_has_wallwalk(world, player) or
                                     state._axiomverge_can_grappleclip(world, player)))),
        LocationData('Central Absu', 'Central Absu: Telal\'s Egg', 4103019,
                     lambda state: state.can_reach('Central Absu', player)),
        LocationData('Inner Absu', 'Inner Absu: Fallway after Telal', 4103020,
                     lambda state: state.can_reach('Inner Absu', player)),
        LocationData('Central Absu', 'Central Absu: Fruit Loops Room 2', 4103021,
                     lambda state: (state.can_reach('Central Absu', player) and
                                    (state._axiomverge_has_ad1(world, player) or
                                     state._axiomverge_has_highjump(world, player)))),
        LocationData('Inner Absu', 'Inner Absu: Last Stop Before Green Absu', 4103022,
                     lambda state: (state.can_reach('Inner Absu', player))),
        LocationData(
            'Inner Absu', 'Inner Absu: Blue Zombie Corridor', 4103023),
        LocationData(
            'Inner Absu', 'Inner Absu: Green Absu Entry Drill Blocks', 4103024),
        LocationData(
            'Inner Absu', 'Inner Absu: Below Green Absu Entry', 4103025),
        LocationData(
            'Inner Absu', 'Inner Absu: Bottom of Squid Room', 4103026),
        LocationData(
            'Inner Absu', 'Inner Absu: Green Absu Shuttle Room', 4103027),
        LocationData(
            'Inner Absu', 'Inner Absu: Green Absu Broccoli Room', 4103028),
        LocationData('Inner Absu', 'Inner Absu: Last Stop Before Zi', 4103029),
        LocationData('Absu', 'Absu: Leftmost Attic', 4103030),
        LocationData('Absu', 'Absu: Rightmost Attic', 4103031),
        LocationData('Absu', 'Absu: Below Pink Fallway', 4103032,
                     lambda state: (state.can_reach('Absu', player) and
                                    ((state._axiomverge_has_ad2(world, player) and
                                      state._axiomverge_has_dash(world, player)) or
                                     (state._axiomverge_can_grappleclip(world, player) and
                                      is_option_enabled(world, player, "AllowBlindNavigation"))))),
        LocationData('Inner Absu', 'Inner Absu: Spider Heck', 4103033),

        # 4103802 - 4103803
        # 2 Items
        LocationData('Absu', 'Absu: Left-Center Attic', 4103802),
        LocationData('Absu', 'Absu: Right-Center Attic', 4103803),

        # 4103034 - 4103048
        # 15 Items
        LocationData('Zi', 'Zi: Main Lobby', 4103034),
        LocationData('Zi', 'Zi: Above Main Lobby', 4103035),
        LocationData('Zi', 'Zi: Above Roly Poly Hall', 4103036),
        LocationData('Zi', 'Zi: Beyond Moss Corridor', 4103037),
        LocationData('Zi', 'Zi: YOLO Room', 4103038),
        LocationData('Zi', 'Zi: Under Demon Coral', 4103039),
        LocationData('Zi', 'Zi: Veruska\'s Basement Left', 4103040),
        LocationData('Zi', 'Zi: Veruska\'s Basement Right', 4103041),
        LocationData('Zi', 'Zi: Left of Demon Coral', 4103042),
        LocationData('Zi', 'Zi: Hopper Hallway', 4103043),
        LocationData('Zi', 'Zi: Uruku', 4103044),
        LocationData('Zi', 'Zi: Power Filter Room', 4103045),
        LocationData('Zi', 'Zi: Uruku\'s Egg', 4103046),
        LocationData('Zi', 'Zi: Maintenance Tunnel 1', 4103047),
        LocationData('Zi', 'Zi: Maintenance Tunnel 2', 4103048),

        # 4103049 - 4103070
        # 22 Items
        LocationData('Lower Kur', 'Lower Kur: Jordans', 4103049),
        LocationData('Lower Kur', 'Lower Kur: Jordans Fallway', 4103050),
        LocationData('Lower Kur', 'Lower Kur: Juicy Room', 4103051),
        LocationData('Lower Kur', 'Lower Kur: After Room of Pain', 4103052),
        LocationData('Lower Kur', 'Lower Kur: AD2 Room', 4103053),
        LocationData('Lower Kur', 'Lower Kur: Mission Impossible', 4103054),

        LocationData('Upper Kur', 'Upper Kur: Drone Mini-Dungeon', 4103055),
        LocationData(
            'Upper Kur', 'Upper Kur: Laser Armadillo Corridor', 4103056),
        LocationData('Upper Kur', 'Upper Kur: Drone Room', 4103057),
        LocationData('Upper Kur', 'Upper Kur: Behind Drone Room', 4103058),
        LocationData('Upper Kur', 'Upper Kur: Zoo (Top)', 4103059),
        LocationData('Upper Kur', 'Upper Kur: Zoo (Pedestal)', 4103060),
        LocationData('Upper Kur', 'Upper Kur: Zoo (Above Pedestal)', 4103061),
        LocationData(
            'Upper Kur', 'Upper Kur: Big Room (Floating Ledge)', 4103062),
        LocationData(
            'Upper Kur', 'Upper Kur: Big Room (Red Coat Blocks)', 4103063),

        LocationData(
            'Snowy Kur', 'Snowy Kur: Hedgehog Room (Top Ledge)', 4103064),
        LocationData(
            'Snowy Kur', 'Snowy Kur: Hedgehog Room (Second Ledge)', 4103065),
        LocationData(
            'Snowy Kur', 'Snowy Kur: Hedgehog Room (Pedestal)', 4103066),
        LocationData('Snowy Kur', 'Snowy Kur: Reflector Room', 4103067),
        LocationData('Snowy Kur', 'Snowy Kur: Left of Silkbugs', 4103068),
        LocationData('Snowy Kur', 'Snowy Kur: Enhanced Drone Launch', 4103069),
        LocationData('Snowy Kur', 'Snowy Kur: Temple Entrance', 4103070),

        # 4103071 - 4103072
        # 2 Items
        LocationData('Indi', 'Indi: Edin Exit', 4103071),
        LocationData('Indi', 'Indi: Eribu Exit', 4103072),

        # 4103073 - 4103083
        # 11 Items
        LocationData(
            'Ukkin-Na', 'Ukkin-Na: Below Slug Room Entrance', 4103073),
        LocationData('Ukkin-Na', 'Ukkin-Na: Slug Room', 4103074),
        LocationData(
            'Ukkin-Na', 'Ukkin-Na: Trenchcoat Fallway (Top)', 4103075),
        LocationData(
            'Ukkin-Na', 'Ukkin-Na: Trenchcoat Fallway (Bottom)', 4103076),
        LocationData(
            'Ukkin-Na', 'Ukkin-Na: Glugg Hallway Hidden Item', 4103077),
        LocationData('Ukkin-Na', 'Ukkin-Na: Drug Skip Room', 4103078),
        LocationData('Ukkin-Na', 'Ukkin-Na: Bottom of Big Open Room', 4103079),
        LocationData('Ukkin-Na', 'Ukkin-Na: Above Elevator Shaft', 4103080),
        LocationData(
            'Ukkin-Na', 'Ukkin-Na: Left of Above Elevator Shaft', 4103081),
        LocationData(
            'Ukkin-Na', 'Ukkin-Na: Bottom of Elevator Shaft', 4103082),
        LocationData('Ukkin-Na', 'Ukkin-Na: Below Elevator Shaft', 4103083),

        # 4103084 - 4103098
        # 15 Items
        LocationData('Edin East', 'Edin: Zombie Alcove 1', 4103084),
        LocationData('Edin East', 'Edin: Zombie Alcove 2', 4103085),

        LocationData('Edin West', 'Edin: Axiom 1', 4103086),
        LocationData('Central Edin', 'Edin: Above the Worms', 4103087),
        LocationData('Central Edin', 'Edin: Bird Room Top', 4103088),
        LocationData('Edin West', 'Edin: Bird Room Drill Blocks', 4103089),
        LocationData('Edin West', 'Edin: Secret Tunnel', 4103090),
        LocationData('Edin West', 'Edin: Owl City Needle Disposal', 4103091),
        LocationData('Edin West', 'Edin: Above Ukkina-Na Exit', 4103092),
        LocationData('Central Edin', 'Edin: Bunker', 4103093),

        LocationData('Edin Tower', 'Edin Tower: Drone Secret', 4103094),
        LocationData('Edin Tower', 'Edin Tower: Drone-n-Coat Room', 4103095),
        LocationData('Edin Tower', 'Edin Tower: Ukhu Antechamber', 4103096),
        LocationData('Edin Tower', 'Edin Tower: After Ukhu', 4103097),
        LocationData('Edin Tower', 'Edin Tower: Note Room', 4103098),

        # 4103804-4103804
        # 1 Item
        LocationData('Edin', 'Edin: Owl City Glitch Tunnel', 4103804),

        # 4103099-4103106
        # 9 Items

        LocationData('E-Kur-Mah', 'E-Kur-Mah: Lobby', 4103099),
        LocationData('E-Kur-Mah', 'E-Kur-Mah: Golden Door 1', 4103100),
        LocationData('E-Kur-Mah', 'E-Kur-Mah: Key Room (Lower)', 4103101),
        LocationData('E-Kur-Mah', 'E-Kur-Mah: Key Room (Upper)', 4103102),
        LocationData('Inner E-Kur-Mah',
                     'Inner E-Kur-Mah: Long Fallway', 4103103),
        LocationData('Inner E-Kur-Mah',
                     'Inner E-Kur-Mah: Green Hell (Drone Secret)', 4103104),
        LocationData('Inner E-Kur-Mah',
                     'Inner E-Kur-Mah: Red Coat Room (Lower)', 4103105),
        LocationData('Inner E-Kur-Mah',
                     'Inner E-Kur-Mah: Red Coat Room (Pedestal)', 4103106),

        # 4103703-4103703
        # 1 Item
        LocationData('Inner E-Kur-Mah',
                     'Inner E-Kur-Mah: Green Hell (Passcode)', 4103703),

        # 4103107-410314
        # 8 Items
        LocationData('Mar-Uru', 'Mar-Uru: After Sentinel', 4103107),
        LocationData('Mar-Uru', 'Mar-Uru: Sentry Puzzle (Upper)', 4103108),
        LocationData('Mar-Uru', 'Mar-Uru: Sentry Puzzle (Lower)', 4103109),
        LocationData(
            'Mar-Uru', 'Mar-Uru: Sentry Puzzle (Drill Blocks)', 4103110),
        LocationData('Mar-Uru', 'Mar-Uru: Sentry Hallway', 4103111),
        LocationData('Mar-Uru', 'Mar-Uru: Left of Disco Hell Exit', 4103112),
        LocationData('Mar-Uru', 'Mar-Uru: Tie Flighter Puzzle', 4103113),
        LocationData('Mar-Uru', 'Mar-Uru: Disco Hell', 4103114),

    ]

    return tuple(location_table)
