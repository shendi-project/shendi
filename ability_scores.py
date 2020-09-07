import math


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
# using the console to input until someone figures out how buttons works
str_boost = int(input("STR Boost?"))
dex_boost = int(input("DEX Boost?"))
con_boost = int(input("CON Boost?"))
int_boost = int(input("INT Boost?"))
wis_boost = int(input("WIS Boost?"))
cha_boost = int(input("CHA Boost?"))
str_flaw = int(input("STR Flaw?"))
dex_flaw = int(input("DEX Flaw?"))
con_flaw = int(input("CON Flaw?"))
int_flaw = int(input("INT Flaw?"))
wis_flaw = int(input("WIS Flaw?"))
cha_flaw = int(input("CHA Flaw?"))

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
