#!/usr/bin/python3

import tkinter as tk

class CalculatorUI:
    def __init__(self, root, controller):
        self.controller = controller

        # Main Display
        self.display = tk.Entry(root, justify='right', font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        # History Display (Listbox for previous operations)
        self.history = tk.Listbox(root, height=10, width=35)
        self.history.grid(row=1, column=0, columnspan=4, sticky='nsew')

        # Adding Buttons (for brevity, just a few buttons here)
        self.create_buttons(root)

    def create_buttons(self, root):
        # Define buttons (e.g., 0-9, +, -, *, /, etc.)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 2
        col = 0
        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: self.button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, button):
        # Example button click handling
        if button == '=':
            result = self.controller.calculate(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            # Add the operation to history
            self.controller.add_to_history(f"{self.display.get()} = {result}")
            self.update_history_display()
        else:
            self.display.insert(tk.END, button)

    def update_history_display(self):
        # Clear the Listbox
        self.history.delete(0, tk.END)
        # Add each item in the history
        for operation in self.controller.get_history():
            self.history.insert(tk.END, operation)
