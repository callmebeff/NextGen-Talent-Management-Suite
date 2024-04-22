from tkinter import *
from tkinter import messagebox as mb

main = Tk()
main.title('Welcome to Overtime')
main.geometry('480x480')
main.configure(bg='light gray')

name = Entry(main)
name.pack()

def input():
    greet = "Greetings, " + name.get()
    Label(main, text=greet)

inputButton = Button(main, text="Enter your name", command=input, bg ='blue', fg='white')
inputButton.pack()

def overtime():

    response = mb.askyesno( 'Are you working overtime?', 'Are you sure, ' + name.get())
    Label(main,text=response).pack()
    if response == 1:
        mb.showinfo('1', 'Your request has been approved!, ' + name.get())
    else:
        mb.showinfo('1', 'Your request has been denied!, ' + name.get())


responseButton = Button(main, text="Are you getting overtime?", command=overtime, bg ='blue', fg='white')
responseButton.pack()


main.mainloop()

