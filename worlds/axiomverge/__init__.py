from typing import Dict, List, Set, Tuple, TextIO

from BaseClasses import Item, MultiWorld, Location, Tutorial, ItemClassification
from .Items import AxiomVergeItem, get_item_names_per_category, item_table
from .Locations import get_locations
from .LogicMixin import AxiomVergeLogic
from .Options import is_option_enabled, get_option_value, axiomverge_options
from .Regions import create_regions
from ..AutoWorld import World, WebWorld

class AxiomVergeWebWorld(WebWorld):
    # TODO:
    # Write a setup guide and web stuff
    

class AxiomVergeWorld(World):
    """
    Axiom Verge is a Geigeresque Metroidvania that takes cues from Contra,
    Bionic Commando, and of course Metroid! Journey across the world of Sudra to
    stop the mysterious Athetos, destroyer of the Sudran people, and return home
    to Earth!
    """
    
    option_definitions = axiomverge_options
    game = "Timespinner"
    topology_present = True
    remote_items = False
    data_version = 10
    web = AxiomVergeWebWorld()

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)

        self.locked_locations = []
        self.location_cache = []


    def create_item(self, item: str) -> AxiomVergeItem:
        return item_table
    
    def generate_early(self):
        if (is_option_set('Masochist') and
            'Drone Teleport' not in self.world.local_items[self.player]):
            self.world.local_items.append('Drone Teleport')
