
import customtkinter as ctk
import time

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("400x480")
app.title('Employee Clearance Update')

id_label = ctk.CTkLabel(app, text="Employee ID", width=200)
id_label.pack()
id_entry = ctk.CTkEntry(app, placeholder_text='Enter a name', width=350)
id_entry.pack()

name_label = ctk.CTkLabel(app, text="Employee Name", width=350)
name_label.pack()
name_entry = ctk.CTkEntry(app, placeholder_text='Enter an employee ID', width=350)
name_entry.pack()

clearance_label = ctk.CTkLabel(app, text="New Clearance Level", width=350)
clearance_label.pack()

clearance_combobox = ctk.CTkComboBox(app, values=["No Clearance", "Low-Level Clearance", "Medium-Level Clearance", "High-Level Clearance"], width=350)
clearance_combobox.pack()

reason_label = ctk.CTkLabel(app, text="Reason for Change", width=350)
reason_label.pack()
reason_textbox = ctk.CTkTextbox(app, width=350)
reason_textbox.pack()


update_button = ctk.CTkButton(app, text="Update")
update_button.pack(padx=20, pady=20)

app.mainloop()
