from functools import total_ordering


@total_ordering
class Supertypes(list):

    def __repr__(self):
        return ', '.join(self)

    def __eq__(self, other):
        return set(self) == set(other)

    def __gt__(self, other):
        pass
