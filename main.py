import tkinter as tk

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

def load_credentials(file_path):
    credentials = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                username, password = line.strip().split(':')
                credentials[username] = password
    except FileNotFoundError:
        print("Fichier Introuvable")
    return credentials

def authenticate(username, password, credentials):
    return credentials.get(username) == password

def main():
    credentials_file = 'credentials.txt'
    credentials = load_credentials(credentials_file)

    if not credentials:
        print("No information")
        return

    username = user_entry.get()
    password = password_entry.get()

    if authenticate(username, password, credentials):
        print("Connexion Réussie")
    else:
        print("User or Password incorect")

root = tk.Tk()
root.title("Login")

login_title = tk.Label(root, text="Login", font=('Aial', 54))
login_title.pack(pady=20)

user_entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
user_entry.insert(0, "User")
user_entry.pack()

password_entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
password_entry.insert(0, "Password")
password_entry.pack()

verif_button = tk.Button(root, text="Login", font=('Aial', 54), width=4, height=1, command=main)
verif_button.pack()

user_entry.bind("<FocusIn>", on_entry_click_user)
user_entry.bind("<FocusOut>", on_focus_out_user)

password_entry.bind("<FocusIn>", on_entry_click_password)
password_entry.bind("<FocusOut>", on_focus_out_password)

root.mainloop()