# mtg-bulk-sorter

Take a CSV export from Archidekt and get back the preferred sorting order for bulk storage.

## The Order

### Spells
1. Colour (cost only, not identity)
    1. Mono
    2. [Multi](#multicolour-sorting)
    3. Colourless
2. Type
    1. Creatures
    2. Planeswalkers
    3. Instants
    4. Sorceries
    5. Enchantments
        1. Subtypeless
        2. By Subtype
    6. Artifacts
        1. Subtypeless
        2. By Subtype
3. Rarity
    1. Rare/Mythic/Special
    2. Common/Uncommon
4. Mana Value (Lowest First)
    1. Number of pips (Phyrexian, Regular)
5. Card Name
6. Collector Number
7. Foil, Non-Foil
8. Edition Code

### Non-Basic Lands
1. Colour (by mana produced):
    1. Mono
    2. Colourless
    3. [Multi](#multicolour-sorting)
        1. Any
        2. Specific + Any
            - WUBRG of specific
        3. Specific colours
            - WUBRG of specific
2. Rarity: Rare/Mythic, Common/Uncommon
3. Card Name
4. Collector Number
5. Foil, Non-Foil
6. Edition Code

### Basic Lands
1. Type (Plains, Island, Swamp, Mountain, Forest)
2. Full Art, Regular Art
3. Artist (Alphabetical as written)
4. Art
5. Collector Number
6. Foil, Non-Foil
7. Edition Code

## Sorting Notes

### Multicolour Sorting
1. Number of Colours
2. Colours

e.g.
- ⚪🔵, ⚪⚫, ...
- 🔵⚫, 🔵🔴, ...
- ...
- ⚪🔵⚫, ⚪🔵🔴, ..., ⚪⚫🔴, ⚪⚫🟢, ⚪🔴🟢
- 🔵⚫🔴, ...
- ...
- ⚪🔵⚫🔴, ⚪🔵⚫🟢, ⚪🔵🔴🟢, ⚪⚫🔴🟢
