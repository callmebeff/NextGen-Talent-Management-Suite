import tkinter as tk


class Certification():
    window = tk.Tk(screenName="Certification")
    window.geometry('480x360')

    def __init__(self):

        # Introductory prompt. Asks for the employee who needs a change in certification.

        SearchName = tk.Label(self.window, text="Employee name: ")
        SearchName.pack(side='top')

        Searchbar = tk.Entry(self.window)
        SearchString = tk.StringVar(Searchbar)
        Searchbar.config(textvariable=SearchString)
        Searchbar.pack(side='top')

        button = tk.Button(self.window, text='Find')
        button.pack(side='top')
        button.config(command=self.add_remove)

    def add_remove_check(self, inputt):

        # Checks the real time input for adding or removing certification. When either show up a continue box appears.

        if inputt == 'add':
            button = tk.Button(self.window, text='Continue')
            button.pack(side='top')
            button.config(command=self.add)
        if inputt == 'remove':
            button = tk.Button(self.window, text='Continue')
            button.pack(side='top')
            button.config(command=self.remove)
        return True

    def add_remove(self):

        # Text box asking for input of either adding or removing certification

        SearchName = tk.Label(self.window, text="Add or remove? ")
        SearchName.pack(side='top')

        Searchbar = tk.Entry(self.window)
        SearchString = tk.StringVar(Searchbar)
        Searchbar.config(textvariable=SearchString)
        Searchbar.pack(side='top')

        reg = self.window.register(self.add_remove_check)
        Searchbar.config(validate="key", validatecommand=(reg, '%P'))

    def add(self):

        # Adding function after the continue processed this direction. Statement of what certification to add.

        Searchname = tk.Label(self.window, text="What certification? ")
        Searchname.pack(side='top')

        Searchbar = tk.Entry(self.window)
        SearchString = tk.StringVar(Searchbar)
        Searchbar.config(textvariable=SearchString)
        Searchbar.pack(side='top')

        button = tk.Button(self.window, text='Confirm')
        button.pack(side='top')
        button.config(command=self.confirmation_a)

    def confirmation_a(self):

        # Confirmation of added certification.

        SearchName = tk.Label(self.window, text='Certification has been added')
        SearchName.pack(side='top')

        button = tk.Button(self.window, text='Quit')
        button.pack(side='top')
        button.config(command=quit)

    def confirmation_r(self):

        # Confirmation of removed certification

        SearchName = tk.Label(self.window, text='Certification has been removed')
        SearchName.pack(side='top')

        button = tk.Button(self.window, text='Quit')
        button.pack(side='top')
        button.config(command=quit)

    def remove(self):

        # Removing function after the continue processed this direction. Statement of what certification to remove.

        SearchName = tk.Label(self.window, text="What certification? ")
        SearchName.pack(side='top')

        Searchbar = tk.Entry(self.window)
        SearchString = tk.StringVar(Searchbar)
        Searchbar.config(textvariable=SearchString)
        Searchbar.pack(side='top')

        button = tk.Button(self.window, text='Confirm')
        button.pack(side='top')
        button.config(command=self.confirmation_r)


Certification()
tk.mainloop()
