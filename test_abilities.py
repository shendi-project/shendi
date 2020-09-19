import abilities

def test__repr__():
    # tests if calling abilities.Strength returns a string '10'
    assert abilities.Strength.__repr__() == '10'


def test_getModifier():
    assert abilities.Dexterity.getModifier() == 0


def test_boost():
    abilities.Strength.boost()
    mod = abilities.Strength.getModifier()
    assert mod == 1


def test_flaw():
    abilities.Constitution.flaw()
    mod = abilities.Constitution.getModifier()
    assert mod == -1
