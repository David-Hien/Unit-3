## Python code
``` python
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

```

## Kivy code
``` kv
Screen:
    size: 500, 500

	MDBoxLayout:
	    # Main screen
	    id: calculator
        orientation: "vertical"
        size_hint: .6, .8
        pos_hint: {"center_x": .5, "center_y": .5}

        # Display
        MDBoxLayout:
            size_hint: 0.8, .18
            pos_hint: {"center_x": .5, "top": 1}

            TextInput:
                id: display
                font_size: 160
                multiline: False
                input_type: "number"
                background_color: 0, 0, 0, 0
                halign: "right"
                valign: "center"

        # Just my name
        MDBoxLayout:
            size_hint: 1, .02

            MDLabel:
                font_size: 30
                halign: "right"
                text: "A calculator by David"

        # Create a grid (a group of MSBoxLayout)
        MDGridLayout:
            orientation: "lr-tb"
            size_hint: 1, .8
            spacing: 8
            padding: 8
            rows: 5

            MDBoxLayout:
                spacing: 8

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 232/255, 214/255, 171/255, 1
                    text: "AC"
                    size_hint: .25, 1
                    on_release: display.text = ""

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 232/255, 214/255, 171/255, 1
                    text: "+/-"
                    size_hint: .25, 1
                    on_release:
                        display.text += "*-1"
                        app.calculate(display.text)

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 232/255, 214/255, 171/255, 1
                    text: "%"
                    size_hint: .25, 1
                    on_release:
                        display.text += "/100"
                        app.calculate(display.text)

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 228/255, 156/255, 60/255, 1
                    text: "/"
                    size_hint: .25, 1
                    on_release: display.text += " / "

            MDBoxLayout:
                spacing: 8

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "7"
                    size_hint: .25, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "8"
                    size_hint: .25, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "9"
                    size_hint: .25, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 228/255, 156/255, 60/255, 1
                    text: "x"
                    size_hint: .25, 1
                    on_release: display.text += " * "

            MDBoxLayout:
                spacing: 8

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "4"
                    size_hint: .25, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "5"
                    size_hint: .25, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "6"
                    size_hint: .25, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 228/255, 156/255, 60/255, 1
                    text: "-"
                    size_hint: .25, 1
                    on_release: display.text += " - "

            MDBoxLayout:
                spacing: 8

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "1"
                    size_hint: .25, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "2"
                    size_hint: .25, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "3"
                    size_hint: .25, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 228/255, 156/255, 60/255, 1
                    text: "+"
                    size_hint: .25, 1
                    on_release: display.text += " + "

            MDBoxLayout:
                spacing: 8

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "0"
                    size_hint: .5, 1
                    on_release: display.text += self.text

                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 0, 0, 0, 0.8
                    text: "."
                    size_hint: .25, 1
                    on_release: display.text += self.text

                # Runs function calculate()
                MDRaisedButton:
                    font_size: 60
	                md_bg_color: 228/255, 156/255, 60/255, 1
                    text: "="
                    size_hint: .25, 1
                    on_release: app.calculate(display.text)
```

## Run
<img width="854" alt="calculator_app_run" src="https://user-images.githubusercontent.com/89367058/155830051-5a318c64-f500-453c-9f56-f46e1bd2e7ce.png">
