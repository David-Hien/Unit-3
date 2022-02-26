from kivymd.app import MDApp


class hw_calculator(MDApp):
    """ This class creates the calculator GUI """

    # Function creates the GUI
    def build(self):
        return

    # Function calculates the expression currently on the display
    def calculate(self, calculation: str):
        if calculation:
            try:
                # Turn string into an expression to calculate, then revert back to string to display
                self.root.ids.display.text = str(eval(calculation))

            # Return either Syntax Error or Math Error if expression has wrong format or zero division
            except SyntaxError:
                self.root.ids.display.text = "Syntax Error"
            except ZeroDivisionError:
                self.root.ids.display.text = "Math Error"
            except NameError:
                self.root.ids.display.text = "Syntax Error"


calculator = hw_calculator()
calculator.run()
