import argparse
import csv

from sortedcontainers import SortedList

from .card import Card
from .mana_colour import ManaColour


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='mtg-bulk-sorter',
        description='Take a CSV export from Archidekt and get back the preferred sorting order for bulk storage.'
    )
    parser.add_argument('filename')
    args = parser.parse_args()

    cards = SortedList(key=lambda x: x)

    errors = False
    # Quantity,Name,Finish,Edition Code,Collector Number,Mana cost,Types,Sub-types,Super-types,Rarity
    with open(args.filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Skip art cards
                if "Card" in row['Types']:
                    continue
                card = Card(
                    count=row['Quantity'],
                    name=row['Name'],
                    foil=(row['Finish'] == "Foil"),
                    edition=row['Edition Code'],
                    number=row['Collector Number'],
                    mana_cost=row['Mana cost'],
                    types=row['Types'].split(','),
                    subtypes=row['Sub-types'].split(','),
                    supertypes=row['Super-types'].split(','),
                    rarity=row['Rarity']
                )
                cards.add(card)
            except ValueError as e:
                errors = True
                print(f"{e}")
                print(f"{row}")
                print("")

    if not errors:
        for card in cards:
            s = f"{"* " if card.multicoloured() else ""}"
            s += f"{card.name} {card.mana_cost.raw}: "
            if card.mana_cost.colours == ManaColour.NONE:
                s += "NONE"
            else:
                s += f"{"|".join([colour.name for colour in card.mana_cost.colours])}"
            print(s)
