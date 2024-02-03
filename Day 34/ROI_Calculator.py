import tkinter as tk

# Create ROI calculation function
def calculate_roi():
    try:
        initial_investment=float(entry_initial_investment.get())
        final_value=float(entry_final_value.get())
        
        roi=((final_value-initial_investment)/initial_investment)*100
        
        result_label.config(text=f"ROI: {roi:.2f}%")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")
        

# Create main window
roi_calculator=tk.Tk()
roi_calculator.title("Return on Investment Calculator")

# Create and place widgets
label_initial_investment=tk.Label(roi_calculator, text="Initial Investment:")
label_initial_investment.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_initial_investment=tk.Entry(roi_calculator)
entry_initial_investment.grid(row=0, column=1, padx=10, pady=10)

label_final_value=tk.Label(roi_calculator, text="Final Value:")
label_final_value.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_final_value=tk.Entry(roi_calculator)
entry_final_value.grid(row=1, column=1, padx=10, pady=10)

calculate_roi_button=tk.Button(roi_calculator, text="Calculate ROI", comman=calculate_roi)
calculate_roi_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label=tk.Label(roi_calculator, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run event loop
roi_calculator.mainloop()