import tkinter as tk
from tkinter import messagebox as mb
from login_system import LoginSystem

login_system = LoginSystem('credentials.txt')

def on_entry_click_user(event):
    if user_entry.get() == "User":
        user_entry.delete(0, tk.END)

def on_focus_out_user(event):
    if user_entry.get() == "":
        user_entry.insert(0, "User")

def on_entry_click_password(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, tk.END)

def on_focus_out_password(event):
    if password_entry.get() == "":
        password_entry.insert(0, "Password")

def main():
    username = user_entry.get()
    password = password_entry.get()

    if login_system.authenticate(username, password):
        mb.showinfo("Succès", "Connection réussie!")
    else:
        mb.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

root = tk.Tk()
root.title("Login")

login_title = tk.Label(root, text="BasicLoginSystem", font=('Aial', 52))
login_title.pack(pady=20)

user_entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
user_entry.insert(0, "User")
user_entry.pack()

password_entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
password_entry.insert(0, "Password")
password_entry.pack()

verif_button = tk.Button(root, text="Login", font=('Aial', 24), width=4, height=1, command=main)
verif_button.pack()

user_entry.bind("<FocusIn>", on_entry_click_user)
user_entry.bind("<FocusOut>", on_focus_out_user)

password_entry.bind("<FocusIn>", on_entry_click_password)
password_entry.bind("<FocusOut>", on_focus_out_password)

root.mainloop()