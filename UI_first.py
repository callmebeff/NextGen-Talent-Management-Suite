
import tkinter as tk


root = tk.Tk()
root.geometry("300x300")
root.title(" Q&A ")

def Take_input():
	
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	if(INPUT == "120"):
		Output.insert(tk.END, 'Correct')
	else:
		Output.insert(tk.END, "Wrong answer")
	
l = tk.Label(text = "First Name")
inputtxt = tk.Text(root, height = 10,
				width = 25,
				bg = "white")

Output = tk.Text(root, height = 5, 
			width = 25, 
			bg = "light cyan")

Display = tk.Button(root, height = 2,
				width = 20, 
				text ="Show",
				command = lambda:Take_input())



l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

tk.mainloop()
