import tkinter as tk
from tkinter import messagebox
from utils import register

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="RegisterPage")
        label.pack(pady=10, padx=10)

        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_entry = tk.Entry(self)
        self.password_entry.pack(pady=5)

        register_button = tk.Button(self, text="Register", command=self.register_user)
        register_button.pack(pady=10)

        login_button = tk.Button(self, text="Login", command=lambda: self.controller.show_frame("LoginPage"))
        login_button.pack(pady=10)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if register(username, password):
            messagebox.showinfo("Success", "Account create successfully")
            self.controller.show_frame("LoginPage")
        else:
            messagebox.showerror("Error", "Username already exists")