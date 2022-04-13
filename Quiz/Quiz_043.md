## Code
``` python
# Import kivymd for GUI design
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    """ This class creates the Login screen"""
    pass


class HomeScreen(MDScreen):
    """ This class creates the Home/Main screen"""
    pass


class ListScreen(MDScreen):
    """ This class creates the List screen"""
    pass


class NewItemScreen(MDScreen):
    """ This class creates the New item screen"""
    pass


class Quiz_043(MDApp):
    """ This class creates the GUI for the app"""
    def build(self):
        return


# Starts the app
gui = Quiz_043()
gui.run()

```

## Kivy
``` .kv
ScreenManager:
    id: scr_manager

    LoginScreen:
        name: "LoginScreen"

    HomeScreen:
        name: "HomeScreen"

    ListScreen:
        name: "ListScreen"

    NewItemScreen:
        name: "NewItemScreen"


<LoginScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDLabel:
            id: name_label
            text: "Login Screen"
            halign: "center"
            font_style: "H1"

        MDRaisedButton:
            id: login_button
            text: "Login"
            font_style: "H1"
            pos_hint: {"center_x": .5}
            size_hint: .6, None
            padding_y: 20
            on_release:
                root.parent.current = "HomeScreen"


<HomeScreen>:
    BoxLayout:
        orientation: "vertical"

        MDLabel:
            id: name_label
            text: "Home Screen"
            halign: "center"
            font_style: "H1"

        MDRaisedButton:
            id: logout_button
            text: "Logout"
            pos_hint: {"center_x": .5}
            size_hint: .6, None
            padding_y: 20
            md_bg_color: 0, 0, 0, .3
            on_release:
                root.parent.current = "LoginScreen"

        MDRaisedButton:
            id: list_button
            text: "List"
            pos_hint: {"center_x": .5}
            size_hint: .6, None
            padding_y: 20
            md_bg_color: 0, 0, 0, .3
            on_release:
                root.parent.current = "ListScreen"

        MDRaisedButton:
            id: add_item
            text: "Add Item"
            pos_hint: {"center_x": .5}
            size_hint: .6, None
            padding_y: 20
            md_bg_color: 0, 0, 0, .3
            on_release:
                root.parent.current = "NewItemScreen"

<ListScreen>:
    BoxLayout:
        orientation: "vertical"

        MDLabel:
            id: name_label
            text: "List"
            halign: "center"
            font_style: "H1"

        MDRaisedButton:
            id: back_to_home_button
            text: "Go Back"
            pos_hint: {"center_x": .5}
            size_hint: .6, None
            padding_y: 20
            md_bg_color: 0, 0, 0, .3
            on_release:
                root.parent.current = "HomeScreen"


<NewItemScreen>:
    BoxLayout:
        orientation: "vertical"

        MDLabel:
            id: name_label
            text: "Add Item"
            halign: "center"
            font_style: "H1"

        MDRaisedButton:
            id: back_to_home_button
            text: "Go Back"
            pos_hint: {"center_x": .5}
            size_hint: .6, None
            padding_y: 20
            md_bg_color: 0, 0, 0, .3
            on_release:
                root.parent.current = "HomeScreen"

```

## Run

https://user-images.githubusercontent.com/89367058/163185710-a5bd32da-74e5-4e08-a1de-98ff73d287af.mov

