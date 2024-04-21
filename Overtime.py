from tkinter import *
from tkinter import messagebox as mb

main = Tk()
main.title('Welcome to Overtime')
main.geometry('480x480')



name = input("Greetings, please enter your name: ")


def overtime():

    response = mb.askyesno( 'Are you working overtime?', 'Are you sure, ' + name)
    Label(main,text=response).pack()
    if response == 1:
        mb.showinfo('1', 'Your request has been approved!, ' + name)
    else:
        mb.showinfo('1', 'Your request has been denied!, ' + name )


Button(main, text="Are you getting overtime?", command=overtime, bg ='blue', fg='white').pack()


main.mainloop()

