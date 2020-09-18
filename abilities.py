import nethysdb
import math

class AbilityScore(nethysdb.NethysDB):
    def __init__(self, link, SourceBook, Page, score):
        super().__init__(link, SourceBook, Page)
        self.score = score
    

    def __repr__(self) -> int:
        # TODO: idk why requests as a string, it should be an integer
        """Returns the score of the function as a string

        Returns:
            int: score of the ability (12, 14, 18)
        """
        return str(self.score)

    def getModifier(self):
        # TODO: Test every modifier
        modifier = math.floor((self.score - 10) / 2)
        return modifier


    def boost(self):
        if self.score < 18:
            self.score = self.score + 2
        else:
            self.score = self.score + 1


    def flaw(self):
        self.score = self.score - 2


# Starting ability scores
Strength = AbilityScore("https://2e.aonprd.com/Rules.aspx?ID=68", "Core RuleBook", 19, 10)
Dexterity = AbilityScore("https://2e.aonprd.com/Rules.aspx?ID=69", "Core RuleBook", 19, 10)
Constitution = AbilityScore("https://2e.aonprd.com/Rules.aspx?ID=70", "Core RuleBook", 19, 10)
Intelligence = AbilityScore("https://2e.aonprd.com/Rules.aspx?ID=71", "Core RuleBook", 19, 10)
Wisdom = AbilityScore("https://2e.aonprd.com/Rules.aspx?ID=72", "Core RuleBook", 19, 10)
Charisma = AbilityScore("https://2e.aonprd.com/Rules.aspx?ID=73", "Core RuleBook", 19, 10)
