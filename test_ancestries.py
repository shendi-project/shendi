import ancestries

def test_list_of_ancestries():
    assert ancestries.list_of_ancestries == ['Dwarf', 'Elf']
    pass

def test_get_boost():
    assert ancestries.get_boost('Dwarf', 0) == 'Constitution'
    assert ancestries.get_boost('Elf', 1) == 'Intelligence'


def test_get_flaw():
    assert ancestries.get_flaw('Dwarf', 0) == 'Charisma'

