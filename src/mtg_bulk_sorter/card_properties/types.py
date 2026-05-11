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
