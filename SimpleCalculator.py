import tkinter as tk


class CalculatorFunctions:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Error"


class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        self.result_var = tk.StringVar()
        self.create_widgets()

        # Bind the Enter key to perform the calculation
        self.master.bind('<Return>', lambda event: self.on_button_click('='))
        # Bind the Backspace key to the backspace function
        self.master.bind('<BackSpace>', lambda event: self.on_backspace())

    def validate_entry(self, char):
        # Allow only digits, '.', '+', '-', '*', '/'
        return char.isdigit() or char in ['.', '+', '-', '*', '/']

    def create_widgets(self):
        # Entry widget to display and edit the expression
        entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 16), bd=5, insertwidth=2, width=14,
                         justify='right', validate='key', validatecommand=(self.master.register(self.validate_entry), '%S'))
        entry.grid(row=1, column=0, columnspan=3)

        # Buttons for digits and operations
        buttons = [
            ('<-', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('C', 5, 1), ('=', 5, 2), ('+', 5, 3),
        ]

        # Create and place buttons
        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, font=('Arial', 14), height=2, width=4,
                               command=lambda t=text: self.on_button_click(t) if t != '<-' else self.on_backspace())
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == 'C':
            # Clear the entry
            self.result_var.set('')
        elif button_text == '=':
            try:
                # Evaluate the expression and set the result
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                # Handle invalid expressions
                self.result_var.set('Error')
        elif button_text == '<-':
            # Backspace functionality
            self.on_backspace()
        else:
            # Append the button text to the current expression
            self.result_var.set(current_text + button_text)

    def on_backspace(self):
        current_text = self.result_var.get()
        # Remove the last character from the entry
        self.result_var.set(current_text[:-1])


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
