from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from .Options import is_option_enabled

class AxiomVergeLogic(LogicMixin):
    def _axiomverge_has_high_reach(self, world: MultiWorld, player: int):
        return self.has_any({'Trenchcoat', 'Red Coat', 'Grapple', 'Drone Teleport'})
    
    def _axiomverge_can_reach_outer_attic(self, world: MultiWorld, player: int):
        return (self.has_any({'Red Coat', 'Drone Teleport'}, player) or
                (self.has_any({'Grapple', 'Field Disruptor'}, player) and
                 self.has('Trenchcoat', player)))
    
    def _axiomverge_can_reach_left_side_attic(self, world: MultiWorld, player: int):
        return (self._axiomverge_can_reach_outer_attic(world, player) or
                self.has('Grapple', player))
    
    def _axiomverge_can_hit_distant_switches(self, world: MultiWorld, player: int) -> bool:
        return (self._axiomverge_has_nova(world, player) or
                self._axiomverge_has_dash(world, player) or
                self._axiomverge_has_grapple(world, player) or
                self._axiomverge_can_pass_laser_walls(world, player))
    
    def _axiomverge_can_pass_laser_walls(self, world: MultiWorld, player: int) -> bool:
        return (self._axiomverge_has_kilver(world, player) or
                self._axiomverge_has_dash(world, player))
    
    def _axiomverge_has_kilver(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({
            'Kilver',
            'Distortion Field',
            'Reverse Slicer',
            'Flamethrower',
            'Scissor Beam',
            'Fat Beam',
            }, player)

    def _axiomverge_has_nova(self, world: MultiWorld, player: int) -> bool:
        return (self.has_any({
            'Nova',
            'Hypo-Atomizer',
            'Reflector',
            'Orbital Discharge',
            }, player) or
            self._axiomverge_has_kilver(world, player))    
    
    def _axiomverge_has_weapon(self, world: MultiWorld, player: int) -> bool:
        return (self.has_any({
            'Axiom Disruptor',
            'Multi-Disruptor',
            'Firewall',
            'Voranj',
            'Inertial Pulse',
            'Lightning Gun',
            'Turbine Pulse',
            'Shards',
            'Data Bomb',
            'Tethered Charge',
            'Quantum Variegator',
            'Ion Beam',
            'Heat Seeker',
            }) or
            self._axiomverge_has_nova(world, player))
        
    def _axiomverge_can_do_damage(self, world: MultiWorld, player: int) -> bool:
        return (
            self._axiomverge_has_grapple(world, player) or
            self._axiomverge_has_drill(world, player) or
            self._axiomverge_has_weapon(world, player) or
            )

    def _axiomverge_has_height_augment(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Grapple', 'Field Disruptor', 'Drone Teleport'})
    
    def _axiomverge_has_grapple(self, world: MultiWorld, player: int) -> bool:
        return self.has('Grapple', player)

    def _axiomverge_can_grappleclip(self, world: MultiWorld, player) -> bool:
        return (self._axiomverge_has_grapple(world, player) and
                is_option_enabled(world, player, "GrappleClips"))

    def _axiomverge_has_highjump(self, world: MultiWorld, player: int) -> bool:
        return (self.has('Field Disruptor', player) or
                self._axiomverge_has_dash(world, player) or
                self._axiomverge_has_drone_teleport(world, player))

    def _axiomverge_has_dash(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Trenchcoat', 'Red Coat', player})

    def _axiomverge_has_high_dash(self, world: MultiWOrld, player: int) -> bool:
        return (self.has('Field Disruptor') and self._axiomverge_has_dash(world,player)) or
            self._axiom_verge_can_drone_fly(world, player)

    def _axiomverge_has_redcoat(self, world: MultiWorld, player: int) -> bool:
        return self.has('Red Coat', player)

    def _axiomverge_has_wallwalk(self, world: MultiWorld, player: int) -> bool:
        return self._axiomverge_has_dash(world, player) or self.has('Lab Coat', player)

    def _axiomverge_has_drill(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Laser Drill', 'Remote Drone', 'Red Coat'}, player)

    def _axiomverge_has_drone(self, world: MultiWorld, player: int) -> bool:
        return self.has('Remote Drone', player)

    def _axiomverge_has_ad1(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Address Disruptor 1', 'Address Disruptor 2', 'Address Bomb'}, player)

    def _axiomverge_has_ad2(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Address Disruptor 2', 'Address Bomb'}, player)

    def _axiomverge_has_bomb(self, world: MultiWorld, player: int) -> bool:
        return self.has('Address Bomb', player)

    def _axiomverge_has_drone_teleport(self, world: MultiWorld, player: int) -> bool:
        return self.has_all({'Remote Drone', 'Drone Teleport'}, player)

    def _axiomverge_has_long_drone_teleport(self, world: MultiWorld, player: int) -> bool:
        return (self._axiomverge_has_drone_teleport and
                self.has('Enhanced Drone Launch', player))

    def _axiomverge_can_drone_fly(self, world: MultiWorld, player: int) -> bool:
        return (self._axiomverge_has_drone_teleport(world, player) and
                (self.has('Laser Drill', player) or self._axiomverge_has_ad1(world, player)))

    def _axiomverge_can_do_clone_backwards(self, world: MultiWorld, player: int) -> bool:
        return (self._axiomverge_has_dash(world, player) and
                (self._axiomverge_has_grapple(world, player) or
                 self._axiomverge_has_drone_teleport(world, player)))

    def _axiomverge_has_go_mode(self, world: MultiWorld, player: int) -> bool:
        grapple_go_mode =
            is_option_enabled(world, player, "Masochist") and
            self.has_all({'Grapple', 'Field Disruptor'})

        drone_go_mode =
            self._axiomverge_can_drone_fly(world, player)

        return self.has('Red Coat', player) and (grapple_go_mode or drone_go_mode)
