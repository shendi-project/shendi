import json
import nethysdb

class Background(nethysdb.NethysDB):
    def __init__(self, link, sourcebook, page, name, traits, description, ability_boost1, ability_boost2, trained_skill, additional_lore, feat):
        super().__init__(link, sourcebook, page)
        self.name = name
        self.traits = traits
        self.description = description
        self.ability_boost1 = ability_boost1
        self.ability_boost2 = ability_boost2
        self.trained_skill = trained_skill
        self.additional_lore = additional_lore
        self.feat = feat


with open('data/backgrounds.json') as f:
    data = json.load(f)

list_of_backgrounds = []

for background in data['backgrounds']:
    link = background['NethysUrl']
    sourcebook = background['Source']
    page = background['Page']
    name = background['Background']
    traits = background['Traits']
    description = background['Description']
    ability_boost1 = background['Ability Boost'][0]
    ability_boost2 = background['Ability Boost'][1]
    trained_skill = background['TrainedSkill']
    additional_lore = background['AdditionalLore']
    feat = background['Feat']

    name = Background(link, sourcebook, page, name, traits, description, ability_boost1, ability_boost2, trained_skill, additional_lore, feat)
    list_of_backgrounds.append(name.name)

if __name__ == "__main__":
    print(list_of_backgrounds)
