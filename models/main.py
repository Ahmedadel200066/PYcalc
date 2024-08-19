#!/usr/bin/python3

import tkinter as tk
from ui import CalculatorUI
from controller import CalculatorController

def main():
    # Create the main application window
    root = tk.Tk()
    root.title("PyCalc")

    # Initialize the Controller
    controller = CalculatorController()

    # Initialize the UI and pass the controller to it
    CalculatorUI(root, controller)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
