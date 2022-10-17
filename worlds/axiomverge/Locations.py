from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld
from .Options import is_option_enabled

class LocationData(NamedTuple):
    region: str
    name: str
    # 4101600 - Slug Item
    # 41017xx - Passcode Locations
    # 41018xx - Address Bomb Locations
    code: Optional[int]
    rule: Callable = lambda state: state.can_do_damage(world, player)

def get_locations(world: Optional[MultiWorld], player: Optional[int]) -> Tuple[LocationData, ...]:
        location_table: List[LocationData] = [
            # This item can be obtained in multiple areas, but only once globally
            LocationData('Slug', 'Glitched Slug', 4101600,
                         lambda state: state._axiomverge_has_ad2(world, player) and
                                       (state.can_reach('Indi', 'Region', player) or
                                        state.can_reach_slug_room(player)),

            # 4101000 - 4101010
            # 10 Items
            LocationData('Eribu', 'Eribu: Morph Ball', 4101000, lambda state: True),
            LocationData('Eribu', 'Eribu: Nova', 4101001),
            LocationData('Eribu', 'Eribu: Bug Corridor', 4101002,
                         lambda state: state._axiomverge_can_hit_distant_switches(world, player)),
            LocationData('Eribu', 'Eribu: Shuttle Room', 4101003,
                         lambda state: state._axiomverge_has_drill(world, player)),
            LocationData('Eribu', 'Eribu: Xedur\'s Egg', 4101004,
                         lambda state: state._axiomverge_can_hit_distant_switches(world, player)),
            LocationData('Eribu', 'Eribu: Under Xedur', 4101005,
                         lambda state: state._axiomverge_has_drill(world, player)),
                         
            LocationData('Lower Eribu', 'Eribu (Lower): Left of Absu', 4101006,
                         lambda state: state.can_reach('Lower Eribu', 'Region', player)),
            LocationData('Lower Eribu', 'Eribu (Lower): Left of Left of Absu', 4101007,
                         lambda state: (state._axiomverge_has_ad1(world, player) and
                                        state.can_reach('Lower Eribu', 'Region', player)),
                         
            LocationData('Eribu Secret', 'Eribu (Secret): Drone Tunnel by the Sea', 4101008,
                         lambda state: (state._axiomverge_has_drone(world, player) and
                                        
                                        (state._axiomverge_has_ad2(world,player) or
                                         state._axiomverge_has_redcoat(world, player)) and
                                        
                                        state.can_reach('Eribu Secret', player)),
                         
            LocationData('Eribu Secret', 'Eribu (Secret): Wheelchair Room', 4101009,
                         lambda state: (state._axiomverge_has_drone_teleport and
                                        state.can_reach('Eribu Secret', player)),
                         
            LocationData('Lower Eribu', 'Eribu (Lower): Exit to Indi', 4101020,
                         lambda state: (
                             (state._axiomverge_has_drone_teleport(world, player) and
                              state._axiomverge_has_dash(world, player)) or
                             
                             (state._axiomverge_has_grapple(world, player) and
                              state._axiomverge_has_redcoat(world, player))
                             )
                         ),

            # 4101700 - 4101702
            # 3 Items
            LocationData('Lower Eribu', 'Eribu (Lower): Passcode Left of Absu', 4101700,
                         lambda state: (
                             state._axiomverge_has_passcode_tool(world, player) and
                             (state._axiomverge_has_highjump(world, player) or
                              state._axiomverge_has_grapple(world, player) or
                              state._axiomverge_has_ad1(world, player)),
                             
            LocationData('Eribu', 'Eribu: Beyond Thriller Room', 4101701,
                         lambda state: state._axiomverge_has_passcode_tool(world, player) and
                             (state._axiomverge_has_grapple(world, player) or
                              state._axiomverge_can_drone_fly(world, player) or
                              state._axiomverge_has_long_drone_teleport))),
                         
            LocationData('Eribu Secret', 'Eribu (Secret): Cave by the Crashing Waves', 4101702,
                         lambda state: (state._axiomverge_has_passcode_tool(world, player) and
                                        
                                        (state._axiomverge_has_ad2(world,player) or
                                         state._axiomverge_has_redcoat(world, player)) and
                                        
                                        state._axiomverge_can_drone_fly(world, player) and
                                        state.can_reach('Eribu Secret', player)),

            # 4101800 - 4101801
            # 2 Items
            LocationData('Eribu', 'Eribu: Above Nova Corridor', 4101800,
                         lambda state: state._axiomverge_has_bomb(world,player) and
                                       state._axiomverge_has_highjump(world,player)),
            LocationData('Eribu', 'Eribu: Sentry Alley', 4101801,
                         lambda state: state._axiomverge_has_bomb(world,player) and
                             (state._axiomverge_has_drone(world,player) or
                              state._axiomverge_has_redcoat(world,player)),
            

            # 4101011 - 4101033
            # 23 Items
            LocationData('Absu', 'Absu: Fallway Drill Blocks', 4101011,
                         lambda state: (state._axiomverge_has_drill(world, player) and
                                        state.can_reach('Absu', player)),
            LocationData('Absu', 'Absu: Broccoli Corridor', 4101012,
                         lambda state: (state.can_reach('Absu', player) and
                                        state._axiomverge_can_pass_laser_walls(world, player)),
            LocationData('Absu', 'Absu: Fruit Loops Room 1', 4101013,
                         lambda state: (state.can_reach('Absu',player) and
                                        (state._axiomverge_has_redcoat(world,player) or
                                         (state._axiomverge_has_ad1(world, player) and
                                          state._axiomverge_can_pass_laser_walls(world, player)))),
            LocationData('Absu', 'Absu: Elsenova', 4101014,
                         lambda state: (state.can_reach('Absu', player)),
            LocationData('Absu', 'Absu: Below Fallway', 4101015,
                         lambda state: (state.can_reach('Absu', player) and
                                        state._axiomverge_has_drone(world, player)),
            LocationData('Absu', 'Absu: Deep Below Fallway', 4101016,
                         lambda state: (state.can_reach('Absu', player) and
                                        state._axiomverge_has_drone_teleport(world, player) and
                                        (state._axiomverge_has_dash(world,player) or
                                         state.__axiomverge_can_grappleclip(world,player))),
            LocationData('Central Absu', 'Central Absu: Prison Cell', 4101017,
                         lambda state: (state.can_reach('Central Absu', player) and
                                        (state._axiomverge_has_wallwalk(world, player) or
                                         state._axiomverge_can_grappleclip(world, player)),
            LocationData('Central Absu', 'Central Absu: Below Prison', 4101018,
                         lambda state: (state.can_reach('Central Absu', player) and
                                        (state._axiomverge_has_wallwalk(world, player) or
                                         state._axiomverge_can_grappleclip(world, player))),
            LocationData('Central Absu', 'Central Absu: Telal\'s Egg', 4101019,
                         lambda state: state.can_reach('Central Absu', player)),
            LocationData('Inner Absu', 'Inner Absu: Fallway after Telal', 4101020,
                         lambda state: state.can_reach('Inner Absu', player)),
            LocationData('Central Absu', 'Central Absu: Fruit Loops Room 2', 4101021,
                         lambda state: (state.can_reach('Central Absu', player) and
                                        (state._axiomverge_has_ad1(world, player) or
                                         state._axiomverge_has_highjump(world, player))),
            LocationData('Inner Absu', 'Inner Absu: Last Stop Before Green Absu', 4101022,
                         lambda state: (state.can_reach('Inner Absu', player)),
            LocationData('Inner Absu', 'Inner Absu: Blue Zombie Corridor', 4101023),
            LocationData('Inner Absu', 'Inner Absu: Green Absu Entry Drill Blocks', 4101024),
            LocationData('Inner Absu', 'Inner Absu: Below Green Absu Entry', 4101025),
            LocationData('Inner Absu', 'Inner Absu: Bottom of Squid Room', 4101026),
            LocationData('Inner Absu', 'Inner Absu: Green Absu Shuttle Room', 4101027),
            LocationData('Inner Absu', 'Inner Absu: Green Absu Broccoli Room', 4101028),
            LocationData('Inner Absu', 'Inner Absu: Last Stop Before Zi', 4101029),
            LocationData('Absu', 'Absu: Leftmost Attic', 4101030),
            LocationData('Absu', 'Absu: Rightmost Attic', 4101031),
            LocationData('Absu', 'Absu: Below Pink Fallway', 4101032,
                         lambda state: (state.can_reach('Absu', player) and
                                        ((state._axiomverge_has_ad2(world, player) and
                                          state._axiomverge_has_dash(world, player)) or
                                         (state._axiomverge_can_grappleclip(world, player) and
                                          is_option_enabled(world, player, "AllowBlindNavigation"))),
            LocationData('Inner Absu', 'Inner Absu: Spider Heck', 4101033),

            # 4101802 - 4101803
            # 2 Items
            LocationData('Absu', 'Absu: Left-Center Attic', 4101802),
            LocationData('Absu', 'Absu: Right-Center Attic', 4101803),

            # 4101034 - 4101048
            # 15 Items
            LocationData('Zi', 'Zi: Main Lobby', 4101034),
            LocationData('Zi', 'Zi: Above Main Lobby', 4101035),
            LocationData('Zi', 'Zi: Above Roly Poly Hall', 4101036),
            LocationData('Zi', 'Zi: Beyond Moss Corridor', 4101037),
            LocationData('Zi', 'Zi: YOLO Room', 4101038),
            LocationData('Zi', 'Zi: Under Demon Coral', 4101039),
            LocationData('Zi', 'Zi: Veruska\'s Basement Left', 4101040),
            LocationData('Zi', 'Zi: Veruska\'s Basement Right', 4101041),
            LocationData('Zi', 'Zi: Left of Demon Coral', 4101042),
            LocationData('Zi', 'Zi: Hopper Hallway', 4101043),
            LocationData('Zi', 'Zi: Uruku', 4101044),
            LocationData('Zi', 'Zi: Power Filter Room', 4101045),
            LocationData('Zi', 'Zi: Uruku\'s Egg', 4101046),
            LocationData('Zi', 'Zi: Maintenance Tunnel 1', 4101047),
            LocationData('Zi', 'Zi: Maintenance Tunnel 2', 4101048),

            # 4101049 - 4101070
            # 22 Items
            LocationData('Lower Kur', 'Lower Kur: Jordans', 4101049),
            LocationData('Lower Kur', 'Lower Kur: Jordans Fallway', 4101050),
            LocationData('Lower Kur', 'Lower Kur: Juicy Room', 4101051),
            LocationData('Lower Kur', 'Lower Kur: After Room of Pain', 4101052),
            LocationData('Lower Kur', 'Lower Kur: AD2 Room', 4101053),
            LocationData('Lower Kur', 'Lower Kur: Mission Impossible', 4101054),
                         
            LocationData('Upper Kur', 'Upper Kur: Drone Mini-Dungeon', 4101055),
            LocationData('Upper Kur', 'Upper Kur: Laser Armadillo Corridor', 4101056),
            LocationData('Upper Kur', 'Upper Kur: Drone Room', 4101057),
            LocationData('Upper Kur', 'Upper Kur: Behind Drone Room', 4101058),
            LocationData('Upper Kur', 'Upper Kur: Zoo (Top)', 4101059),
            LocationData('Upper Kur', 'Upper Kur: Zoo (Pedestal)', 4101060),
            LocationData('Upper Kur', 'Upper Kur: Zoo (Above Pedestal)', 4101061),
            LocationData('Upper Kur', 'Upper Kur: Big Room (Floating Ledge)', 4101062),
            LocationData('Upper Kur', 'Upper Kur: Big Room (Red Coat Blocks)', 4101063),
                         
            LocationData('Snowy Kur', 'Snowy Kur: Hedgehog Room (Top Ledge)', 4101064),
            LocationData('Snowy Kur', 'Snowy Kur: Hedgehog Room (Second Ledge)', 4101065),
            LocationData('Snowy Kur', 'Snowy Kur: Hedgehog Room (Pedestal)', 4101066),
            LocationData('Snowy Kur', 'Snowy Kur: Reflector Room', 4101067),
            LocationData('Snowy Kur', 'Snowy Kur: Left of Silkbugs', 4101068),
            LocationData('Snowy Kur', 'Snowy Kur: Enhanced Drone Launch', 4101069),
            LocationData('Snowy Kur', 'Snowy Kur: Temple Entrance', 4101070),

            # 4101071 - 4101072
            # 2 Items
            LocationData('Indi', 'Indi: Edin Exit', 4101071),
            LocationData('Indi', 'Indi: Eribu Exit', 4101072),

            # 4101073 - 4101083
            # 11 Items
            LocationData('Ukkin-Na', 'Ukkin-Na: Below Slug Room Entrance', 4101073),
            LocationData('Ukkin-Na', 'Ukkin-Na: Slug Room', 4101074),
            LocationData('Ukkin-Na', 'Ukkin-Na: Trenchcoat Fallway (Top)', 4101075),
            LocationData('Ukkin-Na', 'Ukkin-Na: Trenchcoat Fallway (Bottom)', 4101076),
            LocationData('Ukkin-Na', 'Ukkin-Na: Glugg Hallway Hidden Item', 4101077),
            LocationData('Ukkin-Na', 'Ukkin-Na: Drug Skip Room', 4101078),
            LocationData('Ukkin-Na', 'Ukkin-Na: Bottom of Big Open Room', 4101079),
            LocationData('Ukkin-Na', 'Ukkin-Na: Above Elevator Shaft', 4101080),
            LocationData('Ukkin-Na', 'Ukkin-Na: Left of Above Elevator Shaft', 4101081),
            LocationData('Ukkin-Na', 'Ukkin-Na: Bottom of Elevator Shaft', 4101082),
            LocationData('Ukkin-Na', 'Ukkin-Na: Below Elevator Shaft', 4101083),
            
            # 4101084 - 4101098
            # 15 Items
            LocationData('Edin East', 'Edin: Zombie Alcove 1', 4101084),
            LocationData('Edin East', 'Edin: Zombie Alcove 2', 4101085),
                                        
            LocationData('Edin West', 'Edin: Axiom 1', 4101086),
            LocationData('Central Edin', 'Edin: Above the Worms', 4101087),
            LocationData('Central Edin', 'Edin: Bird Room Top', 4101088),
            LocationData('Edin West', 'Edin: Bird Room Drill Blocks', 4101089),
            LocationData('Edin West', 'Edin: Secret Tunnel', 4101090),
            LocationData('Edin West', 'Edin: Owl City Needle Disposal', 4101091),
            LocationData('Edin West', 'Edin: Above Ukkina-Na Exit', 4101092),
            LocationData('Central Edin', 'Edin: Bunker', 4101093),
            
            LocationData('Edin Tower', 'Edin Tower: Drone Secret', 4101094),
            LocationData('Edin Tower', 'Edin Tower: Drone-n-Coat Room', 4101095),
            LocationData('Edin Tower', 'Edin Tower: Ukhu Antechamber', 4101096),
            LocationData('Edin Tower', 'Edin Tower: After Ukhu', 4101097),
            LocationData('Edin Tower', 'Edin Tower: Note Room', 4101098),

            # 4101804-4101804
            # 1 Item
            LocationData('Edin', 'Edin: Owl City Glitch Tunnel', 4101804),             

            # 4101099-4101106
            # 9 Items

            LocationData('E-Kur-Mah', 'E-Kur-Mah: Lobby', 4101099),
            LocationData('E-Kur-Mah', 'E-Kur-Mah: Golden Door 1', 4101100),
            LocationData('E-Kur-Mah', 'E-Kur-Mah: Key Room (Lower)', 4101101),
            LocationData('E-Kur-Mah', 'E-Kur-Mah: Key Room (Upper)', 4101102),
            LocationData('Inner E-Kur-Mah', 'Inner E-Kur-Mah: Long Fallway', 4101103),
            LocationData('Inner E-Kur-Mah', 'Inner E-Kur-Mah: Green Hell (Drone Secret)', 4101104),
            LocationData('Inner E-Kur-Mah', 'Inner E-Kur-Mah: Red Coat Room (Lower)', 4101105),
            LocationData('Inner E-Kur-Mah', 'Inner E-Kur-Mah: Red Coat Room (Pedestal)', 4101106),
                         
            # 4101703-4101703
            # 1 Item
            LocationData('Inner E-Kur-Mah', 'Inner E-Kur-Mah: Green Hell (Passcode)', 4101703),

            # 4101107-410114
            # 8 Items
            LocationData('Mar-Uru', 'Mar-Uru: After Sentinel', 4101107),
            LocationData('Mar-Uru', 'Mar-Uru: Sentry Puzzle (Upper)', 4101108),
            LocationData('Mar-Uru', 'Mar-Uru: Sentry Puzzle (Lower)', 4101109),
            LocationData('Mar-Uru', 'Mar-Uru: Sentry Puzzle (Drill Blocks)', 4101110),
            LocationData('Mar-Uru', 'Mar-Uru: Sentry Hallway', 4101111),
            LocationData('Mar-Uru', 'Mar-Uru: Left of Disco Hell Exit', 4101112),
            LocationData('Mar-Uru', 'Mar-Uru: Tie Flighter Puzzle', 4101113),
            LocationData('Mar-Uru', 'Mar-Uru: Disco Hell', 4101114),  
            
        ]
