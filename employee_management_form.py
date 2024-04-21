import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import StringVar


def button_press():

    print('')

# root window
root = tk.Tk()
root.title('Employee Creation / Removal Form')
root.geometry('450x400')
root.resizable(False, False)

# frame
frame = ttk.Frame(root)

options = {'padx': 5, 'pady': 5}

"""
Employee ID
"""
# Employee ID label
id_label = ttk.Label(frame, text='Employee ID')
id_label.grid(column=0, row=0, sticky='W', **options)

# id entry
id_v = tk.StringVar()
id_entry = ttk.Entry(frame, textvariable=id_v, width=30)
id_entry.grid(column=1, row=0, sticky='W',**options)
id_entry.focus()

"""
Operation type
"""
# Label to indicate employee operation type
operation_label = ttk.Label(root, text='Operation Type')
operation_label.grid(column=0, row=0, sticky='W', **options)

# Dropdown to indicate onboarding/offboarding
v = StringVar(root)
v.set("Onboarding") # default value
operation_drop = ttk.OptionMenu(root, v, "Onboarding", "Onboarding", "Offboarding")
operation_drop.grid(column=0, row=1, sticky='W', **options)

"""
first name
"""
# First Name label
first_name_label = ttk.Label(frame, text='First Name')
first_name_label.grid(column=0, row=2, sticky='W', **options)

# First Name entry
first_name = tk.StringVar()
first_name_entry = ttk.Entry(frame, textvariable=first_name, width=30)
first_name_entry.grid(column=1, row=2, **options)
first_name_entry.focus()

"""
last name
"""
# last Name label
last_name_label = ttk.Label(frame, text='Last Name', width=30)
last_name_label.grid(column=0, row=3, sticky='W', **options)

# Last Name entry
last_name = tk.StringVar()
last_name_entry = ttk.Entry(frame, textvariable=last_name, width=30)
last_name_entry.grid(column=1, row=3, sticky='W',**options)
last_name_entry.focus()

# Address (if creating)
address_label = ttk.Label(frame, text='Address')
address_label.grid(column=0, row=4, sticky='W', **options)

# Address entry
address = tk.StringVar()
address_entry = ttk.Entry(frame, textvariable=address, width=30)
address_entry.grid(column=1, row=4, **options)
address_entry.focus()

# Position entry
Position_label = ttk.Label(frame, text='Position')
Position_label.grid(column=0, row=4, sticky='W', **options)

# Address entry
position = tk.StringVar()
position_entry = ttk.Entry(frame, textvariable=position, width=30)
position_entry.grid(column=1, row=4, **options)
position_entry.focus()

# Empty label to create space between save button and form
empty_label1 = ttk.Label(frame, text=' ')
empty_label1.grid(column=0, row=5)

# Save button
save_button = ttk.Button(frame, text='Save', command=button_press)
save_button.grid(column=1, row=20,sticky='W', **options)

frame.grid(padx=10, pady=10)
# start the app
root.mainloop()