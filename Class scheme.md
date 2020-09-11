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

* I'm not sure to create classes for everything, (for example for each Action, Trigger, Cast(Somatic, Verbal and Material). They seem very specific.
* I could put an optional variable to receive the critical success, failure, etc
* How can I put the information that can only store certain values? (for example (chaotic, neutral, lawful, good, evil) (untrained, trained, expert, master, legendary) (Tiny, Small, Medium, Large, etc) *maybe with enumerators*? 

### Things to investigate
* Why spell.json has a "source" and "components" but they are equal?

# Structure

## Name of a class (Parent class *-if any-*)
* variables of that class: data type
> method

---

# Classes:
(Following [this list](https://2e.aonprd.com/Rules.aspx?ID=15))
## Character
- name

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

> A ver, los ability boosts se tienen que almacenar en algun lado, 

> Y luego yo los elijo

> Para pasar a ser métodos de class: Ability

> Pero como los sumo? y como restrinjo los existentes?
> Tengo 3 casos de Abi boost
> * Te doy un abi boost en X caracteristica
> * Te doy a elegir un abiboost entre estas [] caracteristicas

> Además, un abiboost tiene una lista en la cual vos podés elegir (luego corres una funcion para verificar que todo ande bien.)
 
 
---

# Thinktank copypasta - nothing decided downhere

## PFclass(NethysDB)

## Feat(NethysDB)
(especial traits for each skill feat, so you can filter general feats for each skill)

## Skills

## Armor class(NethysDB)
- Value


## Proficiency(NethysDB)
- name

## Spell(NethysDB)
- name
- type(Focus, Ritual, Spell, ¿Cantrip?)
- Level
- Cast (Somatic, verbal, Material)
- range
- targets
- duration
- description

## Alingment
> is_it_good

> is_it_evil

> is_it_neutral

> is_it_chaotic

> is_it_lawful


# Random Methods or Functions
* SpellAttackRoll(AbilityModifier, ProficiencyBonus, otherBonuses, penalties) = int
* SpellDC(AbilityModifier, ProficiencyBonus, , otherBonuses, penalties) = int 