import tkinter as tk

root = tk.Tk()
root.title("Welcome to Beauty Store")
root.geometry("400x400")

def calculate_total_price():
    try:
        selected_product_index=entry_product.curselection()
        if selected_product_index:
            selected_product_index=selected_product_index[0]
            product_name=entry_product.get(selected_product_index)
            units=int(entry_unit_no.get())
            
            # Assuming the prices of each product
            prices={
                "Wild Rose Perfume": 3000,
                "Coconut Shimmer Shampoo": 360,
                "Sweet Melon Cuticle Oil": 100
            }
            
            if product_name in prices:
                unit_price=prices[product_name]
                total_price=unit_price*units
                result_label.config(text=f"Total Price for {units} units of {product_name}: Rs. {total_price:.2f}")
                
            else:
                result_label.config(text="Invalid product selection.")
                
        else:
            result_label.config(text="Please select a product.")
    except ValueError:
        result_label.config(text="ERROR! Please input valid number values.")


# Heading
heading_label = tk.Label(root, text="Welcome to Beauty Store!", font=("Helvetica", 16, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Customer Information
label_name = tk.Label(root, text="Name:")
label_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=2, column=0, padx=10, pady=5, sticky="w")

entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=3, column=0, padx=10, pady=5, sticky="w")

entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1, padx=10, pady=5)

# Product Information
label_product = tk.Label(root, text="Product:")
label_product.grid(row=4, column=0, padx=10, pady=5, sticky="w")

entry_product = tk.Listbox(root, height=3, width=30)
entry_product.insert(1, "Wild Rose Perfume")
entry_product.insert(2, "Coconut Shimmer Shampoo")
entry_product.insert(3, "Sweet Melon Cuticle Oil")
entry_product.grid(row=5, column=0, padx=10, pady=5)

label_unit_no = tk.Label(root, text="Number of Units:")
label_unit_no.grid(row=4, column=1, padx=10, pady=5, sticky="w")

entry_unit_no = tk.Spinbox(root, from_=0, to=10)
entry_unit_no.grid(row=5, column=1, padx=10, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Total Amount", command=calculate_total_price)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
