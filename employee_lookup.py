import tkinter as tk
from tkinter import ttk

def show_hide_fields(option):

    selection = dropdown.get()

    if selection == "Onboarding":

        id_label.grid(column=0, row=1, padx=10, pady=5)
        id_entry.grid(column=1, row=1, padx=10, pady=5)
        first_name_label.grid(column=0, row=2, padx=10, pady=5)
        first_name_entry.grid(column=1, row=2, padx=10, pady=5)
        last_name_label.grid(column=0, row=3, padx=10, pady=5)
        last_name_entry.grid(column=1, row=3, padx=10, pady=5)
        address_label.grid(column=0, row=4, padx=10, pady=5)
        address_entry.grid(column=1, row=4, padx=10, pady=5)
        position_label.grid(column=0, row=5, padx=10, pady=5)
        position_entry.grid(column=1, row=5, padx=10, pady=5)
        reason_label.grid_remove()
        reason_entry.grid_remove()
        save_button = ttk.Button(root, text='Save')
        save_button.grid(column=0, row=20, padx=10, pady=5)

    elif selection == "Offboarding":

        id_label.grid(column=0, row=1, padx=10, pady=5)
        id_entry.grid(column=1, row=1, padx=10, pady=5)
        first_name_label.grid(column=0, row=2, padx=10, pady=5)
        first_name_entry.grid(column=1, row=2, padx=10, pady=5)
        last_name_label.grid(column=0, row=3, padx=10, pady=5)
        last_name_entry.grid(column=1, row=3, padx=10, pady=5)
        address_label.grid(column=0, row=4, padx=10, pady=5)
        address_entry.grid(column=1, row=4, padx=10, pady=5)
        position_label.grid(column=0, row=5, padx=10, pady=5)
        position_entry.grid(column=1, row=5, padx=10, pady=5)
        reason_label.grid(column=0, row=6, padx=10, pady=5)
        reason_entry.grid(column=1, row=6, padx=10, pady=5)
        save_button = ttk.Button(root, text='Save')
        save_button.grid(column=0, row=20, padx=10, pady=5)

    elif selection == "Employee Lookup":
        
        id_label.grid(column=0, row=1, padx=10, pady=5)
        id_entry.grid(column=1, row=1, padx=10, pady=5)
        first_name_label.grid_remove()
        first_name_entry.grid_remove()
        last_name_label.grid_remove()
        last_name_entry.grid_remove()
        address_label.grid_remove()
        address_entry.grid_remove()
        position_label.grid_remove()
        position_entry.grid_remove()
        reason_label.grid_remove()
        reason_entry.grid_remove()
        search_button = ttk.Button(root, text='Search')
        search_button.grid(column=0, row=20, padx=10, pady=5)


root = tk.Tk()
root.title("Employee Management Form")
frame = ttk.Frame(root)
root.geometry('450x450')

operation_label = ttk.Label(root, text='Operation Selection')
operation_label.grid(column=0, row=0, padx=10, pady=5)

# Dropdown menu
options = ["Onboarding", "Offboarding", "Employee Lookup"]
dropdown = ttk.Combobox(root, values=options)
dropdown.grid(row=0, column=1, padx=10, pady=5)
dropdown.bind("<<ComboboxSelected>>", show_hide_fields)

# Form fields
id_label = ttk.Label(root, text='Employee ID')
id_entry = ttk.Entry(root, width=30)
first_name_label = ttk.Label(root, text='First Name')
first_name_entry = ttk.Entry(root, width=30)
last_name_label = ttk.Label(root, text='Last Name')
last_name_entry = ttk.Entry(root, width=30)
address_label = ttk.Label(root, text='Address')
address_entry = ttk.Entry(root, width=30)
position_label = ttk.Label(root, text='Position')
position_entry = ttk.Entry(root, width=30)
reason_label = ttk.Label(root, text="Reason for Leaving")
reason_entry = tk.Text(root, height=10,width=30)
empty_label1 = ttk.Label(frame, text=' ')

# Employee ID label

# id entry
#id_entry = ttk.Entry(frame, width=30)


root.mainloop()
