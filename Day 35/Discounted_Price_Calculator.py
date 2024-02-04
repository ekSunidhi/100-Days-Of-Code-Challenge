import tkinter as tk

def calculate_discount():
    try: 
        original_price=float(entry_original_price.get())
        discount_rate=float(entry_discount_rate.get())
        
        discount_amount=original_price*(discount_rate/100)
        discounted_price=original_price-discount_amount
        
        result_label.config(text=f"Discounted Price: Rs.{discounted_price: .2f}")
    
    except ValueError:
        result_label.config(text="Invalid input. Please entervalid numbers.")
        
# Create the main application window
app=tk.Tk()
app.title("Retail Calculator")

# Create and place widgets
label_original_price=tk.Label(app, text="Original Price:")
label_original_price.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_original_price=tk.Entry(app)
entry_original_price.grid(row=0, column=1, padx=10, pady=10)

label_discount_rate=tk.Label(app, text="Discount Rate (%):")
label_discount_rate.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_discount_rate=tk.Entry(app)
entry_discount_rate.grid(row=1, column=1, padx=10, pady=10)

calculate_button=tk.Button(app, text="Calculate Discount", command=calculate_discount)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label=tk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
app.mainloop()