import tkinter as tk
from tkinter import ttk
import menufunctions as mfx
import abilities
import ancestries
import backgrounds
import classesfrompathfinder
import skills
import ac
import hitpoints
import savingthrow

# test with xampp and mysql workbench


root = tk.Tk()
root.title('shendi - Pathfinder 2nd Edition Character Builder')
root.config(bg="skyblue")

# The applications will consist on different Frames
# The first frame includes the character name, ancestry, background and class
top_frame = tk.Frame(root, width=200, height=400, bg='yellow')
top_frame.grid(row=0, column=0, padx=10, pady=0)
# frame for proficiencies
proficiencies_frame = ttk.Frame(root, width=10, height=10)
proficiencies_frame.grid(row=0, column=1)
# frame for abilities
ability_frame = ttk.Notebook(root, width=200, height=200)
ability_frame.grid(row=1, column=0, padx=10, pady=10)
# frame with a couple of main buttons
mid_frame = ttk.Frame(root, width=50, height=50)
mid_frame.grid(row=1, column=1)
# the bottom frame includes skills
skills_frame = tk.Frame(root, width=200, height=50, bg='green')
skills_frame.grid(row=2, column=0, padx=10, pady=10)
# the lore frame
lore_frame = tk.Frame(root, width=200, height=400, bg='red')
lore_frame.grid(row=3, column=0, padx=10, pady=10)
# feats frame
feats_frame = tk.Frame(root, width=400, height=300)
feats_frame.grid(row=0, column=2, rowspan=3)

# todo: split this huge UI in more manageable files

# --------------------------------------------------------- Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Creation of File menu dropdown and items
file_menu = tk.Menu(menu_bar, tearoff=0)  # tear off = 0 deletes a -- line on the menus
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=mfx.open_file)

# Creation of Help menu dropdown and items
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=mfx.show_about)
help_menu.add_command(label="Go to Github repository", command=mfx.go_to_github)


# --------------------------------------------------------- Top application box
# Label for name
tk.Label(top_frame, text="Character name:").grid(row=0, column=0)
pc_name_field = tk.Entry(top_frame, width=30).grid(row=0, column=1)
# label for ancestry
tk.Label(top_frame, text="Character ancestry:").grid(row=1, column=0)
PC_ancestry = tk.StringVar()
available_ancestries = ancestries.list_of_ancestries
drop_ancestries = tk.OptionMenu(top_frame, PC_ancestry, *available_ancestries).grid(row=1, column=1)
# label for background
tk.Label(top_frame, text="Character background:").grid(row=2, column=0)
PC_background = tk.StringVar()
available_backgrounds = backgrounds.list_of_backgrounds
drop_background = tk.OptionMenu(top_frame, PC_background, *available_backgrounds).grid(row=2, column=1)
# label for class
tk.Label(top_frame, text="Character class:").grid(row=3, column=0)
PC_class = tk.StringVar()
available_classes = classesfrompathfinder.list_of_classes
drop_class = tk.OptionMenu(top_frame, PC_class, *available_classes).grid(row=3, column=1)
# Level
tk.Label(top_frame, text="Level:").grid(row=4, column=0)
LevelUpButton = tk.Button(top_frame, text="+", command=mfx.open_file)
LevelUpButton.grid(row=4, column=1, padx=5)
# TODO: <<<<<<<<<<<<<< Level Hardcoded, get the Level.py File or something >>>>>>>>>>
Level = 1
PC_Level = tk.Label(top_frame, text=Level).grid(row=4, column=2)
LevelDowNButton = tk.Button(top_frame, text="-", command=mfx.open_file)
LevelDowNButton.grid(row=4, column=3, padx=5)


# --------------------------------------------------------- Ability frame
# Ability Labels
tk.Label(ability_frame, text="Ability Scores").grid(row=0, column=0, columnspan=3)
tk.Label(ability_frame, text="Strength").grid(row=1, column=0, pady=10)
tk.Label(ability_frame, text="Dexterity").grid(row=2, column=0, pady=10)
tk.Label(ability_frame, text="Constitution").grid(row=3, column=0, pady=10)
tk.Label(ability_frame, text="Intelligence").grid(row=4, column=0, pady=10)
tk.Label(ability_frame, text="Wisdom").grid(row=5, column=0, pady=10)
tk.Label(ability_frame, text="Charisma").grid(row=6, column=0, pady=10)
# Ability scores
STR_score = tk.StringVar()
DEX_score = tk.StringVar()
CON_score = tk.StringVar()
INT_score = tk.StringVar()
WIS_score = tk.StringVar()
CHA_score = tk.StringVar()

STR_score.set(abilities.Strength.score)
DEX_score.set(abilities.Dexterity.score)
CON_score.set(abilities.Constitution.score)
INT_score.set(abilities.Intelligence.score)
WIS_score.set(abilities.Wisdom.score)
CHA_score.set(abilities.Charisma.score)

STR_abi_label = tk.Label(ability_frame, textvariable=STR_score).grid(row=1, column=1, padx=20, pady=10)
DEX_abi_label = tk.Label(ability_frame, textvariable=DEX_score).grid(row=2, column=1, padx=20, pady=10)
CON_abi_label = tk.Label(ability_frame, textvariable=CON_score).grid(row=3, column=1, padx=20, pady=10)
INT_abi_label = tk.Label(ability_frame, textvariable=INT_score).grid(row=4, column=1, padx=20, pady=10)
WIS_abi_label = tk.Label(ability_frame, textvariable=WIS_score).grid(row=5, column=1, padx=20, pady=10)
CHA_abi_label = tk.Label(ability_frame, textvariable=CHA_score).grid(row=6, column=1, padx=20, pady=10)
# Ability mods
STR_mod = tk.StringVar()
DEX_mod = tk.StringVar()
CON_mod = tk.StringVar()
INT_mod = tk.StringVar()
WIS_mod = tk.StringVar()
CHA_mod = tk.StringVar()

STR_mod.set(abilities.Strength.getModifier())
DEX_mod.set(abilities.Dexterity.getModifier())
CON_mod.set(abilities.Constitution.getModifier())
INT_mod.set(abilities.Intelligence.getModifier())
WIS_mod.set(abilities.Wisdom.getModifier())
CHA_mod.set(abilities.Charisma.getModifier())

STR_mod_label = tk.Label(ability_frame, textvariable=STR_mod).grid(row=1, column=2, pady=10)
DEX_mod_label = tk.Label(ability_frame, textvariable=DEX_mod).grid(row=2, column=2, pady=10)
CON_mod_label = tk.Label(ability_frame, textvariable=CON_mod).grid(row=3, column=2, pady=10)
INT_mod_label = tk.Label(ability_frame, textvariable=INT_mod).grid(row=4, column=2, pady=10)
WIS_mod_label = tk.Label(ability_frame, textvariable=WIS_mod).grid(row=5, column=2, pady=10)
CHA_mod_label = tk.Label(ability_frame, textvariable=CHA_mod).grid(row=6, column=2, pady=10)

# Class DC
# TODO: <<<<<<<<<<<<<<<<<<<<<< I don't like how this is showed >>>>>>>>>>
tk.Label(ability_frame, text="Class DC").grid(row=7, column=0)
tk.Label(ability_frame, text="10").grid(row=7, column=1, columnspan=2)

# --------------------------------------------------------- Proficiencies frame
# Labels
tk.Label(proficiencies_frame, text="Proficiencies").grid(row=0, column=0, columnspan=2)
tk.Label(proficiencies_frame, text="Simple Weapons").grid(row=1, column=0)
tk.Label(proficiencies_frame, text="Martial Weapons").grid(row=2, column=0)
tk.Label(proficiencies_frame, text="Unarmed Attacks").grid(row=3, column=0)
# Proficiencies
# TODO: <<<<<<<<<<<<<<<<<<<<<<<<<  proficiencies hardcoded here!!!! >>>>>>>>>>>
tk.Label(proficiencies_frame, text="Trained").grid(row=1, column=1, padx=10)
tk.Label(proficiencies_frame, text="Expert").grid(row=2, column=1, padx=10)
tk.Label(proficiencies_frame, text="Master").grid(row=3, column=1, padx=10)


def select_abi_boost():
    abi_free_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    # global drop_ancestry_free1, drop_background_free, drop_class_boost
    # Grabs the dropdown menu on the main window
    get_ancestry = PC_ancestry.get()  # TODO: exception when no ancestry is selected
    get_background = PC_background.get()
    get_class = PC_class.get()

    # Create a new window
    select_abi_window = tk.Toplevel()
    tk.Label(select_abi_window, text="Pick every ability boost from each origin").grid(row=0, column=0)

    # ----- Ancestry group
    ancestry_group = tk.LabelFrame(select_abi_window, text="Ancestry")
    ancestry_group.grid(row=1, column=0)
    # BUG: apparently you cant use .grid on a LabelFrame after a defintion, you need to set it on another line
    PC_ancestry_boosts = ancestries.get_boosts(get_ancestry)
    PC_ancestry_flaw = ancestries.get_flaw(get_ancestry, 0)
    tk.Label(ancestry_group, text=PC_ancestry_boosts[0]).grid(row=0, column=0)
    tk.Label(ancestry_group, text=PC_ancestry_boosts[1]).grid(row=1, column=0)
    tk.Label(ancestry_group, text=PC_ancestry_flaw, fg="Red").grid(row=0, column=1)
    PC_ancestry_free1 = tk.StringVar()
    tk.OptionMenu(ancestry_group, PC_ancestry_free1, *abi_free_list).grid(row=0, column=2)

    # Added function for the Human Ancestry
    def add_free_boost():
        PC_ancestry_free2 = tk.StringVar()
        drop_ancestry_free2 = tk.OptionMenu(ancestry_group, PC_ancestry_free2, *abi_free_list)
        drop_ancestry_free2.grid(row=1, column=2)

    if PC_ancestry == "Human":
        add_free_boost()
    else:
        pass

    # ----- Background group
    background_group = tk.LabelFrame(select_abi_window, text="Background")
    background_group.grid(row=2, column=0)
    PC_background_boost = tk.StringVar()
    available_backgrounds_boosts = backgrounds.get_boosts(get_background)
    tk.Radiobutton(background_group, text=available_backgrounds_boosts[0], variable=PC_background_boost,
                   value=available_backgrounds_boosts[0]).grid(row=0, column=0)
    tk.Radiobutton(background_group, text=available_backgrounds_boosts[1], variable=PC_background_boost,
                   value=available_backgrounds_boosts[1]).grid(row=1, column=0)
    PC_background_free = tk.StringVar()
    tk.OptionMenu(background_group, PC_background_free, *abi_free_list).grid(row=0, column=1)

    # ----- Class group
    class_group = tk.LabelFrame(select_abi_window, text="Class")
    class_group.grid(row=3, column=0)
    available_class_boosts = classesfrompathfinder.get_key_ability(get_class)
    if len(available_class_boosts) == 1:
        tk.Label(class_group, text=available_class_boosts).grid(row=0, column=0)
        PC_class_boost = available_class_boosts[0]
    elif len(available_class_boosts) >= 1:
        PC_class_boost = tk.StringVar()
        tk.OptionMenu(class_group, PC_class_boost, *available_class_boosts).grid(row=0, column=0)

    # ----- Free
    tk.Label(select_abi_window, text="Pick four free ability boosts").grid(row=4, column=0)
    str_checkbox = tk.BooleanVar()
    dex_checkbox = tk.BooleanVar()
    con_checkbox = tk.BooleanVar()
    int_checkbox = tk.BooleanVar()
    wis_checkbox = tk.BooleanVar()
    cha_checkbox = tk.BooleanVar()

    tk.Checkbutton(select_abi_window, text="Strength", var=str_checkbox).grid(row=5, column=0, sticky=tk.W)
    tk.Checkbutton(select_abi_window, text="Dexterity", var=dex_checkbox).grid(row=6, column=0, sticky=tk.W)
    tk.Checkbutton(select_abi_window, text="Constitution", var=con_checkbox).grid(row=7, column=0, sticky=tk.W)
    tk.Checkbutton(select_abi_window, text="Intelligence", var=int_checkbox).grid(row=8, column=0, sticky=tk.W)
    tk.Checkbutton(select_abi_window, text="Wisdom", var=wis_checkbox).grid(row=9, column=0, sticky=tk.W)
    tk.Checkbutton(select_abi_window, text="Charisma", var=cha_checkbox).grid(row=10, column=0, sticky=tk.W)

    # ----- OK Button
    def verify_abi_boosts():
        """Ok button on the Select Ability Boosts Window.
        1-Checks if boosts are selected wrong
        2-Displays an error message
        3-else: get the values
        """
        # Grab the selected values.
        get_ancestry_boost = PC_ancestry_free1.get()
        get_radiobutton_background = PC_background_boost.get()
        get_background_free = PC_background_free.get()
        if len(available_class_boosts) == 1:
            get_class_boost = available_class_boosts[0]
        elif len(available_class_boosts) > 1:
            get_class_boost = PC_class_boost.get()
        else:
            return Exception("Could not get the class boost.")

        bool_attributes = [
            str_checkbox.get(),
            dex_checkbox.get(),
            con_checkbox.get(),
            int_checkbox.get(),
            wis_checkbox.get(),
            cha_checkbox.get()
            ]

        count_bool_attributes = bool_attributes.count(True)
        if get_ancestry_boost in PC_ancestry_boosts or \
                get_background_free in available_backgrounds_boosts or \
                count_bool_attributes != 4:
            tk.messagebox.showerror('Illegal selection',
                                    'An illegal selection ocurred. Please select ability boosts again.')

        # Print statements

        # print(PC_ancestry_boosts[0], \
        #       PC_ancestry_boosts[1], \
        #       get_ancestry_boost, \
        #       get_radiobutton_background, \
        #       get_background_free, \
        #       get_class_boost
        #       )
        # print(bool_attributes)

        boosts = [PC_ancestry_boosts[0],
                  PC_ancestry_boosts[1],
                  get_ancestry_boost,
                  get_radiobutton_background,
                  get_background_free,
                  get_class_boost]

        for boost in boosts:
            if boost == 'Strength':
                abilities.Strength.boost()
            elif boost == 'Dexterity':
                abilities.Dexterity.boost()
            elif boost == 'Constitution':
                abilities.Constitution.boost()
            elif boost == 'Intelligence':
                abilities.Intelligence.boost()
            elif boost == 'Wisdom':
                abilities.Wisdom.boost()
            elif boost == 'Charisma':
                abilities.Charisma.boost()
            else:
                return Exception("Ability boost not found")

        flaws = [PC_ancestry_flaw]
        for flaw in flaws:
            if flaw == 'Strength':
                abilities.Strength.flaw()
            elif flaw == 'Dexterity':
                abilities.Dexterity.flaw()
            elif flaw == 'Constitution':
                abilities.Constitution.flaw()
            elif flaw == 'Intelligence':
                abilities.Intelligence.flaw()
            elif flaw == 'Wisdom':
                abilities.Wisdom.flaw()
            elif flaw == 'Charisma':
                abilities.Charisma.flaw()
            else:
                return Exception("Ability flaw not found")

        if bool_attributes[0] is True:
            abilities.Strength.boost()
        if bool_attributes[1] is True:
            abilities.Dexterity.boost()
        if bool_attributes[2] is True:
            abilities.Constitution.boost()
        if bool_attributes[3] is True:
            abilities.Intelligence.boost()
        if bool_attributes[4] is True:
            abilities.Wisdom.boost()
        if bool_attributes[5] is True:
            abilities.Charisma.boost()

        print(abilities.Strength.score)
        print(abilities.Dexterity.score)
        print(abilities.Constitution.score)
        print(abilities.Intelligence.score)
        print(abilities.Wisdom.score)
        print(abilities.Charisma.score)
        select_abi_window.update()
        select_abi_window.destroy()

        # update ability scores
        STR_score.set(abilities.Strength.score)
        DEX_score.set(abilities.Dexterity.score)
        CON_score.set(abilities.Constitution.score)
        INT_score.set(abilities.Intelligence.score)
        WIS_score.set(abilities.Wisdom.score)
        CHA_score.set(abilities.Charisma.score)

        # update ability mods
        STR_mod.set(abilities.Strength.getModifier())
        DEX_mod.set(abilities.Dexterity.getModifier())
        CON_mod.set(abilities.Constitution.getModifier())
        INT_mod.set(abilities.Intelligence.getModifier())
        WIS_mod.set(abilities.Wisdom.getModifier())
        CHA_mod.set(abilities.Charisma.getModifier())

    ok_button = tk.Button(select_abi_window, text="OK", command=verify_abi_boosts)
    ok_button.grid(row=15, column=0)
    # # Cancel button not actually useful, just close the window

    # def exit_button():
    #     select_abi_window.destroy()
    #     # is this .update really a necessity?
    #     # select_abi_window.update()


def select_skills():
    select_skills_window = tk.Toplevel()
    tk.Label(select_skills_window, text="Pick your skills").grid(row=0, column=0, padx=10)
    tk.Label(select_skills_window, text="Trained level").grid(row=0, column=1, padx=10)
    tk.Label(select_skills_window, text="Ability").grid(row=0, column=2, padx=10)
    tk.Label(select_skills_window, text="Prof. Mod").grid(row=0, column=3, padx=10)
    # TODO: show how many skills must be selected.
    checkbox_acrobatics = tk.BooleanVar()
    checkbox_arcana = tk.BooleanVar()
    checkbox_athletics = tk.BooleanVar()
    checkbox_crafting = tk.BooleanVar()
    checkbox_deception = tk.BooleanVar()
    checkbox_diplomacy = tk.BooleanVar()
    checkbox_intimidation = tk.BooleanVar()
    checkbox_medicine = tk.BooleanVar()
    checkbox_nature = tk.BooleanVar()
    checkbox_occultism = tk.BooleanVar()
    checkbox_performance = tk.BooleanVar()
    checkbox_religion = tk.BooleanVar()
    checkbox_society = tk.BooleanVar()
    checkbox_stealth = tk.BooleanVar()
    checkbox_survival = tk.BooleanVar()
    checkbox_thievery = tk.BooleanVar()

    # Checkboxes
    tk.Checkbutton(select_skills_window, text="Acrobatics", var=checkbox_acrobatics).grid(
        row=1, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Arcana", var=checkbox_arcana).grid(
        row=2, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Athletics", var=checkbox_athletics).grid(
        row=3, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Crafting", var=checkbox_crafting).grid(
        row=4, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Deception", var=checkbox_deception).grid(
        row=5, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Diplomacy", var=checkbox_diplomacy).grid(
        row=6, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Intimidation", var=checkbox_intimidation).grid(
        row=7, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Medicine", var=checkbox_medicine).grid(
        row=8, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Nature", var=checkbox_nature).grid(
        row=9, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Occultism", var=checkbox_occultism).grid(
        row=10, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Performance", var=checkbox_performance).grid(
        row=11, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Religion", var=checkbox_religion).grid(
        row=12, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Society", var=checkbox_society).grid(
        row=13, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Stealth", var=checkbox_stealth).grid(
        row=14, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Survival", var=checkbox_survival).grid(
        row=15, column=0, sticky=tk.W)
    tk.Checkbutton(select_skills_window, text="Thievery", var=checkbox_thievery).grid(
        row=16, column=0, sticky=tk.W)

    # Trained level
    tk.Label(select_skills_window, text="trained").grid(row=1, column=1)
    tk.Label(select_skills_window, text="").grid(row=2, column=1)
    tk.Label(select_skills_window, text="").grid(row=3, column=1)
    tk.Label(select_skills_window, text="").grid(row=4, column=1)
    tk.Label(select_skills_window, text="").grid(row=5, column=1)
    tk.Label(select_skills_window, text="").grid(row=6, column=1)
    tk.Label(select_skills_window, text="").grid(row=7, column=1)
    tk.Label(select_skills_window, text="").grid(row=8, column=1)
    tk.Label(select_skills_window, text="").grid(row=9, column=1)
    tk.Label(select_skills_window, text="").grid(row=10, column=1)
    tk.Label(select_skills_window, text="").grid(row=11, column=1)
    tk.Label(select_skills_window, text="").grid(row=12, column=1)
    tk.Label(select_skills_window, text="").grid(row=13, column=1)
    tk.Label(select_skills_window, text="").grid(row=14, column=1)
    tk.Label(select_skills_window, text="").grid(row=15, column=1)
    tk.Label(select_skills_window, text="").grid(row=16, column=1)

    # Skill Ability Modifier
    tk.Label(select_skills_window, text=abilities.Dexterity.getModifier()).grid(row=1, column=2)  # Acrobatics
    tk.Label(select_skills_window, text=abilities.Intelligence.getModifier()).grid(row=2, column=2)  # Arcana
    tk.Label(select_skills_window, text=abilities.Strength.getModifier()).grid(row=3, column=2)  # Athletics
    tk.Label(select_skills_window, text=abilities.Intelligence.getModifier()).grid(row=4, column=2)  # Crafting
    tk.Label(select_skills_window, text=abilities.Charisma.getModifier()).grid(row=5, column=2)  # Deception
    tk.Label(select_skills_window, text=abilities.Charisma.getModifier()).grid(row=6, column=2)  # Diplomacy
    tk.Label(select_skills_window, text=abilities.Charisma.getModifier()).grid(row=7, column=2)  # Intimidation
    tk.Label(select_skills_window, text=abilities.Wisdom.getModifier()).grid(row=8, column=2)  # Medicine
    tk.Label(select_skills_window, text=abilities.Wisdom.getModifier()).grid(row=9, column=2)  # Nature
    tk.Label(select_skills_window, text=abilities.Intelligence.getModifier()).grid(row=10, column=2)  # Occultism
    tk.Label(select_skills_window, text=abilities.Charisma.getModifier()).grid(row=11, column=2)  # Performance
    tk.Label(select_skills_window, text=abilities.Wisdom.getModifier()).grid(row=12, column=2)  # Religion
    tk.Label(select_skills_window, text=abilities.Intelligence.getModifier()).grid(row=13, column=2)  # Society
    tk.Label(select_skills_window, text=abilities.Dexterity.getModifier()).grid(row=14, column=2)  # Stealth
    tk.Label(select_skills_window, text=abilities.Wisdom.getModifier()).grid(row=15, column=2)  # Survival
    tk.Label(select_skills_window, text=abilities.Dexterity.getModifier()).grid(row=16, column=2)  # Thievery

    # Proficiency modifier
    tk.Label(select_skills_window, text="+3").grid(row=1, column=3)


# --------------------------------------------------------- mid frame
# Buttons on the left of abilities scores
abi_boost_selection = tk.Button(mid_frame, text="Select ability boosts", command=select_abi_boost)
abi_boost_selection.grid(row=0, column=0, columnspan=4, padx=50)
skills_selection = tk.Button(mid_frame, text="Select trained skills", command=select_skills)
skills_selection.grid(row=1, column=0, columnspan=4, padx=50)

# Blank space
tk.Label(mid_frame, text="                           ", ).grid(row=2, column=0, columnspan=5)

# Armor Class
tk.Label(mid_frame, text="AC").grid(row=3, column=0)
tk.Label(mid_frame, text=ac.value).grid(row=3, column=1)

# HitPoints
tk.Label(mid_frame, text="HP").grid(row=3, column=2)
tk.Label(mid_frame, text=hitpoints.value).grid(row=3, column=3)

# --- Saving Throws
# Labels
tk.Label(mid_frame, text="Saving Throws").grid(row=4, column=0, columnspan=4)
tk.Label(mid_frame, text="Fortitude (Con) ").grid(row=5, column=0, columnspan=2)
tk.Label(mid_frame, text="Reflex (Dex) ").grid(row=6, column=0, columnspan=2)
tk.Label(mid_frame, text="Will (Wis) ").grid(row=7, column=0, columnspan=2)
# Mods
tk.Label(mid_frame, text=savingthrow.Fortitude).grid(row=5, column=2, columnspan=2)
tk.Label(mid_frame, text=savingthrow.Reflex).grid(row=6, column=2, columnspan=2)
tk.Label(mid_frame, text=savingthrow.Will).grid(row=7, column=2, columnspan=2)

# --- Perception
tk.Label(mid_frame, text="Perception").grid(row=8, column=0, columnspan=4)
tk.Label(mid_frame, text=skills.perception_proficiency, anchor="w").grid(row=9, column=0, columnspan=2)
tk.Label(mid_frame, text=skills.perception_mod).grid(row=9, column=2, columnspan=2)

# --------------------------------------------------------- Bottom Box
# Skill labels (Lore skills remaining)
tk.Label(skills_frame, text="Skills").grid(row=0, column=0, pady=5)
tk.Label(skills_frame, text="Acrobatics (Dex)", anchor="w").grid(sticky=tk.W, row=1, column=0)
tk.Label(skills_frame, text="Arcana (Int)", anchor="w").grid(sticky=tk.W, row=2, column=0)
tk.Label(skills_frame, text="Athletics (Str)", anchor="w").grid(sticky=tk.W, row=3, column=0)
tk.Label(skills_frame, text="Crafting (Int)", anchor="w").grid(sticky=tk.W, row=4, column=0)
tk.Label(skills_frame, text="Deception (Cha)", anchor="w").grid(sticky=tk.W, row=5, column=0)
tk.Label(skills_frame, text="Diplomacy (Cha)", anchor="w").grid(sticky=tk.W, row=6, column=0)
tk.Label(skills_frame, text="Intimidation (Cha)", anchor="w").grid(sticky=tk.W, row=7, column=0)
tk.Label(skills_frame, text="Medicine (Wis)", anchor="w").grid(sticky=tk.W, row=8, column=0)
tk.Label(skills_frame, text="Nature (Wis)", anchor="w").grid(sticky=tk.W, row=9, column=0)
tk.Label(skills_frame, text="Occultism (Int)", anchor="w").grid(sticky=tk.W, row=10, column=0)
tk.Label(skills_frame, text="Performance (Cha)", anchor="w").grid(sticky=tk.W, row=11, column=0)
tk.Label(skills_frame, text="Religion (Wis)", anchor="w").grid(sticky=tk.W, row=12, column=0)
tk.Label(skills_frame, text="Society (Int)", anchor="w").grid(sticky=tk.W, row=13, column=0)
tk.Label(skills_frame, text="Stealth (Dex)", anchor="w").grid(sticky=tk.W, row=14, column=0)
tk.Label(skills_frame, text="Survival (Wis)", anchor="w").grid(sticky=tk.W, row=15, column=0)
tk.Label(skills_frame, text="Thievery (Dex)", anchor="w").grid(sticky=tk.W, row=16, column=0)

# Skill Modifiers (Lore skills remaining)
tk.Label(skills_frame, text="Mod").grid(row=0, column=1, pady=5)
tk.Label(skills_frame, text=skills.acrobatics_mod, anchor="w").grid(row=1, column=1, padx=10)
tk.Label(skills_frame, text=skills.arcana_mod, anchor="w").grid(row=2, column=1, padx=10)
tk.Label(skills_frame, text=skills.athletics_mod, anchor="w").grid(row=3, column=1, padx=10)
tk.Label(skills_frame, text=skills.crafting_mod, anchor="w").grid(row=4, column=1, padx=10)
tk.Label(skills_frame, text=skills.deception_mod, anchor="w").grid(row=5, column=1, padx=10)
tk.Label(skills_frame, text=skills.diplomacy_mod, anchor="w").grid(row=6, column=1, padx=10)
tk.Label(skills_frame, text=skills.intimidation_mod, anchor="w").grid(row=7, column=1, padx=10)
tk.Label(skills_frame, text=skills.medicine_mod, anchor="w").grid(row=8, column=1, padx=10)
tk.Label(skills_frame, text=skills.nature_mod, anchor="w").grid(row=9, column=1, padx=10)
tk.Label(skills_frame, text=skills.occultism_mod, anchor="w").grid(row=10, column=1, padx=10)
tk.Label(skills_frame, text=skills.performance_mod, anchor="w").grid(row=11, column=1, padx=10)
tk.Label(skills_frame, text=skills.religion_mod, anchor="w").grid(row=12, column=1, padx=10)
tk.Label(skills_frame, text=skills.society_mod, anchor="w").grid(row=13, column=1, padx=10)
tk.Label(skills_frame, text=skills.stealth_mod, anchor="w").grid(row=14, column=1, padx=10)
tk.Label(skills_frame, text=skills.survival_mod, anchor="w").grid(row=15, column=1, padx=10)
tk.Label(skills_frame, text=skills.thievery_mod, anchor="w").grid(row=16, column=1, padx=10)

# Skill Training
tk.Label(skills_frame, text="Proficiency").grid(row=0, column=2, pady=5)
tk.Label(skills_frame, text=skills.acrobatics_proficiency).grid(row=1, column=2, padx=10)
tk.Label(skills_frame, text=skills.arcana_proficiency).grid(row=2, column=2, padx=10)
tk.Label(skills_frame, text=skills.athletics_proficiency).grid(row=3, column=2, padx=10)
tk.Label(skills_frame, text=skills.crafting_proficiency).grid(row=4, column=2, padx=10)
tk.Label(skills_frame, text=skills.deception_proficiency).grid(row=5, column=2, padx=10)
tk.Label(skills_frame, text=skills.diplomacy_proficiency).grid(row=6, column=2, padx=10)
tk.Label(skills_frame, text=skills.intimidation_proficiency).grid(row=7, column=2, padx=10)
tk.Label(skills_frame, text=skills.medicine_proficiency).grid(row=8, column=2, padx=10)
tk.Label(skills_frame, text=skills.nature_proficiency).grid(row=9, column=2, padx=10)
tk.Label(skills_frame, text=skills.occultism_proficiency).grid(row=10, column=2, padx=10)
tk.Label(skills_frame, text=skills.performance_proficiency).grid(row=11, column=2, padx=10)
tk.Label(skills_frame, text=skills.religion_proficiency).grid(row=12, column=2, padx=10)
tk.Label(skills_frame, text=skills.society_proficiency).grid(row=13, column=2, padx=10)
tk.Label(skills_frame, text=skills.stealth_proficiency).grid(row=14, column=2, padx=10)
tk.Label(skills_frame, text=skills.survival_proficiency).grid(row=15, column=2, padx=10)
tk.Label(skills_frame, text=skills.thievery_proficiency).grid(row=16, column=2, padx=10)

# --------------------------------------------------------- Lore Skills
# Lore labels (Lore skills remaining)
tk.Label(lore_frame, text="Lores").grid(row=0, column=0, pady=5)
tk.Label(lore_frame, text="Lore number 1 (Int)", anchor="w").grid(sticky=tk.W, row=1, column=0)

# Lore Modifiers (Lore skills remaining)
tk.Label(lore_frame, text="Mod").grid(row=0, column=1, pady=5)
tk.Label(lore_frame, text="5", anchor="w").grid(row=1, column=1, padx=10)

# Lore Training
tk.Label(lore_frame, text="Proficiency").grid(row=0, column=2, pady=5)
tk.Label(lore_frame, text="Master").grid(row=1, column=2, padx=10)


# --------------------------------------------------------- Feats frame
# Labels
tk.Label(feats_frame, text="Ancestry Feats and Abilities").grid(row=0, column=0, columnspan=2, padx=30)
tk.Label(feats_frame, text="Skill Feats").grid(row=8,  column=0, columnspan=2)
tk.Label(feats_frame, text="General Feats").grid(row=20, column=0, columnspan=2)
tk.Label(feats_frame, text="Class Feats and Abilities").grid(row=0, column=2, columnspan=2, padx=30)
tk.Label(feats_frame, text="Bonus Feats").grid(row=23, column=2, columnspan=2)

# Feats call (insert the feats-file.py)
# Ancestry
tk.Label(feats_frame, text="Ancestry Feat 1").grid(row=1, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Ancestry Feat 1").grid(row=2, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Ancestry Feat 1").grid(row=3, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Ancestry Feat 1").grid(row=4, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Ancestry Feat 1").grid(row=5, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Ancestry Feat 1").grid(row=6, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Ancestry Feat 1").grid(row=7, column=0, sticky=tk.W)

# Skill
tk.Label(feats_frame, text="Skill Feat 1").grid(row=9, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=10, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=11, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=12, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=13, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=14, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=15, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=16, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=17, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=18, column=0, sticky=tk.W)
tk.Label(feats_frame, text="Skill Feat 1").grid(row=19, column=0, sticky=tk.W)

# General
tk.Label(feats_frame, text="General Feat 1").grid(row=21, column=0, sticky=tk.W)
tk.Label(feats_frame, text="General Feat 1").grid(row=22, column=0, sticky=tk.W)
tk.Label(feats_frame, text="General Feat 1").grid(row=23, column=0, sticky=tk.W)
tk.Label(feats_frame, text="General Feat 1").grid(row=24, column=0, sticky=tk.W)
tk.Label(feats_frame, text="General Feat 1").grid(row=25, column=0, sticky=tk.W)

# Class
tk.Label(feats_frame, text="Class Feat 1").grid(row=1, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=2, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=3, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=4, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=5, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=6, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=7, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=8, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=9, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=10, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=11, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=12, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=13, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=14, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=15, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=16, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=17, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=18, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=19, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=20, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=21, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Class Feat 1").grid(row=22, column=2, sticky=tk.W)

# Bonus
tk.Label(feats_frame, text="Bonus Feat 1").grid(row=24, column=2, sticky=tk.W)
tk.Label(feats_frame, text="Bonus Feat 1").grid(row=25, column=2, sticky=tk.W)


# ---------- Buttons
Button1 = tk.Button(feats_frame, text="Special 1st", command=mfx.open_file)
Button2 = tk.Button(feats_frame, text="Heritage 1st", command=mfx.open_file)
Button3 = tk.Button(feats_frame, text="Feat 1st", command=mfx.open_file)
Button4 = tk.Button(feats_frame, text="Feat 5th", command=mfx.open_file)
Button5 = tk.Button(feats_frame, text="Feat 9th", command=mfx.open_file)
Button6 = tk.Button(feats_frame, text="Feat 13th", command=mfx.open_file)
Button7 = tk.Button(feats_frame, text="Feat 17th", command=mfx.open_file)
Button1.grid(row=1, column=1, sticky=tk.E)
Button2.grid(row=2, column=1, sticky=tk.E)
Button3.grid(row=3, column=1, sticky=tk.E)
Button4.grid(row=4, column=1, sticky=tk.E)
Button5.grid(row=5, column=1, sticky=tk.E)
Button6.grid(row=6, column=1, sticky=tk.E)
Button7.grid(row=7, column=1, sticky=tk.E)

Button8 = tk.Button(feats_frame, text="Background", command=mfx.open_file)
Button9 = tk.Button(feats_frame, text="Skill 2nd", command=mfx.open_file)
Button10 = tk.Button(feats_frame, text="Skill 4th", command=mfx.open_file)
Button11 = tk.Button(feats_frame, text="Skill 6th", command=mfx.open_file)
Button12 = tk.Button(feats_frame, text="Skill 8th", command=mfx.open_file)
Button13 = tk.Button(feats_frame, text="Skill 10th", command=mfx.open_file)
Button14 = tk.Button(feats_frame, text="Skill 12th", command=mfx.open_file)
Button15 = tk.Button(feats_frame, text="Skill 14th", command=mfx.open_file)
Button16 = tk.Button(feats_frame, text="Skill 16th", command=mfx.open_file)
Button17 = tk.Button(feats_frame, text="Skill 18th", command=mfx.open_file)
Button18 = tk.Button(feats_frame, text="Skill 20th", command=mfx.open_file)
Button8.grid(row=9, column=1, sticky=tk.E)
Button9.grid(row=10, column=1, sticky=tk.E)
Button10.grid(row=11, column=1, sticky=tk.E)
Button11.grid(row=12, column=1, sticky=tk.E)
Button12.grid(row=13, column=1, sticky=tk.E)
Button13.grid(row=14, column=1, sticky=tk.E)
Button14.grid(row=15, column=1, sticky=tk.E)
Button15.grid(row=16, column=1, sticky=tk.E)
Button16.grid(row=17, column=1, sticky=tk.E)
Button17.grid(row=18, column=1, sticky=tk.E)
Button18.grid(row=19, column=1, sticky=tk.E)

Button19 = tk.Button(feats_frame, text="General 3th", command=mfx.open_file)
Button20 = tk.Button(feats_frame, text="General 7th", command=mfx.open_file)
Button21 = tk.Button(feats_frame, text="General 11th", command=mfx.open_file)
Button22 = tk.Button(feats_frame, text="General 15th", command=mfx.open_file)
Button23 = tk.Button(feats_frame, text="General 19th", command=mfx.open_file)
Button19.grid(row=21, column=1, sticky=tk.E)
Button20.grid(row=22, column=1, sticky=tk.E)
Button21.grid(row=23, column=1, sticky=tk.E)
Button22.grid(row=24, column=1, sticky=tk.E)
Button23.grid(row=25, column=1, sticky=tk.E)

# Second column
Button24 = tk.Button(feats_frame, text="Feature 1st", command=mfx.open_file)
Button25 = tk.Button(feats_frame, text="Feature 1st", command=mfx.open_file)
Button26 = tk.Button(feats_frame, text="Class 1st", command=mfx.open_file)
Button27 = tk.Button(feats_frame, text="Class 2nd", command=mfx.open_file)
Button28 = tk.Button(feats_frame, text="Feature 3th", command=mfx.open_file)
Button29 = tk.Button(feats_frame, text="Class 4th", command=mfx.open_file)
Button30 = tk.Button(feats_frame, text="Feature 5th", command=mfx.open_file)
Button31 = tk.Button(feats_frame, text="Class 6th", command=mfx.open_file)
Button32 = tk.Button(feats_frame, text="Feature 7th", command=mfx.open_file)
Button33 = tk.Button(feats_frame, text="Class 8th", command=mfx.open_file)
Button34 = tk.Button(feats_frame, text="Feature 9th", command=mfx.open_file)
Button35 = tk.Button(feats_frame, text="Class 10th", command=mfx.open_file)
Button36 = tk.Button(feats_frame, text="Feature 11th", command=mfx.open_file)
Button37 = tk.Button(feats_frame, text="Class 12th", command=mfx.open_file)
Button38 = tk.Button(feats_frame, text="Feature 13th", command=mfx.open_file)
Button39 = tk.Button(feats_frame, text="Class 14th", command=mfx.open_file)
Button40 = tk.Button(feats_frame, text="Feature 15th", command=mfx.open_file)
Button41 = tk.Button(feats_frame, text="Class 16th", command=mfx.open_file)
Button42 = tk.Button(feats_frame, text="Feature 17th", command=mfx.open_file)
Button43 = tk.Button(feats_frame, text="Class 18th", command=mfx.open_file)
Button44 = tk.Button(feats_frame, text="Feature 19th", command=mfx.open_file)
Button45 = tk.Button(feats_frame, text="Class 20th", command=mfx.open_file)
Button24.grid(row=1, column=3, sticky=tk.E)
Button25.grid(row=2, column=3, sticky=tk.E)
Button26.grid(row=3, column=3, sticky=tk.E)
Button27.grid(row=4, column=3, sticky=tk.E)
Button28.grid(row=5, column=3, sticky=tk.E)
Button29.grid(row=6, column=3, sticky=tk.E)
Button30.grid(row=7, column=3, sticky=tk.E)
Button31.grid(row=8, column=3, sticky=tk.E)
Button32.grid(row=9, column=3, sticky=tk.E)
Button33.grid(row=10, column=3, sticky=tk.E)
Button34.grid(row=11, column=3, sticky=tk.E)
Button35.grid(row=12, column=3, sticky=tk.E)
Button36.grid(row=13, column=3, sticky=tk.E)
Button37.grid(row=14, column=3, sticky=tk.E)
Button38.grid(row=15, column=3, sticky=tk.E)
Button39.grid(row=16, column=3, sticky=tk.E)
Button40.grid(row=17, column=3, sticky=tk.E)
Button41.grid(row=18, column=3, sticky=tk.E)
Button42.grid(row=19, column=3, sticky=tk.E)
Button43.grid(row=20, column=3, sticky=tk.E)
Button44.grid(row=21, column=3, sticky=tk.E)
Button45.grid(row=22, column=3, sticky=tk.E)

root.mainloop()
