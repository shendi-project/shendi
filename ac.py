class AC:
    def __init__(self, value):
        self.value = value
    
    def raiseShield(self):
        self.value = self.value + 2
        return self.value
    
    def lowerShield(self):
        self.value = self.value - 2
        return self.value

# values to test main.py
value = 16
