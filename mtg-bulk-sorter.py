import csv
import glob
import re

from functools import total_ordering
from sortedcontainers import SortedList

class ManaCost:
    def __init__(self, raw_cost: str=""):
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
            l = re.fullmatch(r"[WUBRGX]", c)
            if l:
                if l.string == "W":
                    self.white += 1
                    self.colours["white"] = True
                elif l.string == "U":
                    self.blue += 1
                    self.colours["blue"] = True
                elif l.string == "B":
                    self.black += 1
                    self.colours["black"] = True
                elif l.string == "R":
                    self.red += 1
                    self.colours["red"] = True
                elif l.string == "G":
                    self.green += 1
                    self.colours["green"] = True
                elif l.string == "X":
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
            raise ValueError(f"raw_cost not parsed: {raw} -> {merged_cost} -> \"{c}\"")
        
    
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
        return tuple[self.white + self.blue + self.black + self.red + self.green + self.colourless + len(self.hybrid), self.X]

class Types:
    def __init__(self, types: list):
        self.raw = types
        self.creature = False
        self.planeswalker = False
        self.instant = False
        self.sorcery = False
        self.enchantment = False
        self.artifact = False
        self.land = False
        self.kindred = False

        for t in self.raw:
            if t == "Creature":
                self.creature = True
                continue
            if t == "Planeswalker":
                self.planeswalker = True
                continue
            if t == "Instant":
                self.instant = True
                continue
            if t == "Sorcery":
                self.sorcery = True
                continue
            if t == "Enchantment":
                self.enchantment = True
                continue
            if t == "Artifact":
                self.artifact = True
                continue
            if t == "Land":
                self.land = True
                continue
            if t == "Kindred":
                self.kindred = True
                continue
            raise ValueError(f"No match for type {t}")
    
    def __repr__(self):
        return ', '.join(self.raw)

class SubTypes:
    def __init__(self, sub_types: list):
        pass

class SuperTypes:
    def __init__(self, super_types: list):
        self.raw = super_types
        self.basic = False
        self.legendary = False
        self.snow = False

        for t in self.raw:
            if not t:
                continue
            if t == "Basic":
                self.basic = True
                continue
            if t == "Legendary":
                self.legendary = True
                continue
            if t == "Snow":
                self.snow = True
                continue
            raise ValueError(f"No match for super-type {t}")
    
    def __repr__(self):
        return ', '.join(self.raw)

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

class Card:
    def __init__(self, count: int, name: str, foil: bool, edition: str, number: int, mana_cost: ManaCost, types: list, sub_types: list, super_types: SuperTypes, rarity: str):
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

cards = SortedList(key=lambda x: x)

files = glob.glob("data/*.csv")

if len(files) > 1:
    print("More than one file found in data/")
    exit(1)

# Quantity,Name,Finish,Edition Code,Collector Number,Mana cost,Types,Sub-types,Super-types,Rarity
with open(files[0]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            card = Card(
                count=row['Quantity'],
                name=row['Name'],
                foil=(row['Finish'] == "Foil"),
                edition=row['Edition Code'],
                number=row['Collector Number'],
                mana_cost=row['Mana cost'],
                types=row['Types'].split(','),
                sub_types=row['Sub-types'].split(','),
                super_types=row['Super-types'].split(','),
                rarity=row['Rarity']
            )
            cards.add(card)
        except ValueError as e:
            print(f"{row['Name']}: {e}")

for c in cards:
    print(f"{c.name}: {c.rarity}")