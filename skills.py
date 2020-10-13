import abilities

# Coded variables to test main.py
char_level = 1
acrobatics_mod = abilities.Dexterity.getModifier()
arcana_mod = abilities.Intelligence.getModifier()
athletics_mod = abilities.Strength.getModifier()
crafting_mod = abilities.Intelligence.getModifier()
deception_mod = abilities.Charisma.getModifier()
diplomacy_mod = abilities.Charisma.getModifier()
intimidation_mod = abilities.Charisma.getModifier()
medicine_mod = abilities.Wisdom.getModifier()
nature_mod = abilities.Wisdom.getModifier()
occultism_mod = abilities.Intelligence.getModifier()
performance_mod = abilities.Charisma.getModifier()
religion_mod = abilities.Wisdom.getModifier()
society_mod = abilities.Intelligence.getModifier()
stealth_mod = abilities.Dexterity.getModifier()
survival_mod = abilities.Wisdom.getModifier()
thievery_mod = abilities.Dexterity.getModifier()

perception_mod = abilities.Wisdom.getModifier()

acrobatics_proficiency = "trained"
arcana_proficiency = "untrained"
athletics_proficiency = "master"
crafting_proficiency = "legendary"
deception_proficiency = "trained"
diplomacy_proficiency = "trained"
intimidation_proficiency = "master"
medicine_proficiency = "trained"
nature_proficiency = "trained"
occultism_proficiency = "trained"
performance_proficiency = "untrained"
religion_proficiency = "trained"
society_proficiency = "trained"
stealth_proficiency = "master"
survival_proficiency = "untrained"
thievery_proficiency = "trained"

perception_proficiency = "trained"

# acrobatics
# arcana
# athletics
# crafting
# deception
# diplomacy
# intimidation
# medicine
# nature
# occultism
# performance
# religion
# society
# stealth
# survival
# thievery


def main():
    # Using the console to input until someone figures out how buttons work.
    char_level = int(input("Enter your character's level: "))

    # Proficiency modifier variables
    untrained = 0
    trained = 2 + char_level
    expert = 4 + char_level
    master = 6 + char_level
    legendary = 8 + char_level

    # Converts user input into a variable I can use to calculate their skill modifier.
    # There's probably a better way to do this.

    def skill_training(skill_prof_input):
        if skill_prof_input == "U":
            skill_prof = untrained
        elif skill_prof_input == "T":
            skill_prof = trained
        elif skill_prof_input == "E":
            skill_prof = expert
        elif skill_prof_input == "M":
            skill_prof = master
        elif skill_prof_input == "L":
            skill_prof = legendary
        else:
            raise Exception("Proficiencyt not selected")
        return skill_prof

    # Using the console to input until someone figures out how buttons work, Electric Boogaloo.
    acrobatics_prof_input = input("Pick Acrobatics proficiency: U | T | E | M | L : ")
    arcana_prof_input = input("Pick Arcana proficiency: U | T | E | M | L : ")
    athletics_prof_input = input("Pick Athletics proficiency: U | T | E | M | L : ")
    crafting_prof_input = input("Pick Crafting proficiency: U | T | E | M | L : ")
    deception_prof_input = input("Pick Deception proficiency: U | T | E | M | L : ")
    diplomacy_prof_input = input("Pick Diplomacy proficiency: U | T | E | M | L : ")
    intimidation_prof_input = input("Pick Intimidation proficiency: U | T | E | M | L : ")
    medicine_prof_input = input("Pick Medicine proficiency: U | T | E | M | L : ")
    nature_prof_input = input("Pick Nature proficiency: U | T | E | M | L : ")
    occultism_prof_input = input("Pick Occultism proficiency: U | T | E | M | L : ")
    performance_prof_input = input("Pick Performance proficiency: U | T | E | M | L : ")
    religion_prof_input = input("Pick Religion proficiency: U | T | E | M | L : ")
    society_prof_input = input("Pick Society proficiency: U | T | E | M | L : ")
    stealth_prof_input = input("Pick Stealth proficiency: U | T | E | M | L : ")
    survival_prof_input = input("Pick Survival proficiency: U | T | E | M | L : ")
    thievery_prof_input = input("Pick Thievery proficiency: U | T | E | M | L : ")

    # Calculating Skill Modifiers.
    acrobatics_mod = abilities.Dexterity.getModifier() + skill_training(acrobatics_prof_input)
    print("Acrobatics Modifier: " + str(acrobatics_mod))
    arcana_mod = abilities.Intelligence.getModifier() + skill_training(arcana_prof_input)
    print("Arcana Modifier: " + str(arcana_mod))
    athletics_mod = abilities.Strength.getModifier() + skill_training(athletics_prof_input)
    print("Athletics Modifier: " + str(athletics_mod))
    crafting_mod = abilities.Intelligence.getModifier() + skill_training(crafting_prof_input)
    print("Crafting Modifier: " + str(crafting_mod))
    deception_mod = abilities.Charisma.getModifier() + skill_training(deception_prof_input)
    print("Deception Modifier: " + str(deception_mod))
    diplomacy_mod = abilities.Charisma.getModifier() + skill_training(diplomacy_prof_input)
    print("Diplomacy Modifier: " + str(diplomacy_mod))
    intimidation_mod = abilities.Charisma.getModifier() + skill_training(intimidation_prof_input)
    print("Intimidation Modifier: " + str(intimidation_mod))
    medicine_mod = abilities.Wisdom.getModifier() + skill_training(medicine_prof_input)
    print("Medicine Modifier: " + str(medicine_mod))
    nature_mod = abilities.Wisdom.getModifier() + skill_training(nature_prof_input)
    print("Nature Modifier: " + str(nature_mod))
    occultism_mod = abilities.Intelligence.getModifier() + skill_training(occultism_prof_input)
    print("Occultism Modifier: " + str(occultism_mod))
    performance_mod = abilities.Charisma.getModifier() + skill_training(performance_prof_input)
    print("Performance Modifier: " + str(performance_mod))
    religion_mod = abilities.Wisdom.getModifier() + skill_training(religion_prof_input)
    print("Religion Modifier: " + str(religion_mod))
    society_mod = abilities.Intelligence.getModifier() + skill_training(society_prof_input)
    print("Society Modifier: " + str(society_mod))
    stealth_mod = abilities.Dexterity.getModifier() + skill_training(stealth_prof_input)
    print("Stealth Modifier: " + str(stealth_mod))
    survival_mod = abilities.Wisdom.getModifier() + skill_training(survival_prof_input)
    print("Survival Modifier: " + str(survival_mod))
    thievery_mod = abilities.Dexterity.getModifier() + skill_training(thievery_prof_input)
    print("Thievery Modifier: " + str(thievery_mod))

    # Item, temporary, and armor bonuses/penalties should be added later.
    # We still need to implement Lore skills.


if __name__ == "__main__":
    main()
