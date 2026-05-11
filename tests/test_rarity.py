import random

from hypothesis import given, strategies
from mtg_bulk_sorter.card import Card

cards = [
    Card(name="Common", rarity="common"),
    Card(name="Uncommon", rarity="uncommon"),
    Card(name="Rare", rarity="rare"),
    Card(name="Mythic", rarity="mythic"),
    Card(name="Special", rarity="special")
]


@given(strategies.lists(strategies.sampled_from(cards)))
def test_rarity(lst):
    shuffled1 = lst[:]
    shuffled2 = lst[:]
    random.shuffle(shuffled1)
    random.shuffle(shuffled2)
    sorted1 = sorted(shuffled1)
    sorted2 = sorted(shuffled2)

    assert sorted1 == sorted2
    assert len(sorted1) == len(sorted2)
