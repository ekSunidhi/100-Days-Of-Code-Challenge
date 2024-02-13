import tkinter as tk
from tkinter import messagebox
import re

def validate_input():
    # Regular expressions for validation
    name_pattern = r'^[a-zA-Z\s]+$'
    age_pattern = r'^\d+$'
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    phone_pattern = r'^\d{10}$'

    # Get input values
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()
    phone = entry_phone.get()
    country = entry_country.get()
    selected_option = entry_option.get()

    # Validate input using regular expressions
    if not re.match(name_pattern, name):
        messagebox.showerror("Error", "Invalid Name")
        return

    if not re.match(age_pattern, age):
        messagebox.showerror("Error", "Invalid Age")
        return

    if not re.match(email_pattern, email):
        messagebox.showerror("Error", "Invalid Email")
        return

    if not re.match(phone_pattern, phone):
        messagebox.showerror("Error", "Invalid Phone Number")
        return

    # Display the validated input
    result_label.config(text=f"Name: {name}\nAge: {age}\nEmail: {email}\nPhone: {phone}\nCountry: {country}\nOption: {selected_option}")

# Create the main application window
form_app = tk.Tk()
form_app.title("Simple Form")

# Create and place widgets (labels, entry fields, spinbox, listbox, button)
label_name = tk.Label(form_app, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_name = tk.Entry(form_app)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_age = tk.Label(form_app, text="Age:")
label_age.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_age = tk.Entry(form_app)
entry_age.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(form_app, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_email = tk.Entry(form_app)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_phone = tk.Label(form_app, text="Phone:")
label_phone.grid(row=3, column=0, padx=10, pady=5, sticky="w")

entry_phone = tk.Entry(form_app)
entry_phone.grid(row=3, column=1, padx=10, pady=5)

label_country = tk.Label(form_app, text="Country:")
label_country.grid(row=4, column=0, padx=10, pady=5, sticky="w")

entry_country = tk.Entry(form_app)
entry_country.grid(row=4, column=1, padx=10, pady=5)

label_option = tk.Label(form_app, text="Select Option:")
label_option.grid(row=5, column=0, padx=10, pady=5, sticky="w")

options = ["Option 1", "Option 2", "Option 3"]
entry_option = tk.StringVar()
entry_option.set(options[0])

option_menu = tk.OptionMenu(form_app, entry_option, *options)
option_menu.grid(row=5, column=1, padx=10, pady=5)

validate_button = tk.Button(form_app, text="Validate Input", command=validate_input)
validate_button.grid(row=6, column=0, columnspan=2, pady=10)

result_label = tk.Label(form_app, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Start the Tkinter event loop
form_app.mainloop()
