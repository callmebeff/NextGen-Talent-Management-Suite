import tkinter as tk


def employeepayrasie():

    thirdwindow= tk.Tk()
    thirdwindow.title("Employee Pay Raise")
    thirdwindow.geometry("500x500")

    username = tk.Label(thirdwindow, text="Username:")
    username.pack(pady=5)
    Managerusername = tk.Entry(thirdwindow)
    Managerusername.pack(pady=5)
    password = tk.Label(thirdwindow, text="Password:")
    password.pack(pady=5)
    Managerpassword = tk.Entry(thirdwindow)
    Managerpassword.pack(pady=5)

    def login():
        # Check if username and password are correct
        usernameadmin = "manager"
        passwordadmin = "password"

        checkusername = Managerusername.get()
        checkpassword = Managerpassword.get()

        if checkusername == usernameadmin and checkpassword == passwordadmin:
            thirdwindow.destroy()

    loginbutton = tk.Button(thirdwindow, text="Login", command=login)
    loginbutton.pack(pady=10)



def mainpage():
    new_window = tk.Tk()
    new_window.title("Blank Page")
    new_window.geometry("500x500")

    # Add a label to the new window


    button2 = tk.Button(new_window, text="Employee Pay Raise", width=20, height=2, font=("Arial", 14), command= employeepayrasie )
    button2.pack(pady=20)

    button3= tk.Button(new_window, text="Certification", width=20, height=2, font=("Arial", 14))
    button3.pack(pady=20)

    button4 = tk.Button(new_window, text="Clearance", width=20, height=2, font=("Arial", 14))
    button4.pack(pady=20)

    button5 = tk.Button(new_window, text="Overtime", width=20, height=2, font=("Arial", 14))
    button5.pack(pady=20)

    button6 = tk.Button(new_window, text="PTO", width=20, height=2, font=("Arial", 14))
    button6.pack(pady=20)

root=tk.Tk()

root.title("Company Name--")
label1=tk.Label(root, text="Welcome!", font=("Arial", 18))
label1.pack(padx=20,pady=20)

#add another label
root.geometry("1000x1000")

button1 = tk.Button(root, text="Continue to Main Page", width=20, height=2, font=("Arial", 14), command= mainpage)
button1.pack(pady=20)


root.mainloop()