import tkinter as tk
from tkinter import messagebox
from utils import login

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="LoginPage")
        label.pack(pady= 10, padx=20)

        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_entry = tk.Entry(self)
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self, text="Login", command=self.check_login)
        login_button.pack(pady=10)

        register_button = tk.Button(self, text="Register", command=lambda: controller.show_frame("RegisterPage"))
        register_button.pack()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if login(username, password):
            self.controller.show_frame("MainPage")
        else:
            messagebox.showerror("Error", "Invalid credentials")