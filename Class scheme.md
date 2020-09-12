# Shendi

For the time being, I have these objectives.

### Upcoming development - Alpha stage:
- Able to generate PC of level 1
- Realtime editable buttons and selections
- Export character in .Shendi format
- Export fillable pdf.
- Manage homebrew content.

### Beta Stage:
- Level up
- Parse Nethys and load up all the data

### After 1.0 Release:
- Animal Companions and familiars
- Monsters
> #### Animal Companions(NethysDB)
> - Name (I mean race, or type of animal)
> - Nickname (the name you put it to your ~~pokemon~~ pet)
> - (size, abilities, melee actions, ranged actions, damage, hitpoints, proficient skills, Senses, Speed, especial abilities, Advanced Maneuver)
> #### Familiars(NethysDB)
> 
- PlayMode
> - Actions will have a boolean to know if the skill-action can be used trained/untrained
> - Build an enumerator / optional variable to receive the critical success, success failure and critical failure. So I can jump up or down depending on the number rolled. 
> - Bonuses and penalties, 4 boxes for each, and pick the highest or lowest possible. (Although it would be cool to show it or pick one of the available list)
> * Attacks
> * Rounds and turns (It's not a combat app yet)
> * roll Initiative(skill): int

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
- size (might be a class?)
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

## Skills(NethysDB)
- Name
- Key Ability

## Spell(NethysDB)
- name
- type(Focus, Ritual, Spell, ¿Cantrip?) <this should be another enum>
- Level
- Cast (Somatic, verbal, Material) <this should be another enum>
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
