from enum import Flag, auto


class ManaColour(Flag):
    NONE = 0
    WHITE = auto()
    BLUE = auto()
    BLACK = auto()
    RED = auto()
    GREEN = auto()

    @staticmethod
    def _lt_monocoloured(first, second) -> bool:
        if first.WHITE:
            return not second.WHITE
        if first.BLUE:
            return not second.BLUE | second.WHITE
        if first.BLACK:
            return not second.BLACK | second.BLUE | second.WHITE
        if first.RED:
            return not second.RED | second.BLACK | second.BLUE | second.WHITE
        # Both are GREEN, so equal instead of less than
        return False

    @staticmethod
    def _lt_multicoloured(first, second) -> bool:
        if len(first) != len(second):
            return len(first) < len(second)
        # TODO: sort the hard way 😢
        return False

    def __lt__(self, other):
        if self.is_monocoloured:
            # Monocoloured before multicoloured or colourless
            if other.is_multicoloured or other.is_colourless:
                return True
            # Both monocoloured so sort in WUBRG order
            return ManaColour._lt_monocoloured(self, other)
        if self.is_multicoloured:
            if other.is_monocoloured:
                return False
            if other.is_colourless:
                return True
            return ManaColour._lt_multicoloured(self, other)
        # colourless, so greater than monocoloured or multicoloured, or equal to another colourless
        # i.e. never less than
        return False

    @property
    def is_colourless(self) -> bool:
        return len(self) == 0

    @property
    def is_monocoloured(self) -> bool:
        return len(self) == 1

    @property
    def is_multicoloured(self) -> bool:
        return len(self) > 1
