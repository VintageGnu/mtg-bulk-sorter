import argparse
import csv

from sortedcontainers import SortedList

from .card import Card


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='mtg-bulk-sorter',
        description='Take a CSV export from Archidekt and get back the preferred sorting order for bulk storage.'
    )
    parser.add_argument('filename')
    args = parser.parse_args()

    cards = SortedList(key=lambda x: x)

    # Quantity,Name,Finish,Edition Code,Collector Number,Mana cost,Types,Sub-types,Super-types,Rarity
    with open(args.filename) as csvfile:
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
