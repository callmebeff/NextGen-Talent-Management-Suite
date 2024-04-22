import customtkinter as ctk

class EmployeeManagementScreen(ctk.CTk):

    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)
        self.geometry("600x650")
        self.title('NextGen Talent Management')
        self.grid_columnconfigure(0, weight=1)
        ctk.set_appearance_mode("dark") 

        self.operation_label = ctk.CTkLabel(self, text='Operation Selection')
        self.operation_label.grid(column=0, row=0, padx=10, pady=5, sticky='w')

        default = ""
        options = ["Onboarding", "Offboarding", "Employee Lookup"]
        self.dropdown = ctk.CTkComboBox(self, variable=default, values=options, command=self.show_hide_fields, width=200)
        self.dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Form fields
        self.id_label = ctk.CTkLabel(self, text='Employee ID')
        self.id_entry = ctk.CTkEntry(self, width=400)
        self.first_name_label = ctk.CTkLabel(self, text='First Name')
        self.first_name_entry = ctk.CTkEntry(self, width=400)
        self.last_name_label = ctk.CTkLabel(self, text='Last Name')
        self.last_name_entry = ctk.CTkEntry(self, width=400)
        self.address_label = ctk.CTkLabel(self, text='Address')
        self.address_entry = ctk.CTkEntry(self, width=400)
        self.position_label = ctk.CTkLabel(self, text='Position')
        self.position_entry = ctk.CTkEntry(self, width=400)
        self.reason_label = ctk.CTkLabel(self, text="Reason for Leaving")
        self.reason_entry = ctk.CTkTextbox(self, width=400)


    def show_hide_fields(self, option):

        selection = self.dropdown.get()

        if selection == "Onboarding":

            self.id_label.grid(column=0, row=1, padx=10, pady=5, sticky='w')
            self.id_entry.grid(column=1, row=1, padx=10, pady=5, sticky='w')
            self.first_name_label.grid(column=0, row=2, padx=10, pady=5, sticky='w')
            self.first_name_entry.grid(column=1, row=2, padx=10, pady=5, sticky='w')
            self.last_name_label.grid(column=0, row=3, padx=10, pady=5, sticky='w')
            self.last_name_entry.grid(column=1, row=3, padx=10, pady=5, sticky='w')
            self.address_label.grid(column=0, row=4, padx=10, pady=5, sticky='w')
            self.address_entry.grid(column=1, row=4, padx=10, pady=5, sticky='w')
            self.position_label.grid(column=0, row=5, padx=10, pady=5, sticky='w')
            self.position_entry.grid(column=1, row=5, padx=10, pady=5, sticky='w')
            self.reason_label.grid_remove()
            self.reason_entry.grid_remove()
            save_button = ctk.CTkButton(self, text='Save')
            save_button.grid(column=0, row=20, padx=10, pady=5, sticky='ew', columnspan=2)

        elif selection == "Offboarding":

            self.id_label.grid(column=0, row=1, padx=10, pady=5, sticky='w')
            self.id_entry.grid(column=1, row=1, padx=10, pady=5, sticky='w')
            self.first_name_label.grid(column=0, row=2, padx=10, pady=5, sticky='w')
            self.first_name_entry.grid(column=1, row=2, padx=10, pady=5, sticky='w')
            self.last_name_label.grid(column=0, row=3, padx=10, pady=5, sticky='w')
            self.last_name_entry.grid(column=1, row=3, padx=10, pady=5, sticky='w')
            self.address_label.grid(column=0, row=4, padx=10, pady=5, sticky='w')
            self.address_entry.grid(column=1, row=4, padx=10, pady=5, sticky='w')
            self.position_label.grid(column=0, row=5, padx=10, pady=5, sticky='w')
            self.position_entry.grid(column=1, row=5, padx=10, pady=5, sticky='w')
            self.reason_label.grid(column=0, row=6, padx=10, pady=5, sticky='w')
            self.reason_entry.grid(column=1, row=6, padx=10, pady=5, sticky='w')
            save_button = ctk.CTkButton(self, text='Save')
            save_button.grid(column=0, row=20, padx=10, pady=5, sticky='ew', columnspan=2)

        elif selection == "Employee Lookup":
            
            self.id_label.grid(column=0, row=1, padx=10, pady=5, sticky='w')
            self.id_entry.grid(column=1, row=1, padx=10, pady=5, sticky='w')
            self.first_name_label.grid_remove()
            self.first_name_entry.grid_remove()
            self.last_name_label.grid_remove()
            self.last_name_entry.grid_remove()
            self.address_label.grid_remove()
            self.address_entry.grid_remove()
            self.position_label.grid_remove()
            self.position_entry.grid_remove()
            self.reason_label.grid_remove()
            self.reason_entry.grid_remove()
            search_button = ctk.CTkButton(self, text='Search')
            search_button.grid(column=0, row=20, padx=10, pady=5, sticky='ew', columnspan=2)



def main():

    emp_management_screen = EmployeeManagementScreen()
    emp_management_screen.mainloop()



# def show_hide_fields(option):

#     selection = dropdown.get()

#     if selection == "Onboarding":

#         id_label.grid(column=0, row=1, padx=10, pady=5, sticky='w')
#         id_entry.grid(column=1, row=1, padx=10, pady=5, sticky='w')
#         first_name_label.grid(column=0, row=2, padx=10, pady=5, sticky='w')
#         first_name_entry.grid(column=1, row=2, padx=10, pady=5, sticky='w')
#         last_name_label.grid(column=0, row=3, padx=10, pady=5, sticky='w')
#         last_name_entry.grid(column=1, row=3, padx=10, pady=5, sticky='w')
#         address_label.grid(column=0, row=4, padx=10, pady=5, sticky='w')
#         address_entry.grid(column=1, row=4, padx=10, pady=5, sticky='w')
#         position_label.grid(column=0, row=5, padx=10, pady=5, sticky='w')
#         position_entry.grid(column=1, row=5, padx=10, pady=5, sticky='w')
#         reason_label.grid_remove()
#         reason_entry.grid_remove()
#         save_button = ctk.CTkButton(app, text='Save')
#         save_button.grid(column=0, row=20, padx=10, pady=5, sticky='ew', columnspan=2)

#     elif selection == "Offboarding":

#         id_label.grid(column=0, row=1, padx=10, pady=5)
#         id_entry.grid(column=1, row=1, padx=10, pady=5)
#         first_name_label.grid(column=0, row=2, padx=10, pady=5)
#         first_name_entry.grid(column=1, row=2, padx=10, pady=5)
#         last_name_label.grid(column=0, row=3, padx=10, pady=5)
#         last_name_entry.grid(column=1, row=3, padx=10, pady=5)
#         address_label.grid(column=0, row=4, padx=10, pady=5)
#         address_entry.grid(column=1, row=4, padx=10, pady=5)
#         position_label.grid(column=0, row=5, padx=10, pady=5)
#         position_entry.grid(column=1, row=5, padx=10, pady=5)
#         reason_label.grid(column=0, row=6, padx=10, pady=5)
#         reason_entry.grid(column=1, row=6, padx=10, pady=5)
#         save_button = ctk.CTkButton(app, text='Save')
#         save_button.grid(column=0, row=20, padx=10, pady=5, sticky='ew', columnspan=2)

#     elif selection == "Employee Lookup":
        
#         id_label.grid(column=0, row=1, padx=10, pady=5)
#         id_entry.grid(column=1, row=1, padx=10, pady=5)
#         first_name_label.grid_remove()
#         first_name_entry.grid_remove()
#         last_name_label.grid_remove()
#         last_name_entry.grid_remove()
#         address_label.grid_remove()
#         address_entry.grid_remove()
#         position_label.grid_remove()
#         position_entry.grid_remove()
#         reason_label.grid_remove()
#         reason_entry.grid_remove()
#         search_button = ctk.CTkButton(app, text='Search')
#         search_button.grid(column=0, row=20, padx=10, pady=5, sticky='ew', columnspan=2)


# # app = ctk.CTk()
# # app.title("Employee Management Form")
# # app.geometry('450x450')
# # app.grid_columnconfigure(0, weight=1)
# # ctk.set_appearance_mode("dark")


# # operation_label = ctk.CTkLabel(app, text='Operation Selection')
# # operation_label.grid(column=0, row=0, padx=10, pady=5, sticky='w')

# # Dropdown menu
# default = ""
# options = ["Onboarding", "Offboarding", "Employee Lookup"]
# dropdown = ctk.CTkComboBox(app, variable=default, values=options, command=show_hide_fields)
# dropdown.grid(row=0, column=1, padx=10, pady=5)
# # dropdown.bind("<<ComboboxSelected>>", show_hide_fields)

# Form fields
# id_label = ctk.CTkLabel(app, text='Employee ID')
# id_entry = ctk.CTkEntry(app)
# first_name_label = ctk.CTkLabel(app, text='First Name')
# first_name_entry = ctk.CTkEntry(app)
# last_name_label = ctk.CTkLabel(app, text='Last Name')
# last_name_entry = ctk.CTkEntry(app)
# address_label = ctk.CTkLabel(app, text='Address')
# address_entry = ctk.CTkEntry(app)
# position_label = ctk.CTkLabel(app, text='Position')
# position_entry = ctk.CTkEntry(app)
# reason_label = ctk.CTkLabel(app, text="Reason for Leaving")
# reason_entry = ctk.CTkTextbox(app)


# if __name__ == "__main__":
#     app.mainloop()



