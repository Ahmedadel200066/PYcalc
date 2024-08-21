#!/usr/bin/python3

import tkinter as tk

class CalculatorUI:
    def __init__(self, root, controller):
        self.controller = controller

        # Main Display
        self.display = tk.Entry(root, justify='right', font=('Arial', 24), bd=10, insertwidth=4, width=17, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # History Display (Listbox for previous operations)
        self.history = tk.Listbox(root, height=10, width=35, font=('Arial', 12), bd=5)
        self.history.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Adding Buttons
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
            tk.Button(root, text=button, padx=30, pady=20, font=('Arial', 14), 
                      command=lambda b=button: self.button_click(b)).grid(row=row, column=col, padx=5, pady=5)
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

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Calculator")
    controller = None  # Replace with the actual controller instance
    CalculatorUI(root, controller)
    root.mainloop()
