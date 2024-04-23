import customtkinter as ctk
import random


# Generate sample OT request
first_names = ['Adam', 'Paul', 'Mark']
last_names = ['Smith', 'Johnson', 'Doe']

random_first = f'{random.choice(first_names)}'
random_last = f'{random.choice(last_names)}'
emp_id = random.randint(100000, 999999)
hours = random.randint(1, 7)

class OvertimeApproval(ctk.CTk):

    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)
        self.geometry("600x650")
        self.title('Overtime Approval Screen')
        self.grid_columnconfigure(0, weight=1)
        ctk.set_appearance_mode("dark")

        heading = ctk.CTkLabel(self, text='Overtime Approval Screen', font=('CTkFont', 30))
        heading.grid(column=0, row=0, padx=10, pady=5, columnspan=2)

        self.id_label = ctk.CTkLabel(self, text='Employee ID')
        self.id_label.grid(column=0, row=1, padx=10, pady=5, sticky='w')
        self.id_display = ctk.CTkLabel(self, text=f'{emp_id}')
        self.id_display.grid(column=1, row=1, padx=10, pady=5, sticky='w')

        self.first_name_label = ctk.CTkLabel(self, text='First Name')
        self.first_name_label.grid(column=0, row=2, padx=10, pady=5, sticky='w')
        self.first_name_display = ctk.CTkLabel(self, text=f'{random_first}')
        self.first_name_display.grid(column=1, row=2, padx=10, pady=5, sticky='w')

        self.last_name_label = ctk.CTkLabel(self, text='Last Name')
        self.last_name_label.grid(column=0, row=3, padx=10, pady=5, sticky='w')
        self.last_name_display = ctk.CTkLabel(self, text=f'{random_last}')
        self.last_name_display.grid(column=1, row=3, padx=10, pady=5, sticky='w')

        self.ot_amount_label = ctk.CTkLabel(self, text='Overtime Hours (amount)')
        self.ot_amount_label.grid(column=0, row=4, padx=10, pady=5, sticky='w')
        self.ot_amount_entry = ctk.CTkLabel(self, text=f'{hours} hour(s)')
        self.ot_amount_entry.grid(column=1, row=4, padx=10, pady=5, sticky='w')

        self.operation_label = ctk.CTkLabel(self, text='Approve/Reject')
        self.operation_label.grid(column=0, row=5, padx=10, pady=5, sticky='w')
        
        default = ""
        options = ["Approve", "Reject"]
        self.operation = ctk.CTkComboBox(self, variable=default, values=options, width=200)
        self.operation.grid(column=1, row=5, padx=10, pady=5, sticky="w")

        self.save_button = ctk.CTkButton(self, text='Save', command=self.ot_button_press)
        self.save_button.grid(column=0, row=20, columnspan=2, sticky='ew', padx=10, pady=25)

        self.response = ctk.CTkLabel(self, text='')
        self.response.grid(column=0,row=22, columnspan=2, padx=10, pady=25)

    def ot_button_press(self):
            
        if self.operation.get() == "Approve":
            self.response.configure(text=f"{random_first} {random_last}'s overtime request has been approved")

        elif self.operation.get() == "Reject":
            self.response.configure(text=f"{random_first} {random_last}'s overtime request has been rejected")
        else:
            self.response.configure(text=f"Please select an option")









def main():

    ot_screen = OvertimeApproval()
    ot_screen.mainloop()


if __name__ == "__main__":
    main()

"""




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

"""