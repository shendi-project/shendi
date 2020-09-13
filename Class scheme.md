# Shendi Class Scheme

---------------------------------------------------------------------------
# Questions:

* Class Features: Can I get any help here? Might be a especial class for "class features(NethysDB)

### Things to investigate
* Why spell.json has a "source" and "components" but they are equal?

---------------------------------------------------------------------------

# Structure

## Name of a class (Parent class *-if any-*)
* variables of that class: data type
+ method

---------------------------------------------------------------------------

# Classes:
(Following [this list](https://2e.aonprd.com/Rules.aspx?ID=15))


## NethysDB
- NethysURL
- Source book
- Source book page

## AC
- value
+ various methods
+ raiseShield()
+ lowerShield()
+ flatfooted()

## Action(NethysDB)
- name
- Description
- Quantity of actions/reaction/free action (this should be a subtype of an action enumerator class)

## Ability Score(NethysDB)
- name
- number
+ modifier


## ((enumeration)) Alignment
Lawful Good

Neutral Good

Chaotic Good

Lawful Neutral

True Neutral

Chaotic Neutral

Lawful Evil

Neutral Evil

Chaotic Evil

+ Is it("lawful", object) for each alignment

## Ancestry(NethysDB)
- name: str
- description: str
- YouMight: list of strings
- OthersProbably: list of strings
- PhysicalDescription: str
- Society: str
- AlignmentAndReligion: str
- Adventurers
- Names: dict of strings, male and female
- Hitpoints: int
- speed: int
- AbilityBoosts1:
- AbilityBoosts2:
- AbilityFlaw:
- *Optional Languages?*
- *Especial race features?*


## Background(NethysDB)
- Name
- Description
- AbilityBoost1
- TrainedSkills
- TrainedLores
- Free(Skill)Feat


## PlayerCharacter
- name
- level
- ClassDC: int (it's here because some classes have options to have either X or Y ability modifier, so it's a thing of a character, not of a PF2_Class)

+ boost
+ flaw
+ SpellAttackRoll(AbilityModifier, ProficiencyBonus, otherBonuses, penalties) = int (Idk if this goes into PF2_class or into character)
+ SpellDC(AbilityModifier, ProficiencyBonus, otherBonuses, penalties) = int 
+ exportFile()
+ exportFillablePDF()
+ exportRoll20()

## PF2_Class(NethysDB)
- Name
- Description
- KeyAbility
- Hitpoints
- During Combat Encounters...
- During Social Encounters...
- While Exploring...
- In Downtime...
- YouMight: list of strings
- OthersProbably: list of strings
> Class Features


## ((Enumerator)) CastComponents
Somatic

Verbal

Material

## Condition(NethysDB)
- Name
- Description
- Group(Optional) {Attitudes, Death and Dying, Degree of Detection, Lowered Abilities, Senses}

## Coin
-Name
-Value in gold coins
> Any methods required?

## Feat(NethysDB)
- Name
- Level
- Prerequisites
- Benefits
- Trigger
- Spoilers: boolean
(especial traits for each skill feat, so you can filter general feats for each skill)

## HeroPoints(NethysDB)
- Maximum
- Current

## HitPoints
- Maximum
- Current
> Temporary hitpoints?
+ Half()
+ Damage
> Do resistance goes here?
+ Heal

## ((enumeration)) Language
- names of languages

## Player
- Name (or nickname)

## ((Enumeration)) Proficiency
untrained

trained

expert

master

legendary

## ((enumeration)) Rarity
common

uncommon

rare

legendary 

## ((enumeration)) Saving Throw
Fortitude

Reflex

Will

## ((enumeration)) Size
Tiny

Small

Medium

Large

Huge

Gargantuan

## Skill(NethysDB)
- Name
- Key Ability

## Spell(NethysDB)
- name
- type(Focus, Ritual, Spell, ¿Cantrip?) <this should be another enum>
- Level
- action?
- trigger
- range
- targets
- duration
- description

## ((Enumerator)) TraitType:
- name

## ((Enumerator)) Trait(NethysDB, Type Trait):
- name
- description
