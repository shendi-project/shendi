import math
import ancestry


# Define all them functions
# Ability Modifier function
def mod_calc(number):
    modifier = math.floor((number - 10) / 2)
    return modifier


# Boost function
def boost(ability):
    if ability < 18:
        ability = ability + 2
    else:
        ability = ability + 1
    return ability


# Flaws function
def flaw(ability):
    ability = ability - 2
    return ability


# Ability modifiers starts at 10
str_ability = 10
dex_ability = 10
con_ability = 10
int_ability = 10
wis_ability = 10
cha_ability = 10
# define the boosts and flaws functions so it doesn't bothers the IDE
global str_boost, dex_boost, con_boost, int_boost, wis_boost, cha_boost
global str_flaw, dex_flaw, con_flaw, int_flaw, wis_flaw, cha_flaw


def main():
    global str_ability, dex_ability, con_ability, int_ability, wis_ability, cha_ability
    global str_boost, dex_boost, con_boost, int_boost, wis_boost, cha_boost
    global str_flaw, dex_flaw, con_flaw, int_flaw, wis_flaw, cha_flaw
    # ask for ancestry, reminder to make a button latter
    race = input("What are you?")
    str_boost, dex_boost, con_boost, int_boost, wis_boost, cha_boost = ancestry.ancestry_boosts(race)
    str_flaw, dex_flaw, con_flaw, int_flaw, wis_flaw, cha_flaw = ancestry.ancestry_flaws(race)

    # Calculates final Ability Score
    while str_boost > 0:
        str_ability = boost(str_ability)
        str_boost = str_boost - 1
    while str_flaw > 0:
        str_ability = flaw(str_ability)
        str_flaw = str_flaw - 1
    while dex_boost > 0:
        dex_ability = boost(dex_ability)
        dex_boost = dex_boost - 1
    while dex_flaw > 0:
        dex_ability = flaw(dex_ability)
        dex_flaw = dex_flaw - 1
    while con_boost > 0:
        con_ability = boost(con_ability)
        con_boost = con_boost - 1
    while con_flaw > 0:
        con_ability = flaw(con_ability)
        con_flaw = con_flaw - 1
    while int_boost > 0:
        int_ability = boost(int_ability)
        int_boost = int_boost - 1
    while int_flaw > 0:
        int_ability = flaw(int_ability)
        int_flaw = int_flaw - 1
    while wis_boost > 0:
        wis_ability = boost(wis_ability)
        wis_boost = wis_boost - 1
    while wis_flaw > 0:
        wis_ability = flaw(wis_ability)
        wis_flaw = wis_flaw - 1
    while cha_boost > 0:
        cha_ability = boost(cha_ability)
        cha_boost = cha_boost - 1
    while cha_flaw > 0:
        cha_ability = flaw(cha_ability)
        cha_flaw = cha_flaw - 1

    # Calculates the modifier and print both score and modifier to console
    str_mod = mod_calc(str_ability)
    print(str_ability, str_mod)
    dex_mod = mod_calc(dex_ability)
    print(dex_ability, dex_mod)
    con_mod = mod_calc(con_ability)
    print(con_ability, con_mod)
    int_mod = mod_calc(int_ability)
    print(int_ability, int_mod)
    wis_mod = mod_calc(wis_ability)
    print(wis_ability, wis_mod)
    cha_mod = mod_calc(cha_ability)
    print(cha_ability, cha_mod)


if __name__ == '__main__':
    main()


# values to test main.py

str_ability = 18
dex_ability = 15
con_ability = 14
int_ability = 13
wis_ability = 12
cha_ability = 10

str_mod = mod_calc(str_ability)
dex_mod = mod_calc(dex_ability)
con_mod = mod_calc(con_ability)
int_mod = mod_calc(int_ability)
wis_mod = mod_calc(wis_ability)
cha_mod = mod_calc(cha_ability)
