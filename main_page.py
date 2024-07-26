import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="BasicAccountSysteme")
        label.pack(pady=10, padx=10)

        logout_button = tk.Button(self, text="Logout", command=lambda: controller.show_frame("LoginPage"))
        logout_button.pack()