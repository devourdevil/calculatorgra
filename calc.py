import tkinter as tk
from tkinter import ttk
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graphical Calculator")
        self.geometry("400x500")
        self.resizable(False, False)
        # Create the main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)
        # Create the display
        self.display = ttk.Entry(self.main_frame)
        self.display.pack(fill="x", expand=True)
        # Create the buttons
        self.buttons = []
        for i in range(10):
            button = ttk.Button(self.main_frame, text=str(i))
            button.pack(side="left", fill="both", expand=True)
            self.buttons.append(button)
        # Create the operators
        self.operators = ["+", "-", "*", "/"]
        for operator in self.operators:
            button = ttk.Button(self.main_frame, text=operator)
            button.pack(side="left", fill="both", expand=True)
            self.buttons.append(button)
        # Create the equals button
        self.equals_button = ttk.Button(self.main_frame, text="=")
        self.equals_button.pack(side="left", fill="both", expand=True)
        self.buttons.append(self.equals_button)
        # Create the clear button
        self.clear_button = ttk.Button(self.main_frame, text="C")
        self.clear_button.pack(side="left", fill="both", expand=True)
        self.buttons.append(self.clear_button)
        # Bind the buttons to the appropriate functions
        for button in self.buttons:
            button.bind("<Button-1>", self.on_button_click)
        # Start the main loop
        self.mainloop()
    def on_button_click(self, event):
        # Get the text of the button that was clicked
