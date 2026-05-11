# mtg-bulk-sorter

Take a CSV export from Archidekt and get back the preferred sorting order for bulk storage.

[![lint](https://github.com/VintageGnu/mtg-bulk-sorter/actions/workflows/lint.yml/badge.svg?event=push)](https://github.com/VintageGnu/mtg-bulk-sorter/actions/workflows/lint.yml) [![test](https://github.com/VintageGnu/mtg-bulk-sorter/actions/workflows/test.yml/badge.svg?event=push)](https://github.com/VintageGnu/mtg-bulk-sorter/actions/workflows/test.yml)

## The Order

### Spells
1. Rarity
    1. Rare/Mythic/Special
    2. Common/Uncommon
2. Colour (cost only, not identity)
    1. Mono
    2. [Multi](#multicolour-sorting)
    3. Colourless
3. Type
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
4. Mana Value (Lowest First)
    * The idea is to sort by ease of casting so Phyrexian < X < Colourless < Hybrid < Specific Colour
        * Hybrid Phyrexian would be the easiest but hybrid was hard enough to handle so I'll cross that bridge when I need to 😭
5. Card Name
6. Collector Number
7. Foil, Non-Foil
8. Edition Code

### Non-Basic Lands
1. Rarity: Rare/Mythic, Common/Uncommon
2. Colour (by mana produced):
    1. Mono
    2. Colourless
    3. [Multi](#multicolour-sorting)
        1. Any
        2. Specific + Any
            - WUBRG of specific
        3. Specific colours
            - WUBRG of specific
3. Card Name
4. Collector Number
5. Foil, Non-Foil
6. Edition Code

### Basic Lands
1. Type (Plains, Island, Swamp, Mountain, Forest)
2. Full Art, Regular Art
3. Foil, Non-Foil
4. Artist (Alphabetical as written)
5. Art
6. Collector Number
7. Edition Code

### Tokens
I haven't actually loaded these into Archidekt, but the sorting is here for completeness.

1. Sidedness
    1. Single Sided
    2. Double Sided
        * Use the side with the name that is first alphabetically as the front.
2. Type
    1. Generic Creatures
    2. Offspring
    3. Artifacts
    4. Emblems
4. Name
5. Art

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

## Sleeves
All cards are sleeved in penny sleeves, except:
* Basic lands (unless foil or full art)
* Tokens (unless foil)

## Usage
For now just run with uv directly:  
`uv run mtg-bulk-sorter path/to/export.csv`

TODO: Create TUI and/or self-contained executable.

## Tests (WIP)
`uv run pytest`
