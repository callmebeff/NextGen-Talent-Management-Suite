
import customtkinter as ctk
import time




class ClearanceUpdate(ctk.CTk):

    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)
        self.geometry("600x650")
        self.title('Employee Clearance Update')
        self.grid_columnconfigure(0, weight=1)
        ctk.set_appearance_mode("dark") 

        self.id_label = ctk.CTkLabel(self, text="Employee ID")
        self.id_label.grid(column=0, row=0, padx=10, pady=5, sticky='ew')

        self.id_entry = ctk.CTkEntry(self, placeholder_text='Enter an ID')
        self.id_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')

        self.name_label = ctk.CTkLabel(self, text="Employee Name")
        self.name_label.grid(column=0, row=1, padx=10, pady=5, sticky='ew')

        self.name_entry = ctk.CTkEntry(self, placeholder_text='Enter an employee name')
        self.name_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')

        self.clearance_label = ctk.CTkLabel(self, text="New Clearance Level")
        self.clearance_label.grid(column=0, row=2, padx=10, pady=5, sticky='ew')

        self.clearance_combobox = ctk.CTkComboBox(self, values=["No Clearance", "Low-Level Clearance", "Medium-Level Clearance", "High-Level Clearance"], width=350)
        self.clearance_combobox.grid(column=1, row=2, padx=10, pady=5, sticky='ew')

        self.reason_label = ctk.CTkLabel(self, text="Reason for Change")
        self.reason_label.grid(column=0, row=3, padx=10, pady=5, sticky='ew')

        self.reason_textbox = ctk.CTkTextbox(self)
        self.reason_textbox.grid(column=1, row=3, padx=10, pady=5, sticky='ew')


        self.update_button = ctk.CTkButton(self, text="Update")
        self.update_button.grid(column=0, row=20, padx=10, pady=5, sticky='ew', columnspan=2)




def main():
    clearance_update = ClearanceUpdate()
    clearance_update.mainloop()
"""

"""

# ctk.set_appearance_mode("dark")

# app = ctk.CTk()
# app.geometry("400x480")
# app.title('Employee Clearance Update')

# id_label = ctk.CTkLabel(app, text="Employee ID", width=200)
# id_label.pack()
# id_entry = ctk.CTkEntry(app, placeholder_text='Enter a name', width=350)
# id_entry.pack()

# name_label = ctk.CTkLabel(app, text="Employee Name", width=350)
# name_label.pack()
# name_entry = ctk.CTkEntry(app, placeholder_text='Enter an employee ID', width=350)
# name_entry.pack()

# clearance_label = ctk.CTkLabel(app, text="New Clearance Level", width=350)
# clearance_label.pack()

# clearance_combobox = ctk.CTkComboBox(app, values=["No Clearance", "Low-Level Clearance", "Medium-Level Clearance", "High-Level Clearance"], width=350)
# clearance_combobox.pack()

# reason_label = ctk.CTkLabel(app, text="Reason for Change", width=350)
# reason_label.pack()
# reason_textbox = ctk.CTkTextbox(app, width=350)
# reason_textbox.pack()


# update_button = ctk.CTkButton(app, text="Update")
# update_button.pack(padx=20, pady=20)

# app.mainloop()
