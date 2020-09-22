import ancestries

def test_list_of_ancestries():
    assert ancestries.list_of_ancestries == ['Dwarf', 'Elf']

def test_get_boost():
    assert ancestries.get_boosts('Dwarf') == ['Constitution', 'Wisdom']
    assert ancestries.get_boosts('Elf') == ['Dexterity', 'Intelligence']


def test_get_flaw():
    assert ancestries.get_flaw('Dwarf', 0) == 'Charisma'

