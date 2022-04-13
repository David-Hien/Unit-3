## Python Code
``` python
from kivymd.app import MDApp


class Quiz_037(MDApp):
    """ This class creates the GUI for USD-YEN converter"""
    def build(self):
        return

    # This method takes the input in USD then converts it into YEN
    def convert(self):
        # This command tries to run the code, however, in the case the calculation cannot happen due to error
        # displays "Error" message
        try:
            self.root.ids.output.text = str(int(self.root.ids.input.text) * 115)
        except ValueError:
            self.root.ids.output.text = "Error"


# Run the app
converter = Quiz_037()
converter.run()

```

## Kivy code
``` kv
Screen:
    size: 500, 500

    MDBoxLayout:
        orientation: "horizontal"
        size_hint: .8, .25
        pos_hint: {"center_x": .5, "center_y": .5}
        spacing: 100

        MDTextField:
            id: input
            hint_text: "USD"
            mode: "rectangle"
            size_hint: .25, 1

        MDRaisedButton:
            size_hint: .3, .9
            center_y: .5
            font_size: 70
            md_bg_color: 159/255, 206/255, 189/255, 1
            text_color: 0, 0, 0, 1
            text: "Convert"
            on_release: app.convert()

        MDTextField:
            id: output
            text: ""
            hint_text: "YEN"
            mode: "rectangle"
            size_hint: .25, 1

```

## Run


https://user-images.githubusercontent.com/89367058/156957183-8e12f8b7-6c18-4511-b105-c20b2cccbfb2.mov

