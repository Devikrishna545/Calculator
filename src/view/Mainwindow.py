import tkinter as tk
from ..model.special_calc import SpecialCalculator
from ..model.simple_calc import SimpleCalculator

# Initialize calculator instances
simple_calc = SimpleCalculator()
special_calc = SpecialCalculator()

root = tk.Tk()
root.title("Calculator")
root.geometry("350x600")
root.resizable(False, False)

display_var = tk.StringVar()
display_var.set("0")
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 24), anchor="e", bg="white", bd=5, relief="sunken")
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

first_num = 0
operation=None
mem = 0

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("M+", 5, 1), ("M-", 5, 2)  # Clear button
]

# Bind commands to buttons (e.g., update_display or calculate)
def on_button_click(value): 
    global first_num, operation, mem
    current = display_var.get()

    if value.isdigit() or value==".":
        if current == "0" and value != ".":
            display_var.set(value)
        elif current != "0":
            display_var.set(current + value)
    elif value == "C":
        display_var.set('0')
        first_num = 0
        operation = None
    elif value in ["+", "-", "*", "/"]:
        first_num = float(current)
        operation = value
        display_var.set(operation)
    elif value == "=" :
        if operation:
            second_num = float(current)
            if operation == "+": 
                result= simple_calc.add(first_num,second_num)           
            elif operation == "-":
                result= simple_calc.sub(first_num,second_num) 
                
            elif operation == "/":
                if second_num ==  0:
                    result = "Error"
                else:
                   result= simple_calc.div(first_num,second_num)                 
            elif operation == "*":
                result= simple_calc.mul(first_num,second_num) 
            display_var.set(result)
            operation=None
    elif value == "M+":
        mem = special_calc.mem_add(mem, float(current))
    elif value == "M-":
        mem = special_calc.mem_sub(mem, float(current))

for (text, row, col) in buttons:
   button = tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=20, command=lambda t=text: on_button_click(t))
   button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)       


def run():
    root.mainloop()

if __name__ == "__main__":
    run()