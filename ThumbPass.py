import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
def newPasswrd():
    count = len(passwdC.winfo_children())
    label = tk.Label(passwdC, text=f"Domain #{count}")
    label.pack(anchor=W, padx=10)
    username = tk.Entry(passwdC, text="Username...")
    username.pack(anchor=W, padx=10)
    password = tk.Entry(passwdC, text="Password...")
    password.pack(anchor=W, padx=10)

passwdR = tk.Tk()
passwdR.title("Passwords")
passwdR.geometry("600x400")
passwdF = ttk.Frame(passwdR)
passwdF.pack(fill=BOTH,expand=1)
passwdC = Canvas(passwdF)
passwdC.pack(fill=BOTH)
newpasswordButton = tk.Button(passwdC, text="New Save", command=newPasswrd)
newpasswordButton.pack()
passwdR.withdraw()
#scroll
scroll = tk.Scrollbar(passwdF, orient=VERTICAL, command=passwdC.yview)
passwdC.configure(yscrollcommand=scroll.set)
passwdC.bind('<Configure>', lambda e: passwdC.configure(scrollregion=passwdC.bbox("all")))
second_frame = Frame(passwdC)
passwdC.create_window((1, 1), window=second_frame, anchor="nw")
# validating the login
def login_Check():
    userid = username_entry.get()
    password = password_entry.get()

    #this is a test for login, will be chaged later :)
    if userid == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        passwdR.deiconify()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# login window
parent = tk.Tk()
parent.title("Window")
parent.geometry("400x200")
# labels and box for username
username_label = tk.Label(parent, text="Username")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# label and box for password
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Hides the password 
password_entry.pack()


# login button
login_button = tk.Button(parent, text="Login", command=login_Check)
login_button.pack()


parent.mainloop()


