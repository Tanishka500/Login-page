import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    # Validation logic
    if userid == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Create and place the username label and entry
username_label = tk.Label(parent, text="Username:", bg="#152238", fg="white")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(parent)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:", bg="#152238", fg="white")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Configure the window size and background color
parent.geometry("300x150")
parent.configure(bg="#152238")

# Start the Tkinter event loop
parent.mainloop()