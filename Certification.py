import tkinter as tk
import customtkinter as ctk


class Certification(ctk.CTk):


    def __init__(self, *args, **kwargs):

        # Introductory prompt. Asks for the employee who needs a change in certification.
        super().__init__(*args, **kwargs)
        self.title('Certification Update')
        ctk.set_appearance_mode("dark")
        self.geometry('600x650')

        SearchName = ctk.CTkLabel(self, text="Employee name: ")
        SearchName.grid(column=0, row=0, padx=2, pady=5)

        Searchbar = ctk.CTkEntry(self)
        SearchString = ctk.StringVar(Searchbar)
        Searchbar.configure(textvariable=SearchString)
        Searchbar.grid(column=1, row=0, padx=2, pady=5)

        button = ctk.CTkButton(self, text='Find')
        button.grid(column=2, row=0, padx=2, pady=5, sticky='e')
        button.configure(command=self.add_remove)

    def add_remove_check(self, inputt):

        # Checks the real time input for adding or removing certification. When either show up a continue box appears.
        inputt = inputt.lower()
        if inputt == 'add':
            button = ctk.CTkButton(self, text='Continue')
            button.grid(column=2, row=1, padx=2, pady=5)
            button.configure(command=self.add)
        if inputt == 'remove':
            button = ctk.CTkButton(self, text='Continue')
            button.grid(column=2, row=1, padx=2, pady=5)
            button.configure(command=self.remove)
        return True

    def add_remove(self):

        # Text box asking for input of either adding or removing certification

        SearchName = ctk.CTkLabel(self, text="Add or remove? ")
        SearchName.grid(column=0, row=1, padx=2, pady=5)

        Searchbar = ctk.CTkEntry(self)
        SearchString = ctk.StringVar(Searchbar)
        Searchbar.configure(textvariable=SearchString)
        Searchbar.grid(column=1, row=1, padx=2, pady=5)

        reg = self.register(self.add_remove_check)
        Searchbar.configure(validate="key", validatecommand=(reg, '%P'))

    def add(self):

        # Adding function after the continue processed this direction. Statement of what certification to add.

        Searchname = ctk.CTkLabel(self, text="What certification? ")
        Searchname.grid(column=0, row=2, padx=2, pady=5)

        Searchbar = ctk.CTkEntry(self)
        SearchString = ctk.StringVar(Searchbar)
        Searchbar.configure(textvariable=SearchString)
        Searchbar.grid(column=1, row=2, padx=2, pady=5)

        button = ctk.CTkButton(self, text='Confirm')
        button.grid(column=2, row=2, padx=2, pady=5)
        button.configure(command=self.confirmation_a)

    def confirmation_a(self):

        # Confirmation of added certification.

        SearchName = ctk.CTkLabel(self, text='Certification has been added')
        SearchName.grid(column=0, row=3, pady=5, columnspan=3)

        button = ctk.CTkButton(self, text='Quit')
        button.grid(column=0, row=4, pady=5, columnspan=3)
        button.configure(command=quit)

    def confirmation_r(self):

        # Confirmation of removed certification

        SearchName = ctk.CTkLabel(self, text='Certification has been removed')
        SearchName.grid(column=0, row=3, pady=5, columnspan=3)

        button = ctk.CTkButton(self, text='Quit')
        button.grid(column=0, row=4, pady=5, columnspan=3)
        button.configure(command=quit)

    def remove(self):

        # Removing function after the continue processed this direction. Statement of what certification to remove.

        SearchName = ctk.CTkLabel(self, text="What certification? ")
        SearchName.grid(column=0, row=2)

        Searchbar = ctk.CTkEntry(self)
        SearchString = ctk.StringVar(Searchbar)
        Searchbar.configure(textvariable=SearchString)
        Searchbar.grid(column=1, row=2)

        button = ctk.CTkButton(self, text='Confirm')
        button.grid(column=2, row=2)
        button.configure(command=self.confirmation_r)




def main():

    cert = Certification()
    cert.mainloop()
