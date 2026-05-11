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
