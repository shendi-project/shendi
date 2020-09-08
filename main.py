import tkinter as tk
from tkinter import ttk
import menufunctions as mfx
import ability_scores

root = tk.Tk()
root.title('shendi - Pathfinder 2nd Edition Character Builder')
root.config(bg="skyblue")

# The applications will consist on different Frames
# The first frame includes the character name, ancestry, background and class
top_frame = tk.Frame(root, width=200, height=400, bg='yellow')
top_frame.grid(row=0, column=0, padx=10, pady=0)
# The second frame includes abilities, and a couple of main buttons
tabs_frame = ttk.Notebook(root, width=200, height=200)
tabs_frame.grid(row=1, column=0, columnspan=3,padx=10, pady=10, sticky="w")
# the bottom frame (currently empty) includes some information on what-to-do-next
bottom_frame = tk.Frame(root, width=200, height=50, bg='green')
bottom_frame.grid(row=2, column=0, padx=10, pady=10)


# todo: split this huge UI in more manageable files

# Creation of the menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Creation of File menu dropdown and items
file_menu = tk.Menu(menu_bar, tearoff=0)  # tear off = 0 deletes a -- line on the menus
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=mfx.open_file)


# Creation of Help menu dropdown and items
help_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=mfx.show_about)
help_menu.add_command(label="Go to Github repository", command=mfx.go_to_github)


# Top application box
# Label for name, ancestry, background and class
tk.Label(top_frame, text="Character name:").grid(row=0, column=0)
pc_name_field = tk.Entry(top_frame, width=30).grid(row=0, column=1)

tk.Label(top_frame, text="Character ancestry:").grid(row=1, column=0)
ancestry = tk.StringVar()
# todo: add an empty space FIRST, then the list of races
races = ["", "Catfolk", "Dwarf", "Elf"]
drop_races = tk.OptionMenu(top_frame, ancestry, *races).grid(row=1, column=1)
s
tk.Label(top_frame, text="Character background:").grid(row=2, column=0)
background = tk.StringVar()
available_backgrounds = ["", "Aerealist", "Animal Wrangler (Athletics)"]
drop_background = tk.OptionMenu(top_frame, background, *available_backgrounds).grid(row=2, column=1)

tk.Label(top_frame, text="Character class:").grid(row=3, column=0)
PC_class = tk.StringVar()
available_classes = ["", "Alchemist", "Barbarian", "Bard"]
drop_class = tk.OptionMenu(top_frame, PC_class, *available_classes).grid(row=3, column=1)

# Ability Labels and scores
tk.Label(tabs_frame, text="Strength").grid(row=0, column=0, pady=10)
tk.Label(tabs_frame, text=ability_scores.str_ability).grid(row=0, column=1, padx=20, pady= 10)
tk.Label(tabs_frame, text=ability_scores.str_mod).grid(row=0, column=2, pady=10)

tk.Label(tabs_frame, text="Dexterity").grid(row=1, column=0, pady=10)
tk.Label(tabs_frame, text=ability_scores.dex_ability).grid(row=1, column=1, padx=20, pady=10)
tk.Label(tabs_frame, text=ability_scores.dex_mod).grid(row=1, column=2, pady=10)

tk.Label(tabs_frame, text="Constitution").grid(row=2, column=0, pady=10)
tk.Label(tabs_frame, text=ability_scores.con_ability).grid(row=2, column=1, padx=20, pady=10)
tk.Label(tabs_frame, text=ability_scores.con_mod).grid(row=2, column=2, padx=20, pady=10)

tk.Label(tabs_frame, text="Intelligence").grid(row=3, column=0, pady=10)
tk.Label(tabs_frame, text=ability_scores.int_ability).grid(row=3, column=1, padx=20, pady=10)
tk.Label(tabs_frame, text=ability_scores.int_mod).grid(row=3, column=2, pady=10)

tk.Label(tabs_frame, text="Wisdom").grid(row=4, column=0, pady=10)
tk.Label(tabs_frame, text=ability_scores.wis_ability).grid(row=4, column=1, padx=20, pady=10)
tk.Label(tabs_frame, text=ability_scores.wis_mod).grid(row=4, column=2, pady=10)

tk.Label(tabs_frame, text="Charisma").grid(row=5, column=0, pady=10)
tk.Label(tabs_frame, text=ability_scores.cha_ability).grid(row=5, column=1, padx=20, pady=10)
tk.Label(tabs_frame, text=ability_scores.cha_mod).grid(row=5, column=2, pady=10)

# Buttons on the left of abilities scores
abi_boost_selection = tk.Button(tabs_frame, text="Select ability boosts", command=mfx.select_abi_boost)
abi_boost_selection.grid(row=0, column=3, padx=50)
skills_selection = tk.Button(tabs_frame, text="Select trained skills", command=mfx.select_skills)
skills_selection.grid(row=1, column=3, padx=50)


# str_label = tk.Label(my_frame1, text="Strength")
# str_label.grid(row=3, column=0)

# bottom limit (where the status bar goes)

# tabs_frame.add(root, text="PC 1")

root.mainloop()
