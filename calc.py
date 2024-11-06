#!/bin/bash

import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")

        self.expression = ""
        self.input_field = tk.Entry(root, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.input_field.grid(row=0, column=0, columnspan=4)

        self.create_buttons()
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'sqrt', '^', 'sin',
            'cos', 'tan', '(', ')'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 15), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.expression = ""
            self.input_field.delete(0, tk.END)
        elif char == 'sqrt':
            self.expression = str(math.sqrt(float(self.input_field.get())))
            self.update_input_field()
        elif char in ['sin', 'cos', 'tan']:
            self.calculate_trig(char)
        else:
            self.expression += str(char)
            self.update_input_field()
    def update_input_field(self):
        self.input_field.delete(0, tk.END)
        self.input_field.insert(tk.END, self.expression)

    def calculate(self):
        try:
            self.expression = str(eval(self.expression.replace('^', '**')))
            self.update_input_field()
        except Exception as e:
            self.input_field.delete(0, tk.END)
            self.input_field.insert(tk.END, "Error")

    def calculate_trig(self, func):
        try:
            angle = float(self.input_field.get())
            if func == 'sin':
                self.expression = str(math.sin(math.radians(angle)))
            elif func == 'cos':
                self.expression = str(math.cos(math.radians(angle)))
            elif func == 'tan':
                self.expression = str(math.tan(math.radians(angle)))
            self.update_input_field()
        except Exception as e:
            self.input_field.delete(0, tk.END)
            self.input_field.insert(tk.END, "Error")
if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()


