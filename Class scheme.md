# Shendi

For the time being, I have these objectives before I hit the alpha, beta or pre-release versions (I'll decide that later).

### Upcoming development:
- Importing and exporting PF2 characters.
- Manage homebrew content.
- Able to generate PC of level 1
- Export character in .Shendi format
- Export fillable pdf.
- Realtime editable buttons and selections


### Later, after alpha:
- Level up

Questions:

* I'm not sure to create classes for everything, (for example for each Trigger, Cast(Somatic, Verbal and Material). They seem very specific.
* Actions might be useful to define normal (123 actions, reactions, free actions) and especial actions (skill actions, support, raise shield, etc)
* I could put an optional variable to receive the critical success, failure, etc
* How can I put the information that can only store certain values? (for example *maybe with enumerators*
> (chaotic, neutral, lawful, good, evil)

> (untrained, trained, expert, master, legendary) 

> (Tiny, Small, Medium, Large, etc) 

> (rarity: common, uncommon, rare, legendary) ? 

> (Saving Throws)

> (*Languages? Maybe?*)

* Bonus and Penalties?
* Class Proficiencies: how can I operate the proficiencies? (perception, Saving Throws, Skills, Attacks, Defenses, Class DC)
* Class Features: Can I get any help here? Might be a especial class for "class features(NethysDB)
* What about temporary hitpoints? should be a different type of hitpoints, stored on a different pool of HPs?
* Does the class Character have a character sheet or is it a different object? (like, a different file on the OS)

### Leftovers
* Attack. I'm not doing a class for it, nor it needs nothing especial
* Rounds. It's not a combat app yet.

### Things to investigate
* Why spell.json has a "source" and "components" but they are equal?

---
# Random Methods or Functions, or things that don't need a Class
* SpellAttackRoll(AbilityModifier, ProficiencyBonus, otherBonuses, penalties) = int
* SpellDC(AbilityModifier, ProficiencyBonus, , otherBonuses, penalties) = int 
* roll Initiative(skill): int
* Alignment = is_it_good evil neutral chaotic lawful?
* AC Value

---


# Structure

## Name of a class (Parent class *-if any-*)
* variables of that class: data type
> method

---

# Classes:
(Following [this list](https://2e.aonprd.com/Rules.aspx?ID=15))

## Player
- Name (or nickname)

## Character
- name
- level

## NethysDB
- NethysURL
- Source book
- Source book page

## Trait(NethysDB):
- description
- type (untyped, Monster, Equipment, etc)

## Action
- name
- Quantity? maybe?

## Trigger
- description

## Ability Score(NethysDB)
- name
- number
> modifier

> boost

>  flaw

## Language
- name

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
- *AbilityBoosts & Flaws?*
- *Optional Languages?*
- *Especial race features?*

--- 
> A ver, los ability boosts se tienen que almacenar en algun lado, 

> Y luego yo los elijo

> Para pasar a ser métodos de class: Ability

> Pero como los sumo? y como restrinjo los existentes?
> Tengo 3 casos de Abi boost
> * Te doy un abi boost en X caracteristica
> * Te doy a elegir un abiboost entre estas [] caracteristicas

> Además, un abiboost tiene una lista en la cual vos podés elegir (luego corres una funcion para verificar que todo ande bien.)
 
 
---



## Background(NethysDB)
- Name
- Description
- AbilityBoosts
- TrainedSkills
- TrainedLores
- Free(Skill)Feat

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
> Proficiencies
> Class Features

## Animal Companions(NethysDB)
- Name (I mean race, or type of animal)
- Nickname (the name you put it to your ~~pokemon~~ pet)
(size, abilities, melee actions, ranged actions, damage, hitpoints, proficient skills, Senses, Speed, especial abilities, Advanced Maneuver)

## Familiars(NethysDB)
> Etc

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
- Spoilers: boolean
(especial traits for each skill feat, so you can filter general feats for each skill)

## HitPoints
- Maximum
- Current
- Temporary?
+ Damage
+ Heal


## Skills(NethysDB)
- Name
- Key Ability

## Spell(NethysDB)
- name
- type(Focus, Ritual, Spell, ¿Cantrip?)
- Level
- Cast (Somatic, verbal, Material)
- range
- targets
- duration
- description

---

## Proficiency(NethysDB)
- name
