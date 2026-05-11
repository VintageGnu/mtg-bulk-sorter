from functools import total_ordering


@total_ordering
class Types(list):

    def __repr__(self):
        return ', '.join(self.raw)

    def __eq__(self, other):
        return set(self) == set(other)

    def __gt__(self, other):
        if "Artifact" in self and "Artifact" not in other:
            return True
        if "Enchantment" in self and "Enchantment" not in other:
            return True
        if "Sorcery" in self and "Sorcery" not in other:
            return True
        if "Instant" in self and "Instant" not in other:
            return True
        if "Planeswalker" in self and "Planeswalker" not in other:
            return True
        if "Creature" in self and "Creature" not in other:
            return True
        return False
