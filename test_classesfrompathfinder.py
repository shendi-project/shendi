import classesfrompathfinder


def test_list_of_classes():
    assert classesfrompathfinder.list_of_classes == ['Alchemist', 'Barbarian']


def test_get_key_ability():
    assert classesfrompathfinder.get_key_ability('Alchemist') == ['Intelligence']
    