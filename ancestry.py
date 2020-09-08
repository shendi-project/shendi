import csv
# this is so pycharm doesn't freaks out
global third_boost


def ancestry_boosts(ancestry):
    # boosts start at 0
    global third_boost
    str_boost = 0
    dex_boost = 0
    con_boost = 0
    int_boost = 0
    wis_boost = 0
    cha_boost = 0
    # open the ancestries file, reminder to fill that one
    with open('data/ancestries.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # matches the ancestry you typed with the correct one in the ancestries file
            if ancestry == row["race"]:
                first_boost = row["first boost"]
                second_boost = row["second boost"]
                third_boost = row["third boost"]
    # just add a +1 if you have the correct boost
    if first_boost == 'str':
        str_boost += 1
    if first_boost == 'dex':
        dex_boost += 1
    if first_boost == 'con':
        con_boost += 1
    if first_boost == 'int':
        int_boost += 1
    if first_boost == 'wis':
        wis_boost += 1
    if first_boost == 'cha':
        cha_boost += 1
    if second_boost == 'str':
        str_boost += 1
    if second_boost == 'dex':
        dex_boost += 1
    if second_boost == 'con':
        con_boost += 1
    if second_boost == 'int':
        int_boost += 1
    if second_boost == 'wis':
        wis_boost += 1
    if second_boost == 'cha':
        cha_boost += 1

    # the third boost, if it exists, is always a free one, this also needs a button
    while third_boost == 'free':
        third_boost = input("What do you want to do with your free boost?")
        # you should only have one ancestry boost for each ability
        if third_boost == first_boost or third_boost == second_boost:
            print("You already have an ancestry boost in that ability score!")
            third_boost = 'free'
    if third_boost == 'str':
        str_boost += 1
    if third_boost == 'dex':
        dex_boost += 1
    if third_boost == 'con':
        con_boost += 1
    if third_boost == 'int':
        int_boost += 1
    if third_boost == 'wis':
        wis_boost += 1
    if third_boost == 'cha':
        cha_boost += 1
    # return the calculated boosts
    return [str_boost, dex_boost, con_boost, int_boost, wis_boost, cha_boost]


def ancestry_flaws(ancestry):
    # flaws start at 0
    str_flaw = 0
    dex_flaw = 0
    con_flaw = 0
    int_flaw = 0
    wis_flaw = 0
    cha_flaw = 0
    # open the ancestries file, reminder to fill that one
    with open('data/ancestries.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # matches the ancestry you typed with the correct one in the ancestries file
            if ancestry == row["race"]:
                flaw = row["ability flaw"]
    # just add a +1 if you have the correct flaws
    if flaw == 'str':
        str_flaw += 1
    if flaw == 'dex':
        dex_flaw += 1
    if flaw == 'con':
        con_flaw += 1
    if flaw == 'int':
        int_flaw += 1
    if flaw == 'wis':
        wis_flaw += 1
    if flaw == 'cha':
        cha_flaw += 1
    # return the calculated flaws
    return [str_flaw, dex_flaw, con_flaw, int_flaw, wis_flaw, cha_flaw]


def ancestry_misc(ancestry):
    # base senses, ancestries can modify this
    senses = ['Vague Hearing', 'Vague Scent', 'Precise Vision']
    with open('data/ancestries.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # matches the ancestry you typed with the correct one in the ancestries file
            if ancestry == row["race"]:
                hit_points = int(row["hit points"])
                speed = int(row["speed"])
                traits = [row["first trait"], row["second trait"]]
                if row["vision"] == "low-vision":
                    senses[2] = "Precise Low-Light Vision"
                if row["vision"] == "darkvision":
                    senses[2] = "Precise Darkvision"
                languages = [row["first language"], row["second language"]]
                if row["third language"] != 'none':
                    languages.append(row["third language"])
    return hit_points, speed, traits, senses, languages


# ancestry_misc test
print(ancestry_misc("Dwarf"))
print(ancestry_misc("Elf"))
print(ancestry_misc("Gnome"))
