
import customtkinter as ctk
import time

ctk.set_appearance_mode("dark")

def button_callback():
    t_end = time.time() + 1.0462
    while time.time() < t_end:
        progressbar.start()
        app.update()

    progressbar.stop()


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


update_button = ctk.CTkButton(app, text="Update", command=button_callback)
update_button.pack(padx=20, pady=20)

progressbar = ctk.CTkProgressBar(app, orientation="horizontal")
progressbar.configure(mode="determinate")
progressbar.set(0)
progressbar.pack()

app.mainloop()
