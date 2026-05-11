import random

from hypothesis import given, strategies
from mtg_bulk_sorter.card import Card

cards = [
    Card(name="Creature", types=["Creature"]),
    Card(name="Planeswalker", types=["Planeswalker"]),
    Card(name="Instant", types=["Instant"]),
    Card(name="Sorcery", types=["Sorcery"]),
    Card(name="Enchantment", types=["Enchantment"]),
    Card(name="Artifact", types=["Artifact"])
]


@given(strategies.lists(strategies.sampled_from(cards)))
def test_types(lst):
    shuffled1 = lst[:]
    shuffled2 = lst[:]
    random.shuffle(shuffled1)
    random.shuffle(shuffled2)
    sorted1 = sorted(shuffled1)
    sorted2 = sorted(shuffled2)

    assert sorted1 == sorted2
    assert len(sorted1) == len(sorted2)
