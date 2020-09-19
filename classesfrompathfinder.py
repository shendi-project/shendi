import json

with open('data/classes.json') as f:
    data = json.load(f)

list_of_classes = []

for book_class in data['classes']:
    name = book_class['Name']
    list_of_classes.append(name)


def get_key_ability(PC_class):
    if PC_class in list_of_classes:
        index = list_of_classes.index(PC_class)
        return data['classes'][index]['Key Ability']


if __name__ == "__main__":
    print(list_of_classes)
    get_key_ability('Alchemist')