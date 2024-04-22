import tkinter as tk


class Clearance:
    window = tk.Tk(screenName='Clearance')
    window.geometry('480x360')

    def __init__(self):

        # Introductory prompt. Asking for employee name to change clearance for.

        SearchName = tk.Label(self.window, text='Employee Name: ')
        SearchName.pack(side='top')

        Searchbar = tk.Entry(self.window)
        SearchString = tk.StringVar(Searchbar)
        Searchbar.config(textvariable=SearchString)
        Searchbar.pack(side='top')

        button = tk.Button(self.window, text='Find')
        button.pack(side='top')
        button.config(command=self.add_remove)

    def add_remove(self):

        # Text box asking for input of either adding or removing clearance level.

        SearchName = tk.Label(self.window, text="Add or remove? ")
        SearchName.pack(side='top')

        Searchbar = tk.Entry(self.window)
        SearchString = tk.StringVar(Searchbar)
        Searchbar.config(textvariable=SearchString)
        Searchbar.pack(side='top')

        reg = self.window.register(self.add_remove_check)
        Searchbar.config(validate="key", validatecommand=(reg, '%P'))

    def add_remove_check(self, inputt):

        # Checks the real time input for adding or removing clearance. When either show up a continue box appears.

        if inputt == 'add':
            button = tk.Button(self.window, text='Continue')
            button.pack(side='top')
            button.config(command=self.add)
        if inputt == 'remove':
            button = tk.Button(self.window, text='Continue')
            button.pack(side='top')
            button.config(command=self.remove)
        return True

    def add(self):

        # Adding function after the continue processed this direction. Statement of what clearance to add.

        SearchName = tk.Label(self.window, text="What level of clearance? ")
        SearchName.pack(side='top')

        # Searchbar = tk.Entry(self.window)
        # SearchString = tk.StringVar(Searchbar)
        # Searchbar.config(textvariable=SearchString)
        # Searchbar.pack(side='top')

        value1 = tk.IntVar()
        Check1 = tk.Checkbutton(self.window, text='Level 1', variable=value1, onvalue=1, offvalue=0, height=1)
        value2 = tk.IntVar()
        Check2 = tk.Checkbutton(self.window, text='Level 2', variable=value2, onvalue=1, offvalue=0, height=1)
        value3 = tk.IntVar()
        Check3 = tk.Checkbutton(self.window, text='Level 3', variable=value3, onvalue=1, offvalue=0, height=1)
        value4 = tk.IntVar()
        Check4 = tk.Checkbutton(self.window, text='Level 4', variable=value4, onvalue=1, offvalue=0, height=1)

        Check1.pack()
        Check2.pack()
        Check3.pack()
        Check4.pack()

        button = tk.Button(self.window, text='Confirm')
        button.pack(side='top')
        button.config(command=self.confirmation_a)

    def remove(self):

        # Removing function after the continue processed this direction. Statement of what clearance to remove.

        SearchName = tk.Label(self.window, text="What clearance? ")
        SearchName.pack(side='top')

        # Searchbar = tk.Entry(self.window)
        # SearchString = tk.StringVar(Searchbar)
        # Searchbar.config(textvariable=SearchString)
        # Searchbar.pack(side='top')

        value1 = tk.IntVar()
        Check1 = tk.Checkbutton(self.window, text='Level 1', variable=value1, onvalue=1, offvalue=0, height=1)
        value2 = tk.IntVar()
        Check2 = tk.Checkbutton(self.window, text='Level 2', variable=value2, onvalue=1, offvalue=0, height=1)
        value3 = tk.IntVar()
        Check3 = tk.Checkbutton(self.window, text='Level 3', variable=value3, onvalue=1, offvalue=0, height=1)
        value4 = tk.IntVar()
        Check4 = tk.Checkbutton(self.window, text='Level 4', variable=value4, onvalue=1, offvalue=0, height=1)

        Check1.pack()
        Check2.pack()
        Check3.pack()
        Check4.pack()

        button = tk.Button(self.window, text='Confirm')
        button.pack(side='top')
        button.config(command=self.confirmation_r)

    def confirmation_a(self):

        # Confirmation of added clearance

        SearchName = tk.Label(self.window, text='Clearance has been added')
        SearchName.pack(side='top')

        button = tk.Button(self.window, text='Quit')
        button.pack(side='top')
        button.config(command=quit)

    def confirmation_r(self):

        # Confirmation of removed clearance

        SearchName = tk.Label(self.window, text='Clearance has been removed')
        SearchName.pack(side='top')

        button = tk.Button(self.window, text='Quit')
        button.pack(side='top')
        button.config(command=quit)


Clearance()
tk.mainloop()
