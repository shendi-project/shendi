import csv


def ancestry_boosts(ancestry, str_boost, dex_boost, con_boost, int_boost, wis_boost, cha_boost):
    # open the ancestries file, reminder to fill that one
    with open('data/ancestries.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # matches the ancestry you typed with the correct one in the ancestries file
            if ancestry == row["race"]:
                # for now it just cares about boosts and flaws, will make the rest latter
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
    if third_boost == 'free':
        third_boost = input("What do you want to do with your free boost?")
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


def ancestry_flaws(ancestry, str_flaw, dex_flaw, con_flaw, int_flaw, wis_flaw, cha_flaw):
    # open the ancestries file, reminder to fill that one
    with open('data/ancestries.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # matches the ancestry you typed with the correct one in the ancestries file
            if ancestry == row["race"]:
                # for now it just cares about boosts and flaws, will make the rest latter
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
