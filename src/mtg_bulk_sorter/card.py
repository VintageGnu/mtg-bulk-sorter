from functools import total_ordering

from .card_properties.rarity import Rarity
from .card_properties.subtypes import Subtypes
from .card_properties.supertypes import Supertypes
from .card_properties.types import Types
from .card_properties.mana_cost import ManaCost


@total_ordering
#pylint: disable-next=too-many-instance-attributes
class Card:
    num = 1

    # pylint: disable-next=too-many-arguments,too-many-positional-arguments
    def __init__(self, count: int = 0, name: str = "", foil: bool = False, edition: str = "", number: int = None,
                 mana_cost: str = "", types: list[str] = None, subtypes: list[str] = None, supertypes: list[str] = None,
                 rarity: str = ""):
        self.count = count
        self.name = name
        self.foil = foil
        self.edition = edition
        if number:
            self.number = number
        else:
            self.number = Card.num
            Card.num += 1
        self.mana_cost = ManaCost(mana_cost)
        if types is None:
            types = []
        self.types = Types(types)
        if subtypes is None:
            subtypes = []
        if "Creature" in self.types:
            self.subtypes = Subtypes([])
        else:
            self.subtypes = Subtypes(subtypes)
        if supertypes is None:
            supertypes = []
        self.supertypes = Supertypes(supertypes)
        self.rarity = Rarity(rarity)

    def __repr__(self):
        return f"{self.name} ({self.mana_cost.raw})"

    def __eq__(self, other):
        if self.foil != other.foil:
            return False
        if self.edition != other.edition:
            return False
        if self.number != other.number:
            return False
        return True

    # Greater than means sorted after, so take care with < vs > in these comparisons!
    # Order is also important as earlier tests are broader categories.
    def __gt__(self, other):
        if any(getattr(self, a) < getattr(other, a) for a in ["rarity", "types", "subtypes"]):
            return True
        if any(getattr(self, a) > getattr(other, a) for a in ["mana_cost", "name", "number"]):
            return True
        if (not self.foil and other.foil) or (self.edition > other.edition):
            return True
        return False

    def mana_value(self):
        return self.mana_cost.mana_value

    def multicoloured(self):
        return self.mana_cost.multicoloured
