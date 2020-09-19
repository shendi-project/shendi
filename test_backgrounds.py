import backgrounds


def test_get_boosts():
    assert backgrounds.get_boosts('Acolyte') == ['Intelligence', 'Wisdom']