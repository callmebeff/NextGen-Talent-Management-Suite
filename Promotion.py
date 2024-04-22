
import customtkinter as ctk

class EmployeeRaise:
    def __init__(self):
        self.page = ctk.CTk(screenName='Employee raise')
        self.page.title("Employee Management")
        self.page.geometry('480x360')

        self.label = ctk.CTkLabel(self.page, text="Enter Employee ID:")
        self.label.pack()

        self.entry = ctk.CTkEntry(self.page, width=300)
        self.entry.pack()

        self.button = ctk.CTkButton(self.page, text="Search", command=self.search_employee)
        self.button.pack()

        self.promotion_label = ctk.CTkLabel(self.page, text="")
        self.promotion_label.pack()

    def search_employee(self):
        employee_id = self.entry.get()

        if employee_id.isdigit():
            self.promotion_label.configure(text="Employee with ID {} is promoted".format(employee_id))
        else:
            self.promotion_label.configure(text="Employee not found")

    def run(self):
        self.page.mainloop()

app = EmployeeRaise()
app.run()