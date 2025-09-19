import tkinter as tk


root = tk.Tk()
root.title("Calculator")
root.geometry("350x600")
root.resizable(False, False)

display_var = tk.StringVar()
display_var.set("0")
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 24), anchor="e", bg="white", bd=5, relief="sunken")
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("M+", 5, 1), ("M-", 5, 2)  # Clear button
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=20)
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    
# Bind commands to buttons (e.g., update_display or calculate)


root.mainloop()

