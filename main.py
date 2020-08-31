import tkinter as tk

root = tk.Tk()
root.title('Shendi - Pathfinder 2nd Edition Character Builder')
root.geometry("400x400")

# Creating menu bar
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Creating a Label widget
myLabel = tk.Label(root, text="Hello Shendi!")

# Showing it onto the screen
myLabel.pack()

# creating aa menu item
file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)

root.mainloop()

