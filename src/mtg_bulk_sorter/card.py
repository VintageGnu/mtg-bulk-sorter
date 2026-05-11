from .card_properties.rarity import Rarity
from .card_properties.sub_types import SubTypes
from .card_properties.super_types import SuperTypes
from .card_properties.types import Types
from .card_properties.mana_cost import ManaCost


class Card:
    def __init__(self, count: int, name: str, foil: bool, edition: str, number: int, mana_cost: ManaCost,
                 types: list, sub_types: list, super_types: SuperTypes, rarity: str):
        self.count = count
        self.name = name
        self.foil = foil
        self.edition = edition
        self.number = number
        self.mana_cost = ManaCost(mana_cost)
        self.types = Types(types)
        self.sub_types = SubTypes(sub_types)
        self.super_types = SuperTypes(super_types)
        self.rarity = Rarity(rarity)

    def __eq__(self, other):
        return self.rarity == other.rarity

    def __gt__(self, other):
        return self.rarity > other.rarity

    def mana_value(self):
        return self.mana_cost.mana_value

    def multicoloured(self):
        return len([x for x in self.mana_cost.colours.values() if x]) > 1
