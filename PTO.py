from tkinter import *
from tkinter import messagebox as mb

main = Tk()
main.title('Welcome to PTO!')
main.geometry('480x480')
main.configure(bg='light gray')

name = Entry(main)
name.pack()


def input():
    greet = "Greetings, " + name.get()
    Label(main, text=greet)
    mb.showinfo('1', greet)

inputButton = Button(main, text="Enter your name", command=input, bg ='green', fg='white')
inputButton.pack()

def PTO():
    response = mb.askyesno("Are you getting PTO?", "Are you sure, " + name.get())
    Label(main,text=response).pack()
    if response == 1:
        mb.showinfo('1', 'Your request has been approved!, ' + name.get())
    else:
        mb.showinfo('1', 'Your request has been denied!, ' + name.get())


responseButton = Button(main, text="Are you getting overtime?", command=PTO, bg ='blue', fg='white')
responseButton.pack()

main.mainloop()
