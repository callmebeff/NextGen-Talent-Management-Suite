import customtkinter as ctk
import emp_management_screen
import Certification
import Promotion
import clearance_update
import Overtime
import pto_form



class App(ctk.CTk):

    def __init__(self):

        super().__init__()
        self.geometry("600x650")
        self.title('NextGen Talent Management')
        self.grid_columnconfigure(0, weight=1)
        ctk.set_appearance_mode("dark") 

        # Heading
        heading = ctk.CTkLabel(self, text='NextGen Talent Management Suite', font=('CTkFont', 30))
        heading.grid(column=0, row=0, padx=20, pady=5, sticky="ew")

        # Subheading
        subheading = ctk.CTkLabel(self, text='What would you like to do today?', font=('CTkFont', 15))
        subheading.grid(column=0, row=1, padx=20, pady=5, sticky="ew")

        # Button: Add/remove employee
        add_rem_button = ctk.CTkButton(self, text='Add, Remove, or Search for Employee', font=('CTkFont', 15), height=40, command=self.open_employee_management_screen)
        add_rem_button.grid(column=0, row=2, padx=20, pady=15, sticky="ew")

        # Button: Update user clearance level
        clearance_button = ctk.CTkButton(self, text='Update Clearance', font=('CTkFont', 15), height=40, command=self.open_clearance_button)
        clearance_button.grid(column=0, row=3, padx=20, pady=15, sticky="ew")

        # Button: Overtime: Approve/Reject
        overtime_button = ctk.CTkButton(self, text='Manage Overtime Requests', font=('CTkFont', 15), height=40, command=self.open_overtime_button)
        overtime_button.grid(column=0, row=4, padx=20, pady=15, sticky="ew")

        # Button: PTO: Approve/Reject
        pto_button = ctk.CTkButton(self, text='Manage PTO Requests', font=('CTkFont', 15), height=40, command=self.open_pto_button)
        pto_button.grid(column=0, row=5, padx=20, pady=15, sticky="ew")

        # Button: Add/Remove Employee Certification
        cert_button = ctk.CTkButton(self, text='Add/Remove Employee Certification', font=('CTkFont', 15), height=40, command=self.open_cert_button)
        cert_button.grid(column=0, row=6, padx=20, pady=15, sticky="ew")

        # Button: Update Employee Pay Rate
        emp_promotion_button = ctk.CTkButton(self, text='Update Employee Position', font=('CTkFont', 15), height=40, command=self.open_emp_promotion_button)
        emp_promotion_button.grid(column=0, row=7, padx=20, pady=15, sticky="ew")

    def open_employee_management_screen(self):

        emp_management_screen.main()

    def open_clearance_button(self):

        clearance_update.main()

    def open_overtime_button(self):

        Overtime.main()

    def open_pto_button(self):
        
        pto_form.main()
    
    def open_cert_button(self):
        Certification.main()

    def open_emp_promotion_button(self):
        
        Promotion.main()

    
    
app = App()

if __name__ == "__main__":
    app.mainloop()
