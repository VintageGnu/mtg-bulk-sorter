import re


class ManaCost:
    def __init__(self, raw_cost: str = ""):
        self.raw = raw_cost
        self.white = 0
        self.blue = 0
        self.black = 0
        self.red = 0
        self.green = 0
        self.colourless = 0
        self.hybrid = []
        self.white_p = 0
        self.blue_p = 0
        self.black_p = 0
        self.red_p = 0
        self.green_p = 0
        self.X = 0
        self.mana_value = 0
        self.colours = {
            "white": False,
            "blue": False,
            "black": False,
            "red": False,
            "green": False
        }

        if '//' in self.raw:
            merged_cost = ''.join(self.raw.split('//'))
        else:
            merged_cost = self.raw
        # Extract the symbols from the {}
        for c in [x.replace('}', '').strip() for x in merged_cost.split('{') if x]:
            # Single letters
            letter = re.fullmatch(r"[WUBRGX]", c)
            if letter:
                if letter.string == "W":
                    self.white += 1
                    self.colours["white"] = True
                elif letter.string == "U":
                    self.blue += 1
                    self.colours["blue"] = True
                elif letter.string == "B":
                    self.black += 1
                    self.colours["black"] = True
                elif letter.string == "R":
                    self.red += 1
                    self.colours["red"] = True
                elif letter.string == "G":
                    self.green += 1
                    self.colours["green"] = True
                elif letter.string == "X":
                    self.X += 1
                self.mana_value += 1
                continue

            # Numbers for colourless
            n = re.fullmatch(r"\d*", c)
            if n:
                self.colourless += int(n.string)
                self.mana_value += int(n.string)
                continue

            # Hybrid mana symbols
            h = re.fullmatch(r"[WUBRG]\/[WUBRGP]", c)
            if h:
                hybrid_split = h.string.split('/')
                if len(hybrid_split) != 2:
                    raise ValueError(f"Hybrid mana cost with more than two colours: {h}")
                # Phyrexian Mana
                if hybrid_split[1] == "P":
                    if hybrid_split[0] == "W":
                        self.white_p += 1
                        self.colours["white"] = True
                    elif hybrid_split[0] == "U":
                        self.blue_p += 1
                        self.colours["blue"] = True
                    elif hybrid_split[0] == "B":
                        self.black_p += 1
                        self.colours["black"] = True
                    elif hybrid_split[0] == "R":
                        self.red_p += 1
                        self.colours["red"] = True
                    elif hybrid_split[0] == "G":
                        self.green_p += 1
                        self.colours["green"] = True
                else:
                    first = hybrid_split[0]
                    second = hybrid_split[1]

                    if first == second:
                        raise ValueError(f"Hybrid mana with two of the same colour: {h}")

                    hybrid_dict = {
                        "white": False,
                        "blue": False,
                        "black": False,
                        "red": False,
                        "green": False
                    }

                    if first == "W" or second == "W":
                        hybrid_dict["white"] = True
                        self.colours["white"] = True
                    if first == "U" or second == "U":
                        hybrid_dict["blue"] = True
                        self.colours["blue"] = True
                    if first == "B" or second == "B":
                        hybrid_dict["black"] = True
                        self.colours["black"] = True
                    if first == "R" or second == "R":
                        hybrid_dict["red"] = True
                        self.colours["red"] = True
                    if first == "G" or second == "G":
                        hybrid_dict["green"] = True
                        self.colours["green"] = True
                    self.hybrid.append(hybrid_dict)
                self.mana_value += 1
                continue

            # Catch anything not handled so handler can be added
            raise ValueError(f"raw_cost not parsed: {raw_cost} -> {merged_cost} -> \"{c}\"")

    def __repr__(self) -> str:
        if self.raw:
            s = f"raw: {self.raw}, "
            s += f"W: {self.white}/{self.white_p}, "
            s += f"U: {self.blue}/{self.blue_p}, "
            s += f"B: {self.black}/{self.black_p}, "
            s += f"R: {self.red}/{self.red_p}, "
            s += f"G: {self.green}/{self.green_p}, "
            s += f"C: {self.colourless}, "
            s += f"X: {self.X}, "
            s += f"Hybrid: {self.hybrid}"
            return s
        else:
            return "None"

    def mana_value(self) -> tuple[int, int]:
        return tuple[
            self.white + self.blue + self.black + self.red + self.green + self.colourless + len(self.hybrid),
            self.X
        ]
