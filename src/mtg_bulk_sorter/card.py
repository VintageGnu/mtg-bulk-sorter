from functools import total_ordering

from .card_properties.rarity import Rarity
from .card_properties.subtypes import Subtypes
from .card_properties.supertypes import Supertypes
from .card_properties.types import Types
from .card_properties.mana_cost import ManaCost


@total_ordering
class Card:
    num = 1

    def __init__(self, count: int = 0, name: str = "", foil: bool = False, edition: str = "", number: int = None,
                 mana_cost: str = "", types: list[str] = [], subtypes: list[str] = [], supertypes: list[str] = [],
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
        self.types = Types(types)
        if "Creature" in self.types:
            self.subtypes = Subtypes([])
        else:
            self.subtypes = Subtypes(subtypes)
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
    def __gt__(self, other):
        if self.rarity < other.rarity:
            return True
        if self.types < other.types:
            return True
        if self.subtypes < other.subtypes:
            return True
        if self.mana_cost > other.mana_cost:
            return True
        if self.name > other.name:
            return True
        if self.number > other.number:
            return True
        if not self.foil and other.foil:
            return True
        if self.edition > other.edition:
            return True
        return False

    def mana_value(self):
        return self.mana_cost.mana_value

    def multicoloured(self):
        return self.mana_cost.multicoloured
