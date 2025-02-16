from ttkbootstrap import Frame, Label, Button, Entry
from tkinter import messagebox

from DataAccessLayer.user_data_access import UserDataAccess
from BusiinessLogicLayer.user_business_logic import UserBusinessLogic
from tkinter.ttk import Treeview, Combobox


# from PresentationLayer.main_view import MainView

class UserManagementFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.user_business_logic = UserBusinessLogic()
        self.main_view = main_view
        self.user_data_access = UserDataAccess()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header = Label(self, text="User Management Page")
        self.header.grid(row=0, column=0, pady=10, columnspan=4)

        self.search_entry = Entry(self)
        self.search_entry.grid(row=1, column=0, columnspan=3, pady=(0, 10), padx=10, sticky="ew")

        self.search_button = Button(self, text="Search", command=self.search)
        self.search_button.grid(row=1, column=3, padx=(0, 10), pady=(0, 10), sticky="w")

        self.active_button = Button(self, text="Active", command=self.active_user)
        self.active_button.grid(row=2, column=0, padx=10, pady=(0, 10))

        self.deactivate_button = Button(self, text="Deactivate", command=self.deactivate_user)
        self.deactivate_button.grid(row=2, column=1, padx=10, pady=(0, 10))

        self.pending_button = Button(self, text="Pending", command=self.pending_user)
        self.pending_button.grid(row=2, column=2, padx=10, pady=(0, 10))

        self.change_role_button = Button(self, text="Change Role", command=self.change_role)
        self.change_role_button.grid(row=2, column=3, padx=10, pady=(0, 10))

        self.user_treeview = Treeview(self, columns=("firstname", "lastname", "username", "status", "role"))
        self.user_treeview.grid(row=3, column=0, columnspan=4, padx=10, pady=(0, 10), sticky="nsew")

        self.user_treeview.heading("#0", text="NO")
        self.user_treeview.heading("firstname", text="First Name")
        self.user_treeview.heading("lastname", text="Last Name")
        self.user_treeview.heading("username", text="Username")
        self.user_treeview.heading("status", text="Status")
        self.user_treeview.heading("role", text="Role")

        self.current_page_number = 0
        self.items_per_page = 6
        self.prev_page_button = Button(self, text="⬅️ prev page", command=self.prev_page)
        self.prev_page_button.grid(row=4, column=1, padx=10, pady=(0, 10))

        self.current_page_label = Label(self, text=f"Page {self.current_page_number + 1}")
        self.current_page_label.grid(row=4, column=2, padx=10, pady=(0, 10))

        self.next_page_button = Button(self, text="next page ➡️", command=self.next_page)
        self.next_page_button.grid(row=4, column=3, padx=10, pady=(0, 10))

        self.current_user = None

        self.row_list = []

    def set_current_user(self, user):
        self.current_user = user
        response = self.user_business_logic.get_user_management_list(user)
        if response.success:
            user_list = response.data
            self.load_data_treeview(user_list)

        else:
            messagebox.showerror("Error", message=response.message)
            self.main_view.switch_frame("login")

    def load_data_treeview(self, user_list):
        for row in self.row_list:
            try:
                self.user_treeview.delete(row)
            except:
                pass
        self.row_list.clear()

        row_number = 1
        for user in user_list:
            row = self.user_treeview.insert("", "end", iid=user.id, text=str(row_number), values=
            (user.first_name,
             user.last_name,
             user.username,
             user.get_status(),
             user.get_role()))
            self.row_list.append(row)
            row_number += 1

    def active_user(self):
        id_list = self.user_treeview.selection()
        self.user_business_logic.activate_user(id_list)
        response = self.user_business_logic.get_user_management_list(self.current_user)
        if response.success:
            user_list = response.data
            self.load_data_treeview(user_list)
        else:
            messagebox.showerror("Error", message=response.message)
            self.main_view.switch_frame("login")

    def deactivate_user(self):
        id_list = self.user_treeview.selection()
        self.user_business_logic.deactivate_user(id_list)
        response = self.user_business_logic.get_user_management_list(self.current_user)
        if response.success:
            user_list = response.data
            self.load_data_treeview(user_list)
        else:
            messagebox.showerror("Error", message=response.message)
            self.main_view.switch_frame("login")

    def pending_user(self):
        id_list = self.user_treeview.selection()
        self.user_business_logic.pending_user(id_list)
        response = self.user_business_logic.get_user_management_list(self.current_user)
        if response.success:
            user_list = response.data
            self.load_data_treeview(user_list)
        else:
            messagebox.showerror("Error", message=response.message)
            self.main_view.switch_frame("login")

    def change_role(self):
        self.values = ("Default User", "Admin")
        self.role_combobox = Combobox(self, values=self.values)
        self.role_combobox.grid(row=2, column=5, padx=10, pady=(0, 10))
        self.submit_button = Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=5, padx=10, pady=(0, 10))

    def submit(self):
        global role_id, role
        try:
            if self.role_combobox.get():
                role = self.role_combobox.get()
                id = self.user_treeview.selection()
                if role == "Default User":
                    role_id = 2
                elif role == "Admin":
                    role_id = 1
                self.user_business_logic.change_role(id, role_id)
                response = self.user_business_logic.get_user_management_list(self.current_user)
                if response.success:
                    user_list = response.data
                    self.load_data_treeview(user_list)
                    self.update_table()
                    self.role_combobox.grid_forget()
                    self.submit_button.grid_forget()

        except ValueError:
            messagebox.showerror("Error", message=f"Role {role} does not exist")
        self.update_table()

    def search(self):
        search = self.search_entry.get()
        user_list = self.user_business_logic.search_user(search)
        self.load_data_treeview(user_list)



    def update_table(self):
        global user_list
        response = self.user_business_logic.get_user_management_list(self.current_user)
        if response.success:
            user_list = response.data

        self.user_treeview.delete(*self.user_treeview.get_children())

        start = self.current_page_number * self.items_per_page
        end = start + self.items_per_page
        row_number = start + 1
        for user in user_list[start:end]:
            self.user_treeview.insert("", "end", iid=user.id, text=str(row_number), values=
            (user.first_name,
             user.last_name,
             user.username,
             user.get_status(),
             user.get_role()))
            row_number += 1

    def next_page(self):
        if (self.current_page_number + 1) * self.items_per_page < len(user_list):
            self.current_page_number += 1
            self.update_table()
            self.current_page_label.config(text=f"Page {self.current_page_number + 1}")

    def prev_page(self):
        if self.current_page_number > 0:
            self.current_page_number -= 1
            self.update_table()
            self.current_page_label.config(text=f"Page {self.current_page_number + 1}")
