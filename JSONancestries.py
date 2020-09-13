import json
import NethysDB

class Ancestry(NethysDB.NethysDB):
    def __init__(self, name, NethysUrl, Source, Page, description, YouMight, OthersProbably, PhysicalDescription, Society, AlignmentAndReligion, Adventurers, Names, Hitpoints, Size, Speed, AbilityBoost1, AbilityBoost2, AbilityFlaw):
        self.name = name
        # self.NethysURL = NethysUrl
        # self.SourceBook = Source
        # self.Page = Page
        self.description = description
        self.YouMight = YouMight
        self.OthersProbably = OthersProbably
        self.PhysicalDescription = PhysicalDescription
        self.Society = Society
        self.AlignmentAndReligion = AlignmentAndReligion
        self.Adventurers = Adventurers
        self.Names = Names
        self.Hitpoints = Hitpoints
        self.Size = Size
        self.Speed = Speed
        self.AbilityBoost1 = AbilityBoost1
        self.AbilityBoost2 = AbilityBoost2
        self.AbilityFlaw = AbilityFlaw


with open('data/ancestries.json') as f:
    data = json.load(f)

list_of_races = []

# append races on the list
for index, ancestry in enumerate(data['ancestries']):
    list_of_races.append(data['ancestries'][index]['race'])


def main():
    # test print
    # print(list_of_races)
    # print(list_of_races[0])
    # print(list_of_races[1])

    # build an instance of Ancestry class for each element
    for ancestry in data['ancestries']:
        name = ancestry['race']
        NethysURL = ancestry['NethysUrl']
        SourceBook = ancestry['Source']
        Page = ancestry['Page']
        description = ancestry['Description']
        YouMight = ancestry['YouMight']
        OthersProbably = ancestry['OthersProbably']
        PhysicalDescription = ancestry['Physical Description']
        Society = ancestry['Society']
        AlignmentAndReligion = ancestry['Alignment and Religion']
        Adventurers = ancestry['Adventurers']
        Names = ancestry['Names']
        Hitpoints = ancestry['Hit Points']
        Size = ancestry['Size']
        Speed = ancestry['Speed']
        AbilityBoost1 = ancestry['Ability Boosts'][0]
        AbilityBoost2 = ancestry['Ability Boosts'][1]
        AbilityFlaw = ancestry['Ability Flaw'][0]
        # print(ancestry['race'])
        

if __name__ == '__main__':
    main()
