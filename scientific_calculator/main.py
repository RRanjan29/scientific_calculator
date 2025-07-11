import tkinter as tk
from math import *

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

# Entry widget to show calculations
entry = tk.Entry(root, font=('Arial', 20), borderwidth=5, relief="ridge", justify='right')
entry.pack(fill='both', ipadx=8, ipady=15, padx=10, pady=20)

# Function to update expression
def add_to_expression(symbol):
    entry.insert(tk.END, str(symbol))

# Function to evaluate the expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Button layout
buttons = [
    ['7', '8', '9', '/', 'sqrt'],
    ['4', '5', '6', '*', 'log'],
    ['1', '2', '3', '-', 'ln'],
    ['0', '.', '(', ')', '+'],
    ['sin', 'cos', 'tan', 'pow', 'C'],
    ['=']
]

# Create button frame
frame = tk.Frame(root)
frame.pack()

# Define button actions
for row in buttons:
    button_row = tk.Frame(frame)
    button_row.pack(expand=True, fill='both')
    for btn in row:
        def cmd(x=btn):
            if x == '=':
                calculate()
            elif x == 'C':
                clear()
            elif x == 'sqrt':
                add_to_expression('sqrt(')
            elif x == 'log':
                add_to_expression('log10(')
            elif x == 'ln':
                add_to_expression('log(')
            elif x == 'pow':
                add_to_expression('**')
            elif x in ['sin', 'cos', 'tan']:
                add_to_expression(f"{x}(radians(")  # Convert degrees to radians
            else:
                add_to_expression(x)
        tk.Button(button_row, text=btn, font=('Arial', 16), height=2, width=6, command=cmd).pack(side='left', expand=True, fill='both')

# Run the app
root.mainloop()
