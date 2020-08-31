import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser

root = tk.Tk()
root.title('shendi - Pathfinder 2nd Edition Character Builder')
root.geometry("400x400")


# Create a PC
def create_pc(pc_name):
    print(pc_name)


#       Menu Functions
# show about
def show_about():
    messagebox.showinfo("About shendi", "This is a project by AucaCoyan#9411. "
                                        "Contact him at Discord or you can check "
                                        "the github at: "
                                        "https://github.com/AucaCoyan/shendi")


def go_to_github():
    webbrowser.open_new("https://github.com/AucaCoyan/shendi")


#       Creating menu bar
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Creating File menu Item
file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File",
                    menu=file_menu)

# Creating Help menu Item
help_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Help",
                    menu=help_menu)
help_menu.add_command(label="About",
                      command=show_about)
help_menu.add_command(label="Go to Github repository",
                      command=go_to_github)

# Text before the field
enter_name_for_pc = tk.Label(root,
                             text="Enter the name of your character:")
enter_name_for_pc.grid(row=0, column=0)

# Creating an input field
pc_name_field = tk.Entry(root,
                         width=30)

# Creating the ok button
ok_name = tk.Button(root, text="OK", command=create_pc(enter_name_for_pc.pack()))

# Locations of fields in the grid
enter_name_for_pc.grid(row=0, column=0)
pc_name_field.grid(row=0, column=1)
ok_name.grid(row=0, column=3)


# Tabs
my_notebook = ttk.Notebook()
# bottom limit (where the status bar goes)
# my_notebook.pack(pady=15)

my_frame1 = tk.Frame(my_notebook, width=500, height=500, bg="blue")
my_frame1.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="PC 1")

root.mainloop()
