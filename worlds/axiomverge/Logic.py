from BaseClasses import MultiWorld
from .Items import BASIC_WEAPONS, NOVAISH_WEAPONS, KILVERISH_WEAPONS
from ..AutoWorld import LogicMixin
from .Options import is_option_enabled

class AxiomVergeLogic(LogicMixin):    

    ###########
    # Helpers
    ###########
    

    def has_high_reach(self, world: MultiWorld, player: int):
        return self.has_any({'Trenchcoat', 'Red Coat', 'Grapple', 'Drone Teleport'})


    def can_reach_outer_attic(self, world: MultiWorld, player: int):
        return (self.has_any({'Red Coat', 'Drone Teleport'}, player) or
                (self.has_any({'Grapple', 'Field Disruptor'}, player) and
                 self.has('Trenchcoat', player)))


    def can_reach_left_side_attic(self, world: MultiWorld, player: int):
        return (self.can_reach_outer_attic(world, player) or
                self.has('Grapple', player))


    def can_hit_distant_switches(self, world: MultiWorld, player: int) -> bool:
        return (self.has_nova(world, player) or
                self.has_dash(world, player) or
                self.has_grapple(world, player) or
                self.can_pass_laser_walls(world, player))


    def can_pass_laser_walls(self, world: MultiWorld, player: int) -> bool:
        return (self.has_kilver(world, player) or
                self.has_dash(world, player))


    def has_kilver(self, world: MultiWorld, player: int) -> bool:
        return self.has_any(KILVERISH_WEAPONS, player)


    def has_nova(self, world: MultiWorld, player: int) -> bool:
        return (self.has_any(NOVAISH_WEAPONS, player) or
                self.has_kilver(world, player))


    def has_weapon(self, world: MultiWorld, player: int) -> bool:
        return (self.has_any(BASIC_WEAPONS) or
                self.has_nova(world, player))


    def can_do_damage(self, world: MultiWorld, player: int) -> bool:
        return (self.has_any({'Laser Drill', 'Grapple'}) or
                self.has_weapon(world, player))


    def has_height_augment(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Grapple', 'Field Disruptor', 'Drone Teleport'})


    def has_grapple(self, world: MultiWorld, player: int) -> bool:
        return self.has('Grapple', player)


    def can_grappleclip(self, world: MultiWorld, player) -> bool:
        return (self.has_grapple(world, player) and
                is_option_enabled(world, player, "GrappleClips"))


    def has_highjump(self, world: MultiWorld, player: int) -> bool:
        return (self.has('Field Disruptor', player) or
                self.has_dash(world, player) or
                self.has_drone_teleport(world, player))


    def has_dash(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Trenchcoat', 'Red Coat', player})


    def has_high_dash(self, world: MultiWorld, player: int) -> bool:
        return ((self.has('Field Disruptor') and self.has_dash(world,player)) or
            self._axiom_verge_can_drone_fly(world, player))


    def has_redcoat(self, world: MultiWorld, player: int) -> bool:
        return self.has('Red Coat', player)


    def has_wallwalk(self, world: MultiWorld, player: int) -> bool:
        return self.has_dash(world, player) or self.has('Lab Coat', player)


    def has_drill(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Laser Drill', 'Remote Drone', 'Red Coat'}, player)


    def has_drone(self, world: MultiWorld, player: int) -> bool:
        return self.has('Remote Drone', player)


    def has_ad1(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Address Disruptor 1', 'Address Disruptor 2', 'Address Bomb'}, player)


    def has_ad2(self, world: MultiWorld, player: int) -> bool:
        return self.has_any({'Address Disruptor 2', 'Address Bomb'}, player)


    def has_bomb(self, world: MultiWorld, player: int) -> bool:
        return self.has('Address Bomb', player)


    def has_drone_teleport(self, world: MultiWorld, player: int) -> bool:
        return self.has_all({'Remote Drone', 'Drone Teleport'}, player)


    def has_long_drone_teleport(self, world: MultiWorld, player: int) -> bool:
        return (self.has_drone_teleport and
                self.has('Enhanced Drone Launch', player))


    def can_drone_fly(self, world: MultiWorld, player: int) -> bool:
        return (self.has_drone_teleport(world, player) and
                (self.has('Laser Drill', player) or self.has_ad1(world, player)))


    def can_do_clone_backwards(self, world: MultiWorld, player: int) -> bool:
        return (self.has_dash(world, player) and
                (self.has_grapple(world, player) or
                 self.has_drone_teleport(world, player)))


    def has_go_mode(self, world: MultiWorld, player: int) -> bool:
        grapple_go_mode = (is_option_enabled(world, player, "Masochist") and
                           self.has_all({'Grapple', 'Field Disruptor'}))

        drone_go_mode = self.__can_drone_fly(world, player)

        return self.has('Red Coat', player) and (grapple_go_mode or drone_go_mode)


    ###################
    # Entrance Logic
    ###################

    def can_pass_thick_glitch_walls(self, world: MultiWorld, player: int) -> bool:
        return (self.has_ad2(world, player) or
                self.has_redcoat(world, player))


    def can_pass_temple_entrance(self, world: MultiWorld, player: int) -> bool:
        return (self.has_drone_teleport(world, player) and
                self.has_dash(world, player))


        
