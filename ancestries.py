import json
import nethysdb

class Ancestry(nethysdb.NethysDB):
    def __init__(self, link, SourceBook, Page, name, description, YouMight, OthersProbably, PhysicalDescription, Society, AlignmentAndReligion, Adventurers, Names, Hitpoints, Size, Speed, AbilityBoost1, AbilityBoost2, AbilityFlaw):
        super().__init__(link, SourceBook, Page)
        self.name = name
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

# grab data from JSON, create classes and append ancestries on the list
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
    
    name = Ancestry(link, SourceBook, Page, name, description, YouMight, OthersProbably, PhysicalDescription, Society, AlignmentAndReligion, Adventurers, Names, Hitpoints, Size, Speed, AbilityBoost1, AbilityBoost2, AbilityFlaw)
    list_of_ancestries.append(ancestry['race'])


def get_boost(ancestry, n):
    if ancestry in list_of_ancestries:
        index = list_of_ancestries.index(ancestry)
        return data['ancestries'][index]['Ability Boosts'][n]
    else:
        raise Exception("Ancestry not found in the list_of_ancestries")


def get_flaw(ancestry, n):
    if ancestry in list_of_ancestries:
        index = list_of_ancestries.index(ancestry)
        return data['ancestries'][index]['Ability Flaw'][n]
    else:
        raise Exception("Ancestry not found in the list_of_ancestries")


def main():
    print(list_of_ancestries)      


if __name__ == '__main__':
    main()