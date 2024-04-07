from tkinter import *

root = Tk()
root.geometry("300x300")
root.title(" Q&A ")

def Take_input():
	
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	if(INPUT == "120"):
		Output.insert(END, 'Correct')
	else:
		Output.insert(END, "Wrong answer")
	
l = Label(text = "First Name")
inputtxt = Text(root, height = 10,
				width = 25,
				bg = "white")

Output = Text(root, height = 5, 
			width = 25, 
			bg = "light cyan")

Display = Button(root, height = 2,
				width = 20, 
				text ="Show",
				command = lambda:Take_input())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
