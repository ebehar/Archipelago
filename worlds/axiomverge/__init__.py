from typing import Dict, List, Set, Tuple, TextIO

from BaseClasses import Item, MultiWorld, Location, Tutorial, ItemClassification
from .Constants.Items import ITEMS
from .Items import AxiomVergeItem, item_name_to_id
from .Locations import location_name_to_id
from .Options import is_option_enabled, get_option_value, axiomverge_options
from .Regions import create_regions
from ..AutoWorld import World, WebWorld
import .Logic


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

    game: str = "AxiomVerge"
    option_definitions = axiomverge_options
    topology_present: bool = True
    remote_items: bool = False
    data_version = 0

    web = AxiomVergeWebWorld()
    item_name_to_id = item_name_to_id()
    location_name_to_id = location_name_to_id()

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)

        self.locked_locations = []
        self.location_cache = []

    def create_item(self, item: str) -> AxiomVergeItem:
        item_data = ITEMS[item]
        return AxiomVergeItem(name=item_data.name,
                              code=item_ids[item],
                              classification=item_data.classification)
