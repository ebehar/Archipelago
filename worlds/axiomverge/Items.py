from typing import Dict, Set
from BaseClasses import Item, ItemClassification
from .Constants.Items import ITEMS
from .Options import is_option_enabled


class AxiomVergeItem(Item):
    game: str = "Axiom Verge"


code_offset: int = 4103000


def item_name_to_id() -> Dict[str, int]:
    items = item_name: {item_id for item_id, item_name in enumerate(ITEMS.keys(), code_offset)}
    return items
