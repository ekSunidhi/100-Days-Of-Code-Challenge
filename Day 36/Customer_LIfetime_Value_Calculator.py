import tkinter as tk

def calculate_clv():
    try:
        average_purchase_value=float(entry_avg_purchase.get())
        purchase_frequency=float(entry_purchase_frequency.get())
        customer_lifespan=float(entry_lifespan.get())
        retention_rate=float(entry_retention_rate.get())
        
        clv=(average_purchase_value*purchase_frequency*customer_lifespan)/(1-retention_rate)
        
        result_label.config(text=f"Estimated CLV: Rs.{clv:.2f}")
    
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")
        
        
    
# Create the main application window
app=tk.Tk()
app.title("Customer Lifetime Value Calculator")
  
# Create and place widgets 
label_avg_purchase=tk.Label(app, text="Average Purchase Value:")
label_avg_purchase.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
entry_avg_purchase=tk.Entry(app)
entry_avg_purchase.grid(row=0, column=1, padx=10, pady=10)
    
label_purchase_frequency=tk.Label(text="Purchase Frequency per Year:")
label_purchase_frequency.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_purchase_frequency=tk.Entry(app)
entry_purchase_frequency.grid(row=1, column=1, padx=10, pady=10)

label_lifespan=tk.Label(text="Customer Lifespan (Years):")
label_lifespan.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_lifespan=tk.Entry(app)
entry_lifespan.grid(row=2, column=1, padx=10, pady=10)

label_retention_rate=tk.Label(text="Retention Rate (%):")
label_retention_rate.grid(row=3, column=0, padx=10, pady=10, sticky="w")

entry_retention_rate=tk.Entry(app)
entry_retention_rate.grid(row=3, column=1, padx=10, pady=10)

calculate_button=tk.Button(app, text="Calculate CLV", comman=calculate_clv)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label=tk.Label(app, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
app.mainloop()