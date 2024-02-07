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

# Create and place widgets (labels, entry fields, buttons)
# (Similar structure as previous examples with additional entry fields)

# Start the Tkinter event loop
discount_calculator.mainloop()
