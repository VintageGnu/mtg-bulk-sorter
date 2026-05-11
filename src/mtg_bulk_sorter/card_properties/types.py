from functools import total_ordering


@total_ordering
class Types(list):

    def __repr__(self):
        return ', '.join(self)

    def __eq__(self, other):
        return set(self) == set(other)

    def __gt__(self, other):
        if any(t in self and t not in other for t in
        ["Artifact", "Enchantment", "Sorcery", "Instant", "Planeswalker", "Creature"]):
            return True
        return False
