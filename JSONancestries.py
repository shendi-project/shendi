import json


with open('data/ancestries.json') as f:
    data = json.load(f)

list_of_races = []

for index, race in enumerate(data):
    list_of_races.append(data[index]['race'])


print(list_of_races)
