import re

from collections import Counter
from enum import StrEnum

from ..mana_colour import ManaColour


class ManaSymbol(StrEnum):
    WHITE = "W"
    BLUE = "U"
    BLACK = "B"
    RED = "R"
    GREEN = "G"
    X = "X"
    PHYREXIAN = "P"
    TWO = "2"


class ManaCost:
    def __init__(self, raw_cost: str = ""):
        self.raw: str = raw_cost
        self.extracted_colours: list[ManaSymbol] = []
        self.colourless: int = 0
        self.colours: ManaColour = ManaColour.NONE

        if '//' in self.raw:
            merged_cost = ''.join(self.raw.split('//'))
        else:
            merged_cost = self.raw
        # Extract the symbols from the {}
        for c in [x.replace('}', '').strip() for x in merged_cost.split('{') if x]:
            # Single letters
            letter = re.fullmatch(r"[WUBRGX]", c)
            if letter:
                if letter.string in ManaSymbol:
                    symbol = ManaSymbol(letter.string)
                    self.extracted_colours.append(symbol)
                if symbol.name in ManaColour.__members__:
                    self.colours |= ManaColour[symbol.name]
                continue

            # Numbers for colourless
            n = re.fullmatch(r"\d*", c)
            if n:
                self.colourless += int(n.string)
                continue

            # Hybrid mana symbols
            h = re.fullmatch(r"[WUBRG2P]\/[WUBRG2P]", c)
            if h:
                hybrid_split = h.string.split('/')
                if len(hybrid_split) != 2:
                    raise ValueError(f"Hybrid mana cost with more than two colours: {h}")
                self.extracted_colours.append(hybrid_split)
                continue

            # Catch anything not handled so handler can be added
            raise ValueError(f"raw_cost not parsed: {raw_cost} -> {merged_cost} -> \"{c}\"")

    def __repr__(self) -> str:
        if self.raw:
            s = f"raw: {self.raw}"
            mono_colours = Counter(
                sorted([c for c in self.extracted_colours if len(c) == 1], key=list(ManaSymbol).index)
            ).items()
            if mono_colours:
                s += "\n"
                s += "Colours: "
                s += ", ".join([f"{colour} x {count}" for colour, count in mono_colours])
            if self.colourless > 0:
                s += "\n"
                s += f"Colourless: {self.colourless}"
            hybrid_colours = Counter(["/".join(c) for c in self.extracted_colours if len(c) > 1]).items()
            if hybrid_colours:
                s += "\n"
                s += "Hybrid: "
                s += ", ".join([f"{colour}: {count}" for colour, count in hybrid_colours])
            return s
        return "None"

    def __eq__(self, other):
        if self.mana_value != other.mana_value:
            return False
        if self.extracted_colours != other.extracted_colours:
            return False
        if self.colourless != other.colourless:
            return False
        return True

    def __gt__(self, other):
        pass

    @property
    def mana_value(self) -> int:
        return len(self.extracted_colours) + self.colourless

    @property
    def is_colourless(self) -> bool:
        return self.colours.is_colourless

    @property
    def is_monocoloured(self) -> bool:
        return self.colours.is_monocoloured

    @property
    def is_multicoloured(self) -> bool:
        return self.colours.is_multicoloured
