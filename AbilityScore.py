import NethysDB

class AbilityScore(NethysDB):
    def __init__(self, name, number):
        self.name = name
        self.number = number
    

    def getModifier(self):
        return self