import tkinter as tk
from math import *
from tkinter import messagebox

# --- Theme Options ---
themes = [
    {"bg": "#f0f0f0", "fg": "#000"},  # Light
    {"bg": "#1e1e1e", "fg": "#fff"},  # Dark
    {"bg": "#e8f5e9", "fg": "#1b5e20"},  # Mint Green
    {"bg": "#ede7f6", "fg": "#4a148c"},  # Grape
    {"bg": "#fff3e0", "fg": "#e65100"},  # Orange
]
current_theme_index = 0

# --- Main Window ---
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x630")
root.resizable(False, False)

# --- Entry Field ---
entry = tk.Entry(root, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20, ipady=10, sticky="we")

# --- Memory Variable ---
memory = ""

# --- Core Functions ---
def add(symbol):
    entry.insert(tk.END, str(symbol))

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def toggle_theme():
    global current_theme_index
    current_theme_index = (current_theme_index + 1) % len(themes)
    theme = themes[current_theme_index]
    apply_theme(theme["bg"], theme["fg"])

def apply_theme(bg_color, fg_color):
    root.configure(bg=bg_color)
    entry.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)
    for btn in buttons:
        btn.configure(bg=bg_color, fg=fg_color, activebackground="#ccc")

def memory_save():
    global memory
    memory = entry.get()

def memory_recall():
    entry.insert(tk.END, memory)

def memory_clear():
    global memory
    memory = ""

# --- Button Layout ---
button_texts = [
    ['C', '⌫', '(', ')', 'MC'],
    ['7', '8', '9', '/', 'M+'],
    ['4', '5', '6', '*', 'M'],
    ['1', '2', '3', '-', 'π'],
    ['0', '.', '%', '+', 'e'],
    ['sin', 'cos', 'tan', 'log', '√'],
    ['^', 'exp', '!', '=', 'Theme']
]

# --- Create Buttons Dynamically ---
buttons = []
for r, row in enumerate(button_texts, 1):
    for c, txt in enumerate(row):
        def command(x=txt):
            if x == "=":
                calculate()
            elif x == "C":
                clear()
            elif x == "⌫":
                backspace()
            elif x == "π":
                add(str(pi))
            elif x == "e":
                add(str(e))
            elif x == "^":
                add("**")
            elif x == "√":
                add("sqrt(")
            elif x == "log":
                add("log10(")
            elif x == "sin":
                add("sin(radians(")
            elif x == "cos":
                add("cos(radians(")
            elif x == "tan":
                add("tan(radians(")
            elif x == "!":
                try:
                    num = int(entry.get())
                    entry.delete(0, tk.END)
                    entry.insert(0, factorial(num))
                except:
                    entry.delete(0, tk.END)
                    entry.insert(0, "Error")
            elif x == "exp":
                add("exp(")
            elif x == "M+":
                memory_save()
            elif x == "M":
                memory_recall()
            elif x == "MC":
                memory_clear()
            elif x == "Theme":
                toggle_theme()
            else:
                add(x)

        btn = tk.Button(root, text=txt, font=("Arial", 16), width=5, height=2, command=command)
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
        buttons.append(btn)

# --- Keyboard Binding ---
def keypress(event):
    key = event.char
    if key in '0123456789.+-*/()':
        add(key)
    elif key == '\r':
        calculate()
    elif key == '\x08':
        backspace()

root.bind("<Key>", keypress)

# --- Grid Weight Configuration ---
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

# --- Apply Initial Theme ---
apply_theme(themes[current_theme_index]["bg"], themes[current_theme_index]["fg"])

# --- Run App ---
root.mainloop()
