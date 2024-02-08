import tkinter as tk

def compare_discounts():
    try:
        price = float(entry_price.get())
        discount1 = float(entry_discount1.get())
        discount2 = float(entry_discount2.get())

        final_price1 = price * (1 - discount1 / 100)
        final_price2 = price * (1 - discount2 / 100)

        result_label.config(text=f"Final Price with Discount 1: ${final_price1:.2f}\nFinal Price with Discount 2: ${final_price2:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main application window
discount_calculator = tk.Tk()
discount_calculator.title("Discount Comparison Calculator")

label_price = tk.Label(discount_calculator, text="Original Price:")
label_price.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_price = tk.Entry(discount_calculator)
entry_price.grid(row=0, column=1, padx=10, pady=10)

label_discount1 = tk.Label(discount_calculator, text="Discount 1 (%):")
label_discount1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_discount1 = tk.Entry(discount_calculator)
entry_discount1.grid(row=1, column=1, padx=10, pady=10)

label_discount2 = tk.Label(discount_calculator, text="Discount 2 (%):")
label_discount2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_discount2 = tk.Entry(discount_calculator)
entry_discount2.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(discount_calculator, text="Compare Discounts", command=compare_discounts)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(discount_calculator, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
discount_calculator.mainloop()
