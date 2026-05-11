from functools import total_ordering


@total_ordering
class Rarity:
    def __init__(self, rarity: str):
        self.rarity = rarity

    def __repr__(self):
        return self.rarity

    def __eq__(self, other):
        return self.rarity == other.rarity

    def __gt__(self, other):
        if self.rarity == "mythic":
            return other.rarity in ["rare", "special", "uncommon", "common"]
        if self.rarity == "rare":
            return other.rarity in ["special", "uncommon", "common"]
        if self.rarity == "special":
            return other.rarity in ["uncommon", "common"]
        if self.rarity == "uncommon":
            return other.rarity in ["common"]
        if self.rarity == "common":
            return False
