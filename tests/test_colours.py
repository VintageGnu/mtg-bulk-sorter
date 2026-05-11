import random

from hypothesis import given, strategies
from mtg_bulk_sorter.card import Card

cards = [
    Card(name="White", mana_cost="{W}"),
    Card(name="Blue", mana_cost="{U}"),
    Card(name="Black", mana_cost="{B}"),
    Card(name="Red", mana_cost="{R}"),
    Card(name="Green", mana_cost="{G}"),
    Card(name="Azorius", mana_cost="{W}{U}"),
    Card(name="Orzhov", mana_cost="{W}{B}"),
    Card(name="Boros", mana_cost="{W}{R}"),
    Card(name="Selesnya", mana_cost="{W}{G}"),
    Card(name="Dimir", mana_cost="{U}{B}"),
    Card(name="Izzet", mana_cost="{U}{R}"),
    Card(name="Simic", mana_cost="{U}{G}"),
    Card(name="Rakdos", mana_cost="{B}{R}"),
    Card(name="Golgari", mana_cost="{B}{G}"),
    Card(name="Gruul", mana_cost="{R}{G}"),
    Card(name="Esper", mana_cost="{W}{U}{B}"),
    Card(name="Jeskai", mana_cost="{W}{U}{R}"),
    Card(name="Bant", mana_cost="{W}{U}{G}"),
    Card(name="Mardu", mana_cost="{W}{B}{R}"),
    Card(name="Abzan", mana_cost="{W}{B}{G}"),
    Card(name="Naya", mana_cost="{W}{R}{G}"),
    Card(name="Grixis", mana_cost="{U}{B}{R}"),
    Card(name="Sultai", mana_cost="{U}{B}{G}"),
    Card(name="Temur", mana_cost="{U}{R}{G}"),
    Card(name="Jund", mana_cost="{B}{R}{G}"),
    Card(name="Artifice", mana_cost="{W}{U}{B}{R}"),
    Card(name="Growth", mana_cost="{W}{U}{B}{G}"),
    Card(name="Altruism", mana_cost="{W}{U}{R}{G}"),
    Card(name="Aggression", mana_cost="{W}{B}{R}{G}"),
    Card(name="Chaos", mana_cost="{U}{B}{R}{G}"),
    Card(name="WUBRG", mana_cost="{W}{U}{B}{R}{G}")
]


@given(strategies.lists(strategies.sampled_from(cards)))
def test_colours(lst):
    shuffled1 = lst[:]
    shuffled2 = lst[:]
    random.shuffle(shuffled1)
    random.shuffle(shuffled2)
    sorted1 = sorted(shuffled1)
    sorted2 = sorted(shuffled2)

    assert sorted1 == sorted2
    assert len(sorted1) == len(sorted2)
