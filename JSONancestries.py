import json


with open('data/ancestries.json') as f:
    data = json.load(f)

list_of_races = []

for index, race in enumerate(data):
    list_of_races.append(data[index]['race'])

# for race in data:
#     print(da)

def main():
    print(list_of_races)
    print(list_of_races[0])
    print(list_of_races[1])

if __name__ == '__main__':
    main()


