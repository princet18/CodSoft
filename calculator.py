import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='#282828')  # Set dark background color

# Entry widgets for numbers
entry_num1 = tk.Entry(root, width=12, font=('Arial', 12), bg='#404040', fg='white', insertbackground='white')
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=12, font=('Arial', 12), bg='#404040', fg='white', insertbackground='white')
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Operation dropdown
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar()
operation_var.set(operations[0])
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.config(font=('Arial', 12), bg='#404040', fg='white')
operation_menu["menu"].config(font=('Arial', 12), bg='#404040', fg='white')
operation_menu.grid(row=0, column=2, padx=10, pady=10)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate, style='TButton')
calculate_button.grid(row=1, column=0, columnspan=3, pady=15)

# Result label
result_label = tk.Label(root, text="Result: ", font=('Arial', 12), bg='#282828', fg='white')
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Configure style for colorful buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 12, 'bold'), foreground='black', background='#61bfad')  # Set button text color, background color, and font size

# Start the GUI
root.mainloop()
 