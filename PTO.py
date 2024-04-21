from tkinter import *
from tkinter import messagebox as mb


main = Tk()
main.title('Welcome to PTO')
main.geometry('480x480')
main.configure(bg='black')

name = input("Greetings!, please enter your name: ")

def PTO():

    response = mb.askyesno("Are you getting PTO?", "Are you sure, " + name)
    Label(main,text=response).pack()
    if response == 1:
        mb.showinfo('1', 'Your request has been approved!, ' + name)
    else:
        mb.showinfo('1', 'Your request has been denied!, ' + name )


respond = Button(main, text="Are you getting PTO?", command=PTO, bg='green', fg='white').pack()


main.mainloop()
