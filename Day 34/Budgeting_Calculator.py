import tkinter as tk

# Create the function to calculate the budget
def calculate_budget():
    try:
        income=float(entry_income.get())
        expenses=float(entry_expenses.get())
        
        savings=income-expenses
        
        result_label.config(text=f"Remaining Budget: Rs. {savings:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main application window
budget_calculator=tk.Tk()
budget_calculator.title("Budgeting Calculator")

# Create widgets
label_income=tk.Label(budget_calculator, text="Income:")
label_income.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_income=tk.Entry(budget_calculator)
entry_income.grid(row=0, column=1, padx=10, pady=10)

label_expenses=tk.Label(text="Expenses:")
label_expenses.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_expenses=tk.Entry(budget_calculator)
entry_expenses.grid(row=1, column=1, padx=10, pady=10)

calculate_budget_button=tk.Button(budget_calculator, text="Calculate Budget", command=calculate_budget)
calculate_budget_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label=tk.Label(budget_calculator, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the mainloop
budget_calculator.mainloop()
