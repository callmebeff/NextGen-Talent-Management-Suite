import customtkinter as ctk
import random

first_names = ['Adam', 'Paul', 'Mark']
last_names = ['Smith', 'Johnson', 'Doe']

random_first = f'{random.choice(first_names)}'
random_last = f'{random.choice(last_names)}'
emp_id = random.randint(100000, 999999)


class OvertimeApproval(ctk.CTk):

    def __init__(self,*args, **kwargs):

        super().__init__(*args, **kwargs)
        self.geometry("600x650")
        self.title('Overtime Approval Screen')
        self.grid_columnconfigure(0, weight=1)
        ctk.set_appearance_mode("dark")


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

        self.operation_label = ctk.CTkLabel(self, text='Approve/Reject')
        self.operation_label.grid(column=0, row=5, padx=10, pady=5, sticky='w')

        default = ""
        options = ["Approve", "Reject", "Employee Lookup"]
        self.operation = ctk.CTkComboBox(self, variable=default, values=options, command=self.manage_ot, width=200)
        self.operation.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.response = ctk.CTkLabel(self, text='')
        self.response.grid(column=0,row=22, columnspan=2)




    def manage_ot(self, option):
            
        if self.operation.get() == "Approve":
            self.promotion_label.configure(text="Request approved")









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