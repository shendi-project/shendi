class Hitpoints():
    def __init__(self, maximum, current):
        self.maximum = maximum
        self.current = current

    # actually doesn't return current hitpoints, but the number you enter divided by 2
    def half(current):
        current = current / 2
        return current


class Temporary(Hitpoints):
    pass


# values to test main.py
value = 30

## HitPoints
# + Damage
# > Do resistance goes here?
# + Heal