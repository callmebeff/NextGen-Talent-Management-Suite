
import customtkinter as ctk

class EmployeeRaise(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x650")
        self.title("Employee Management")
        self.geometry('480x360')

        self.label = ctk.CTkLabel(self, text="Enter Employee ID:")
        self.label.pack()

        self.entry = ctk.CTkEntry(self, width=300)
        self.entry.pack()

        self.button = ctk.CTkButton(self, text="Search", command=self.search_employee)
        self.button.pack()

        self.promotion_label = ctk.CTkLabel(self, text="")
        self.promotion_label.pack()

    def search_employee(self):
        employee_id = self.entry.get()

        if employee_id.isdigit():
            self.promotion_label.configure(text="Employee with ID {} has been promoted to manager".format(employee_id))
        else:
            self.promotion_label.configure(text="Employee not found")


def main():

    app = EmployeeRaise()
    app.mainloop()