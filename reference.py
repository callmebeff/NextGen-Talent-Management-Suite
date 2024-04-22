import customtkinter as ctk


class Form(ctk.CTk):

    def __init__(self):

        # label
        heading = ctk.CTkLabel(self, text='Label')
        heading.grid(column=0, row=0, padx=20, pady=5)
