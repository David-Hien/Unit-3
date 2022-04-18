# Unit 3 Project 

## Table of Contents

1. [Planning](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-a-planning)
2. [Design](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-b-solution-overview)
3. [Development](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-c-development)
5. [Evaluation]
6. [Apendix]()
7. [Citation](https://github.com/David-Hien/Unit-3/blob/main/Project.md#citation)


## Criteria A: Planning 

### Definition of Problem

My client's name is Nagisa Sato. She has a collection of shoes - both the ones currently in her possesion and the ones she would like to have. At the moment, my client does not use any application or system to organize her collection. For that reason, Nagisa wishes for an application that can store the data of her shoes and is able to organize it base on different factors as to help her keep a better track of the collection. In addition, my client wants to have a "wishlist" - list of shoes that she wants to add to her collection in the future - that is also organized to find the next pair to buy.

### Proposed Solution

My proposed solution is to create an application that uses Python as the main programming language, Kivymd Library for the GUI (Graphical User Interface), and SQLAlchemy to manipulate the database. The app will consist of a Login/Register screen, a page to show the shoe collections, and another page for the user to manually edit the collections. Two other additions are:
- a search function that can assist the user navigate large databases
- a sort function that rearrange the collection based on factors (eg. name, price, color) of the user's choice

***Python***

I choose Python as the programming language for the following reasons. Firstly, Python is widely used in various areas thanks to it simple syntax and focus on natural language, making it beginner friendly at the same time not losing much versitility. According to Stackoverflow blog by David Robinson<sup>[[1]](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)</sup>, Python is the fastest growing programming language, and is predicted to be the most in-demand language in 2020, which was proven to be true - according to PYPL PopularitY of Programming Language<sup>[[2]](https://pypl.github.io/PYPL.html)</sup>, Python ranked first with the most tutorial video views on Google. Also, because I'm familiar with this language, the process of developing this product will be more efficient. Secondly, Python supports OOP (Object-oriented programming). For this application, I believe it is more effective to approach using OOP, because it makes it much easier to navigate and understand the code, which means easy to locate errors, high code-reusability, and other developers - who might work on the project after you - won't have a hard time.

***Kivymd Library***

The Kivymd Library is an open-source library used as a framework for cross-platform applications<sup>[[3]](https://kivymd.readthedocs.io/en/latest/)</sup>. It is a tool for creating GUI (Graphical User Interface) for applications, which serves as a communicator between the input (keyboard, mouse, multitouch events, etc.) and the program, as well as between the program and the output (screen). This is an essential part of any application because it exponentially increases the app's usability and desirabilty - easier to understand, use, and charming visual aesthetics.

***SQLAlchemy and ORM***

To operate the database, I choose to use SQLAlchemy. It's a declarative query language that is common for relational databases. Also, when identifying the issue and planing out the ER (Entity Relation) diagram and table, I noticed that classes have relation to each other. In this instance, a user has many shoes, and a shoe only has one user. In order to effectively address this, I choose to use an ORM (Object Relational Mapper) supported language, and among them, SQLAlchemy is highly compatible with Python that allows for Python construct<sup>[[4]](https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/)</sup>.

### Success Criteria

1. User is able to Create, Add, Edit, Delete data in the table
2. The application has a login and register page
3. The login information and database is secured and the password is hashed
4. Function to sort the table based on different factors
5. Function to search specific information from a defined range
6. Uses OOP (Object-oriented programming)

### Evidence

https://user-images.githubusercontent.com/89367058/160220880-46e9df1f-ca53-4b7a-97ad-bdec87c4fe62.mov  


## Criteria B: Solution Overview

### Solution Sketch

### Flow Diagrams

### System Diagram

### UML Diagram

![Untitled Diagram drawio](https://user-images.githubusercontent.com/89367058/161373661-df4e5e95-5beb-4503-a19b-4fa82f9b2499.png)


### ER Diagram

![Extended_ER_diagram](https://user-images.githubusercontent.com/89367058/161374040-9c06bf97-d484-4f60-9fd7-bb012408d727.png)


### ER Table (example)

**Table: User**
| username | email                           | password |
|----------|---------------------------------|----------|
| nagi     | 2023.nagisa.sato@uwcisak.jp     | naginagi |
| david    | 2023.hien.minh.trinh@uwcisak.jp | david032 |

**Table: Shoes**
| brand  | model       | size | material               | color       | price |
|--------|-------------|------|------------------------|-------------|-------|
| Adidas | Ultra-boost | 44.5 | thermoplastic urethane | black/white | 300   |
| Nike   | Jordan 1    | 39   | leather                | white       | 5000  |


### Test Plan



## Criteria C: Development

## Apendix (as of 11:40AM, Apr 18)

### database_models.py
``` python
# Import database_models
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base

# Call Base
Base = declarative_base()


class users(Base):
    """ This class represents the users table"""

    # Create new table for users
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    # Attributes of users, used for input
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Shoes(Base):
    """ This class represents the Shoes table"""

    # Create new table for Shoes
    __tablename__ = "Shoes"
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    model = Column(String(255))
    size = Column(String(255))
    material = Column(String(255))
    color = Column(String(255))
    price = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))

    # Attributes of Shoes, used for input
    def __int__(self, brand, model, size, material, color, price, user_id):
        self.brand = brand
        self.model = model
        self.size = size
        self.material = material
        self.color = color
        self.price = price
        self.user_id = user_id


# Creates the database
db_engine = create_engine("sqlite:///orm_database.db")
Base.metadata.create_all(db_engine)

```

### main.py
``` python
# Import kivymd for GUI design
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen

# Import from SQLAlchemy the function to connect to db
from sqlalchemy import create_engine

# Function to create a session
from sqlalchemy.orm import sessionmaker
from database_models import Base, users, Shoes

# Import function for hashing password
from password_hash import encrypt_password, check_password

# Creates the database
db_engine = create_engine("sqlite:///orm_database.db")
Base.metadata.create_all(db_engine)
Base.metadata.bind = db_engine
db_session = sessionmaker(bind=db_engine)
session = db_session()


class LoginScreen(MDScreen):
    """ This class creates the login screen"""

    # This method takes the login information then cross check it with the database log the user in
    def try_login(self):
        # Store the values inputed
        email_entered = self.ids.email_input.text
        pass_entered = self.ids.password_input.text

        # Stops the method if either inputs is empty
        if not email_entered or not pass_entered:
            print("Input required")
            return

        # Scan the database for the account with the same email
        current_user = (session.query(users).
                        filter(users.email == email_entered).
                        first())

        # Stops the method if the user doesn't exist
        if not current_user:
            print("User doesn't exist")
            return

        # Check if the password stored in the database is the same as the one inputed
        if check_password(pass_entered, current_user.password):
            self.parent.current = "HomeScreen"

    # Go to Register screen
    def register_screen(self):
        self.parent.current = "RegisterScreen"


class RegisterScreen(MDScreen):
    """ This class creates the register screen"""

    # This method creates a new user account and add it to the database
    def register(self):
        # Store the values inputed
        username_entered = self.ids.username_input.text
        email_entered = self.ids.email_input.text
        pass_entered = self.ids.password_input.text

        # Stops method if input left blank
        if not username_entered or not email_entered or not pass_entered:
            print("Input required")
            return

        # Hash the password (for security)
        pass_hashed = encrypt_password(pass_entered)

        # Update the database with the new account
        new_user = users(username_entered, email_entered, pass_hashed)
        session.add(new_user)

        # Tries to update the database, fail if account already exist (same email)
        try:
            session.commit()
            session.close()
            self.parent.current = "HomeScreen"
        except Exception:
            print("Email already linked to an account.")

    # Go to Login screen
    def login_screen(self):
        self.parent.current = "LoginScreen"


class HomeScreen(MDScreen):
    """ This class creates the home screen"""

    # This method runs when loading the window
    def on_pre_enter(self, *args):
        # Store the current logged in user's email
        current_user_email = self.parent.ids.LoginScreen.ids.email_input.text

        # Query the user
        current_user = (session.query(users).
                        filter(users.email == current_user_email).
                        first())

        # Welcome message
        self.ids.name_label.text = f"Welcome, {current_user.username}"

    # Go to Login screen
    def logout(self):
        self.parent.current = "LoginScreen"

    # Go to Table screen
    def table_screen(self):
        self.parent.current = "TableScreen"

    # Go to Add or Remove item screen
    def add_remove(self):
        self.parent.current = "AddRemoveScreen"


class AddRemoveScreen(MDScreen):
    """ This class creates the add remove item screen"""

    # Go back to welcome/main screen
    def back_to_home(self):
        self.parent.current = "HomeScreen"


class TableScreen(MDScreen):
    """ This class creates the table screen"""
    data_tables = None

    # Go back to welcome/main screen
    def back_to_home(self):
        self.parent.current = "HomeScreen"

    # This method queries the Shoes table and return its data as a list
    def get_shoes(self):
        # Store the current logged in user's email
        current_user_email = self.parent.ids.LoginScreen.ids.email_input.text

        # Query the user
        current_user = (session.query(users).
                        filter(users.email == current_user_email).
                        first())

        # Query the Shoes table for rows with matching Foreign key to the user
        query = session.query(Shoes).filter(Shoes.user_id == current_user.id)
        session.close()

        # Append the results into a list then return it
        result = []
        for q in query:
            result.append([q.id, q.brand, q.model, q.size, q.material, q.color, q.price])

        return result

    def on_pre_enter(self, *args):
        # List of shoes (and attributes)
        result = self.get_shoes()

        # Creates the table
        self.data_tables = MDDataTable(
            size_hint=(.9, .5),
            pos_hint={"center_x": .5, "center_y": .5},
            check=True,
            column_data=[
                ("id", dp(20), self.sort_id),
                ("brand", dp(35), self.sort_brand),
                ("model", dp(35), self.sort_model),
                ("size", dp(20), self.sort_size),
                ("material", dp(30), self.sort_material),
                ("color", dp(20), self.sort_color),
                ("price", dp(20), self.sort_price)
            ],
            row_data=result,
        )
        self.data_tables.bind(on_check_press=self.check_pressed)
        self.add_widget(self.data_tables)

    # These methods are toggles used for sorting the table
    def get_sort(self, data, column_number):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][column_number]
            )
        )

    # Sort based on id number
    def sort_id(self, data):
        return self.get_sort(data, 0)

    # Sort based on brand name
    def sort_brand(self, data):
        return self.get_sort(data, 1)

    # Sort based on model
    def sort_model(self, data):
        return self.get_sort(data, 2)

    # Sort based on size
    def sort_size(self, data):
        return self.get_sort(data, 3)

    # Sort based on material
    def sort_material(self, data):
        return self.get_sort(data, 4)

    # Sort based on color
    def sort_color(self, data):
        return self.get_sort(data, 5)

    # Sort based on price
    def sort_price(self, data):
        return self.get_sort(data, 6)

    # This method takes the value on the selected row of the table
    # and prints it on the according TextEdit fields
    def check_pressed(self, table, row):
        # Assign variables to store the values of the selected row
        shoe_id, brand, size, model, material, color, price = row

        # Print the values on the TextEdit fields
        self.ids.shoe_id.text = shoe_id
        self.ids.brand.text = brand
        self.ids.model.text = model
        self.ids.size.text = size
        self.ids.material.text = material
        self.ids.color.text = color
        self.ids.price.text = price

    # This method runs when the button "Save" is pressed
    # Takes the values in the TextEdit fields and update it in the database
    def edit_save(self):
        # Assign variables to store the values of each TextEdit fields
        updated_brand = self.ids.brand.text
        updated_model = self.ids.model.text
        updated_size = self.ids.size.text
        updated_material = self.ids.material.text
        updated_color = self.ids.color.text
        updated_price = self.ids.price.text

        if (not updated_brand or
                not updated_model or
                not updated_size or
                not updated_material or
                not updated_color or
                not updated_price):
            print("Input missing")
            return

        # Format the values correctly for update
        updated_row = {Shoes.brand: updated_brand,
                       Shoes.model: updated_model,
                       Shoes.size: updated_size,
                       Shoes.material: updated_material,
                       Shoes.color: updated_color,
                       Shoes.price: updated_price}

        # Update the Shoes table with the new data
        session.query(Shoes). \
            filter(Shoes.id == self.ids.shoe_id.text). \
            update(updated_row)

        session.commit()

        # Refresh the table and TextEdit fields
        self.update_table()
        self.clear()

    # This method update the table on display
    def update_table(self):
        # List of shoes (and attributes)
        result = self.get_shoes()

        # Updates the table
        self.data_tables.update_row_data(
            None, result
        )

    def clear(self):
        # Clear all TextEdit fields
        self.ids.shoe_id.text = ""
        self.ids.brand.text = ""
        self.ids.model.text = ""
        self.ids.size.text = ""
        self.ids.material.text = ""
        self.ids.color.text = ""
        self.ids.price.text = ""


class app_GUI(MDApp):
    """ This class creates the GUI for the app"""

    def build(self):
        return


gui = app_GUI()
gui.run()

```

### app_GUI.kv
``` .kv
ScreenManager:
    id: scr_manager

    LoginScreen:
        name: "LoginScreen"
        id: LoginScreen

    RegisterScreen:
        name: "RegisterScreen"
        id: RegisterScreen

    HomeScreen:
        name: "HomeScreen"
        id: HomeScreen

    AddRemoveScreen:
        name: "AddRemoveScreen"
        id: AddRemoveScreen

    TableScreen:
        name: "TableScreen"
        id: TableScreen

# Define the login screen
<LoginScreen>:
    MDBoxLayout:
        orientation: "vertical"

        FitImage:
            source: 'shoez_login_background.jpg'
            opacity: .85

    MDCard:
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        size: "400dp", "500dp"
        elevation: 10
        # For colors: red, green, blue, alpha
        md_bg_color: 229/255, 170/255, 140/255, 0.6
        radius: 20, 20, 20, 20

        MDBoxLayout:
            orientation: "vertical"
            size_hint: .8, .8
            pos_hint: {"center_x": .5, "center_y": .5}
            spacing: dp(15)
            padding: [dp(20), dp(60)]

            MDLabel:
                id: name_label
                text: "Shoez"
                halign: "center"
                font_style: "H1"
                color: 1, 1, 1, 1

            MDTextField:
                id: email_input
                hint_text: "email"
                color: 1, 1, 1, 1
                required: True
                icon_right: "email"

            MDTextField:
                id: password_input
                hint_text: "password"
                color: 1, 1, 1, 1
                password: True
                required: True
                icon_right: "eye-off"

            MDRaisedButton:
                id: login_button
                text: "Login"
                pos_hint: {"center_x": .5}
                size_hint: .6, None
                padding_y: 20
                on_release:
                    root.try_login()
                    password_input.text=''

            MDRaisedButton:
                id: register_button
                text: "Register"
                pos_hint: {"center_x": .5}
                size_hint: .6, None
                padding_y: 20
                md_bg_color: 0, 0, 0, .3
                on_release:
                    root.register_screen()
                    email_input.text=''
                    password_input.text=''


<RegisterScreen>
    MDBoxLayout:
        orientation: "vertical"

        FitImage:
            source: 'shoez_login_background.jpg'
            opacity: .85

    MDCard:
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        size: "400dp", "500dp"
        elevation: 10
        # For colors: red, green, blue, alpha
        md_bg_color: 229/255, 170/255, 140/255, 0.6
        radius: 20, 20, 20, 20

        MDBoxLayout:
            orientation: "vertical"
            size_hint: .8, 1
            pos_hint: {"center_x": .5, "center_y": .5}
            spacing: dp(15)
            padding: [dp(20), dp(40)]

            MDLabel:
                id: name_label
                text: "Shoez"
                halign: "center"
                font_style: "H1"
                color: 1, 1, 1, 1

            MDTextField:
                id: username_input
                hint_text: "username"
                color: 1, 1, 1, 1
                required: True
                icon_right: "account"

            MDTextField:
                id: email_input
                hint_text: "email"
                color: 1, 1, 1, 1
                required: True
                icon_right: "email"

            MDTextField:
                id: password_input
                hint_text: "password"
                color: 1, 1, 1, 1
                password: True
                required: True
                icon_right: "eye-off"

            MDRaisedButton:
                id: register_button
                text: "Register"
                pos_hint: {"center_x": .5}
                size_hint: .6, None
                padding_y: 20
                on_release:
                    root.register()
                    username_input.text=''
                    email_input.text=''
                    password_input.text=''

            MDRaisedButton:
                id: login_button
                text: "Login"
                pos_hint: {"center_x": .5}
                size_hint: .6, None
                padding_y: 20
                md_bg_color: 0, 0, 0, .3
                on_release:
                    root.login_screen()
                    username_input.text=''
                    email_input.text=''
                    password_input.text=''


<HomeScreen>:
    BoxLayout:
        orientation: "vertical"
        size: 1000, 700

        MDLabel:
            id: name_label
            text: ""
            halign: "center"
            font_style: "H1"
            color: 0, 0, 0, 1

        MDRaisedButton:
            id: logout_button
            text: "Logout"
            pos_hint: {"center_x": .5}
            size_hint: .6, None
            padding_y: 20
            md_bg_color: 0, 0, 0, .3
            on_release:
                root.logout()

        MDRaisedButton:
            id: logout_button
            text: "Table"
            pos_hint: {"center_x": .5}
            size_hint: .6, None
            padding_y: 20
            md_bg_color: 0, 0, 0, .3
            on_release:
                root.table_screen()

        MDRaisedButton:
            id: add_item
            text: "Add Item"
            pos_hint: {"center_x": .5}
            size_hint: .6, None
            padding_y: 20
            md_bg_color: 0, 0, 0, .3
            on_release:
                root.add_remove()


<AddRemoveScreen>:
    BoxLayout:
        orientation: "vertical"
        size: 1000, 700

        MDLabel:
            id: name_label
            text: "Add Item"
            halign: "center"
            font_style: "H1"
            color: 0, 0, 0, 1

        MDRaisedButton:
            id: back_to_home_button
            text: "Go Back"
            pos_hint: {"center_x": .5, "top": .2}
            size_hint: .6, None
            padding_y: 20
            md_bg_color: 0, 0, 0, .3
            on_release:
                root.back_to_home()


<TableScreen>
    MDRaisedButton:
        id: back_to_home_button
        text: "Go Back"
        pos_hint: {"right": .15, "top": .95}
        size_hint: None, None
        md_bg_color: 0, 0, 0, .3
        on_release:
            root.back_to_home()

    MDBoxLayout:
        orientation: "horizontal"
        pos_hint: {"center_x": .5, "top": .3}
        size_hint: .9, .3

        MDLabel:
            text: "Edit entry"
            font_size: 30
            pos_hint : {"left": 0, "center_y": .5}
            size_hint: .08, .3

        MDLabel:
            id: shoe_id
            pos_hint : {"left": .1, "center_y": .5}
            size_hint : .03, .3

        MDTextField:
            id: brand
            hint_text : "brand"
            pos_hint : {"left": .15, "center_y": .5}
            size_hint : .1, .3

        MDTextField:
            id: model
            hint_text : "model"
            pos_hint : {"left": .26, "center_y": .5}
            size_hint : .1, .3

        MDTextField:
            id: size
            hint_text : "size"
            pos_hint : {"left": .37, "center_y": .5}
            size_hint : .05, .3

        MDTextField:
            id: material
            hint_text : "material"
            pos_hint : {"left": .44, "center_y": .5}
            size_hint : .1, .3

        MDTextField:
            id: color
            hint_text : "color"
            pos_hint : {"left": .56, "center_y": .5}
            size_hint : .1, .3

        MDTextField:
            id: price
            hint_text : "price"
            pos_hint : {"left": .67, "center_y": .5}
            size_hint : .05, .3

        MDRaisedButton:
            text: "Save"
            size_hint: .1, .2
            pos_hint : {"left": .74, "center_y": .5}
            on_release:
                root.edit_save()

        MDRaisedButton:
            text: "Clear"
            md_bg_color : 1, .1, .1, 1
            size_hint: .1, .2
            pos_hint : {"left": .9, "center_y": .5}
            on_release:
                root.clear()

```

## Citation
1. Robinson, D. (2017, September 6). The incredible growth of python. Stack Overflow Blog. Retrieved March 22, 2022, from https://stackoverflow.blog/2017/09/06/incredible-growth-python/ 
2. Carbonnelle, P. (n.d.). PYPL popularity of Programming Language index. index. Retrieved March 22, 2022, from https://pypl.github.io/PYPL.html 
3. Rodríguez, A. (2021). Welcome to KIVYMD's documentation!. Welcome to KivyMD's documentation! - KivyMD 1.0.0.dev0 documentation. Retrieved March 26, 2022, from https://kivymd.readthedocs.io/en/latest/ 
4. Gantan, X. (2014, March 12). Overview of SQLALCHEMY's expression language and Orm queries. Python Central. Retrieved March 27, 2022, from https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/ 
