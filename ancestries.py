import json
import nethysdb

class Ancestry(nethysdb.NethysDB):
    def __init__(self, link, SourceBook, Page, description, YouMight, OthersProbably, PhysicalDescription, Society, AlignmentAndReligion, Adventurers, Names, Hitpoints, Size, Speed, AbilityBoost1, AbilityBoost2, AbilityFlaw):
        super().__init__(link, SourceBook, Page)
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

list_of_ancestries = []

# append ancestries on the list
for index, ancestry in enumerate(data['ancestries']):
    list_of_ancestries.append(data['ancestries'][index]['race'])


list_of_ancestry_classes = []

def main():
    # build an instance of Ancestry class for each element
    for ancestry in data['ancestries']:
        name = ancestry['race']
        link = ancestry['NethysUrl']
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
        
        name = Ancestry(link, SourceBook, Page, description, YouMight, OthersProbably, PhysicalDescription, Society, AlignmentAndReligion, Adventurers, Names, Hitpoints, Size, Speed, AbilityBoost1, AbilityBoost2, AbilityFlaw)
        print(link)
        # list_of_ancestries.append(ancestry['race'])
        

if __name__ == '__main__':
    main()
    # print(list_of_ancestry_classes)
    