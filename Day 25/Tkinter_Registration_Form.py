import tkinter as tk
from tkinter import messagebox
import re

def validate_email(email):
    # Regular expression for a simple email verification
    email_regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def validate_password(password):
    # Regular expression for password validation (at least8 characters, one uppercase, one lowercase, and one digit)
    password_regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    return re.match(password_regex, password)

def submit_form():
    name=name_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    age=age_entry.get()
    gender=gender_var.get()
    subscription=subscription_var.get()
    
    # Validate email and password using regular expressions
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email address.")
        return
    
    if not validate_password(password):
        messagebox.showerror("Error", "Invalid password. It must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")
        return
    
    # Perform customer segmentation based on collected information
    # Categorize customers based on age
    if int(age)<25:
        segment="Young"
    elif 25<=int(age)<=40:
        segment="Adult"
    else:
        segment="Senior"
        
    # Display the customer segment
    messagebox.showinfo("Success", f"Registration successful! Customer segment: {segment}")
    
# Create the main window
root=tk.Tk()
root.title("Registration Form")

# Create and place widgets in the window
tk.Label(root, text="Name:").pack(pady=5)
name_entry=tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
email_entry=tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry=tk.Entry(root, show='*')
password_entry.pack(pady=5)

tk.Label(root, text="Age:").pack(pady=5)
age_entry=tk.Entry(root)
age_entry.pack(pady=5)

tk.Label(root, text="Gender:").pack(pady=5)
gender_var=tk.StringVar(root)
gender_var.set("Male")
gender_menu=tk.OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_menu.pack(pady=5)

tk.Label(root, text="Subscription:").pack(pady=5)
subscription_var=tk.StringVar(root)
subscription_var.set("Free")
subscription_menu=tk.OptionMenu(root, subscription_var, "Free", "Basic", "Premium")
subscription_menu.pack(pady=5)

submit_button=tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()