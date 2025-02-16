from ttkbootstrap import Frame, Label, Entry, Button
from tkinter import messagebox
from BusiinessLogicLayer.user_business_logic import UserBusinessLogic

class RegisterFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)
        self.main_view = main_view

        self.user_business_logic = UserBusinessLogic()

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Register New User")
        self.header.grid(row=0, column=1, sticky='ew')

        self.first_name_label = Label(self, text="First Name")
        self.first_name_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.first_name_entry = Entry(self)
        self.first_name_entry.grid(row=1, column=1, pady=10, padx=(0,20), sticky='ew')

        self.last_name_label = Label(self, text="Last Name")
        self.last_name_label.grid(row=2, column=0,  pady=(0,10), padx=10, sticky='w')

        self.last_name_entry = Entry(self)
        self.last_name_entry.grid(row=2, column=1, pady=(0,10), padx=(0,20), sticky='ew')

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=3, column=0, pady=(0,10), padx=10, sticky='w')

        self.username_entry = Entry(self)
        self.username_entry.grid(row=3, column=1, pady=(0,10), padx=(0,20), sticky='ew')

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=4, column=0, pady=(0,10), padx=10, sticky='w')

        self.password_entry = Entry(self)
        self.password_entry.grid(row=4, column=1, pady=(0,10), padx=(0,20), sticky='ew')

        self.register_button = Button(self, text="Register", command=self.register)
        self.register_button.grid(row=5, column=1, pady=(0,10), padx=(0,20), sticky='w')

        self.back_button = Button(self, text="Back", command=self.back)
        self.back_button.grid(row=6, column=1, pady=(0,10), padx=(0,20), sticky='w')

    def register(self):
        first_name= self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        response= self.user_business_logic.register(first_name, last_name, username, password)
        if response.success:
            messagebox.showinfo("Registered", response.message)
            self.main_view.switch_frame("login")

    def back(self):
        self.main_view.switch_frame("login")