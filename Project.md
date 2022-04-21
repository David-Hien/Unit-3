# Unit 3 Project 

## Table of Contents

1. [Planning](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-a-planning)
2. [Design](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-b-solution-overview)
3. [Development](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-c-development)
5. [Functionality](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-d-functionality)
6. [Apendix](https://github.com/David-Hien/Unit-3/blob/main/Project.md#apendix-as-of-314pm-apr-18)
7. [Citation](https://github.com/David-Hien/Unit-3/blob/main/Project.md#citation)


## Criteria A: Planning 

### Definition of Problem

My client's name is Nagisa Sato. She has a collection of shoes. At the moment, my client does not use any application or system to organize her collection. For that reason, Nagisa wishes for an application that can store the data of her shoes and is able to organize it based on different factors to help her keep a better track of the collection.

### Proposed Solution

My proposed solution is to create an application that uses Python as the main programming language, Kivymd Library for the GUI (Graphical User Interface), and SQLAlchemy to manipulate the database. The app will consist of a Login/Register screen, a page to show the shoe collections, and another page for the user to manually edit the collections. The table can be sorted based on factors (eg. name, price, color) of the user's choice.

#### Python

I choose Python as the programming language for the following reasons. Firstly, Python is widely used in various areas thanks to its simple syntax and focus on natural language, making it beginner friendly at the same time not losing much versatility. According to Stackoverflow blog by David Robinson<sup>[[1]](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)</sup>, Python is the fastest growing programming language, and is predicted to be the most in-demand language in 2020, which was proven to be true - according to PYPL PopularitY of Programming Language<sup>[[2]](https://pypl.github.io/PYPL.html)</sup>, Python ranked first with the most tutorial video views on Google. Also, because I'm familiar with this language, the process of developing this product will be more efficient. Secondly, Python supports OOP (Object-oriented programming). For this application, I believe it is more effective to approach using OOP, because it makes it much easier to navigate and understand the code, which means easy to locate errors, high code-reusability, and other developers - who might work on the project after you - won't have a hard time.

#### Kivymd Library

The Kivymd Library is an open-source library used as a framework for cross-platform applications<sup>[[3]](https://kivymd.readthedocs.io/en/latest/)</sup>. It is a tool for creating GUI (Graphical User Interface) for applications, which serves as a communicator between the input (keyboard, mouse, multitouch events, etc.) and the program, as well as between the program and the output (screen). This is an essential part of any application because it exponentially increases the app's usability and desirability - easier to understand, use, and charming visual aesthetics.

#### SQLAlchemy and ORM

To operate the database, I choose to use SQLAlchemy. It's a declarative query language that is common for relational databases. Also, when identifying the issue and planning out the ER (Entity Relation) diagram and table, I noticed that classes have relation to each other. In this instance, a user has many shoes, and a shoe only has one user. In order to effectively address this, I choose to use an ORM (Object Relational Mapper) supported language, and among them, SQLAlchemy is highly compatible with Python that allows for Python construct<sup>[[4]](https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/)</sup>.

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

![IMG_1232](https://user-images.githubusercontent.com/89367058/163813430-44550b42-912f-4e20-bf2b-59c13366dded.JPG)

***Figure 1:*** Sketch of purposed solution's wireframe

***Fig.1*** is a wireframe showing a total of 4 screens - ```LoginScreen```, ```RegisterScreen```, ```HomeScreen```, and ```TableSscreen``` - connected via buttons.
- The ```LoginScreen``` and ```RegisterScreen``` are connected via the "Register"/"Login" buttons.
- From the ```RegisterScreen```, registering will automatically send the user to the ```LoginScreen```.
- From the ```LoginScreen```, logging in will automatically send the user to the ```HomeScreen```.
- From the ```HomeScreen```, the user can access the ```TableScreen``` via "Table", or chose go back to the ```LoginScreen``` via "Logout".
- From the ```TableScreen```, return to the ```HomeScreen``` via "Back"

### System Diagram

![system_diagram](https://user-images.githubusercontent.com/89367058/163824670-2851f64a-4b74-4ea5-b221-2a2f30bce573.png)

***Figure 2:*** System Diagram. Shows the input, output, and the process in between.

### Flow Diagrams

### UML Diagram

![Untitled Diagram drawio](https://user-images.githubusercontent.com/89367058/161373661-df4e5e95-5beb-4503-a19b-4fa82f9b2499.png)

***Figure 6:*** UML diagram for the database. Shows the attributes of each class/tables and the relation of the two: ***one*** user can have ***n*** Shoes.

### ER Diagram

![Extended_ER_diagram](https://user-images.githubusercontent.com/89367058/161374040-9c06bf97-d484-4f60-9fd7-bb012408d727.png)

***Figure 7:*** ER diagram for the database. Visualized version of the database.

### ER Table (example)

**Table: User**
| username | email                           | password |
|----------|---------------------------------|----------|
| nagi     | 2023.nagisa.sato@uwcisak.jp     | naginagi |
| david    | 2023.hien.minh.trinh@uwcisak.jp | david032 |

***Figure 8:*** ER table 1. User table with some examples.

**Table: Shoes**
| brand  | model       | size | material               | color       | price |
|--------|-------------|------|------------------------|-------------|-------|
| Adidas | Ultra-boost | 44.5 | thermoplastic urethane | black/white | 300   |
| Nike   | Jordan 1    | 39   | leather                | white       | 5000  |

***Figure 9:*** ER table 2. Shoes table with some examples.


### Development Plan
| task no. | task                                        | planned outcome                                                                      | est. time | est. completion date | criteria |
|----------|---------------------------------------------|--------------------------------------------------------------------------------------|-----------|----------------------|----------|
| 1        | Planning: meet with client                  | identified problem, success criteria, meeting schedule, etc.                         | 20min     | March 2              | A        |
| 2        | Planning: purposed solution                 | solid idea of a purposed solution, sent to client for confirmation                   | 30min     | March 2              | A        |
| 3        | Planning: rationale                         | researched and documented the rationale for the purposed solution                    | 30min     | March 7              | A        |
| 4        | Design: solution sketch                     | detailed wireframe of the application                                                | 20min     | March 15             | B        |
| 5        | Design: system diagram                      | detailed system diagram of the application                                           | 30min     | March 15             | B        |
| 6        | Design: UML diagram                         | detailed UML diagram                                                                 | 15min     | March 18             | B        |
| 7        | Design: ER table & diagram                  | detailed ER table & diagram                                                          | 20min     | March 18             | B        |
| 8        | Development: login screen                   | functional GUI for the login screen                                                  | 40min     | March 25             | C        |
| 9        | Development: database & password hashing    | created 2 database (users, Shoes) using ORM-SQLAlchemy; function for password hasing | 60min     | March 25             | C        |
| 10       | Development: register screen                | functional GUI for the register screen                                               | 30min     | March 27             | C        |
| 11       | Development: welcome screen                 | functional GUI for the welcome screen                                                | 20min     | April 2              | C        |
| 12       | Development: table screen                   | functional GUI for the table screen                                                  | 90min     | April 5              | C        |
| 13       | Development: edit function for table screen | feature for editing existing data (Shoes) and saving it to the database              | 30min     | April 7              | C        |
| 14       | Development: add/remove function            | feature for adding/removing data (Shoes) in the database                             | 50min     | April 7              | C        |
| 15       | Development: sorting function               | feature for sorting the table based on each columns                                  | 40min     | April 11             | C        |
| 16       | Design: flow diagrams                       | detailed flow diagrams of specific functions                                         | 30min     | April 15             | B        |
| 17       | Development: program check                  | no bugs/errors, appropriate written comments, good coding practices                  | 30min     | April 17             | C        |
| 18       | Functionality: testing                      | test application following the testing plan                                          | 30min     | April 19             | D        |
| 19       | Functionality: video demonstration          | film video for final submission                                                      | 30min     | April 20             | D        |

### Test Plan



## Criteria C: Development

### Tools
1. Object-oriented programming (OOP)
2. KivyMD library
3. Relation database
4. SQLAlchemy, ORM (Object-relational mapping)
5. Guard clause

### Setting up the database with ORM and SQLAlchemy

The database plays two important roles in the application, managing the users and Shoes. I created a separate python file ```database_models.py``` specifically for handling the database.

Import the necessary modules and declare ```Base```.

``` python
# Import database_models
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base

# Call Base
Base = declarative_base()

```

Make two classes, one for each table: ```users(Base)``` and ```Shoes(Base)```.

``` python
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

```

1. Import the classes into the ```main.py``` file where the app will be running from.
2. Create the database with SQLAlchemy.
3. Assign the database handler as ```session```.

``` python
# Import from SQLAlchemy the function to connect to db
from sqlalchemy import create_engine

# Function to create a session
from sqlalchemy.orm import sessionmaker
from database_models import Base, users, Shoes

# Creates the database
db_engine = create_engine("sqlite:///orm_database.db")
Base.metadata.create_all(db_engine)
Base.metadata.bind = db_engine
db_session = sessionmaker(bind=db_engine)
session = db_session()

```

### Password hashing

Hashing is encrypting a value to secure it. In case of a security breach, your account/password is most likely safe because it is saved as a seemingly random string. I'll be using the PBKDF2-SHA256 hash, which is one of the most powerful hashes that focuses on countering brute-force attacks<sup>[[5]](https://en.wikipedia.org/wiki/PBKDF2#Purpose_and_operation)</sup>. For example, hash the string ```ilovecomsci``` with PBKDF2-SHA256, 1000 iterations will give you ```$pbkdf2-sha256$1000$KoVwLuVcaw1BiPGe897bGw$pAjrkYKpAyc7Fcu7b6vJ9.L0qzTOtOCKOmmXaKDDSMU```.

I allocated a different python file ```password_hash.py``` for this task.

1. Install the passlib library. In the terminal, run the command ```pip install passlib```, and import it into the python file.
2. Use CryptContext to set the parameters for the hash function.

``` python
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=65893
)

```

Create two functions: ```encrypt_password()``` for encrypting the password and ```check_password()``` for checking the password input and the hashed password.

``` python
def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_password(password, hashed):
    return pwd_context.verify(password, hashed)
    
```

Lastly, import these functions into ```main.py```.

``` python
# Import function for hashing password
from password_hash import encrypt_password, check_password

```

### Instal and import KivyMD

1. Install the KivyMD library via the terminal using the command line ```pip install kivymd```.
2. Import the library into ```main.py```.

``` python
# Import kivymd for GUI design
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
```

### Login Screen: Creating the UI with KivyMD

Assign a ```SreenManager```, which is used to manage multiple screens, then include all the screens/pages in the application.

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

    TableScreen:
        name: "TableScreen"
        id: TableScreen
```

1. Set the background as an image using ```FitImage``` inside an ```MDBoxLayout``` that covers the whole window.
2. Add an ```MDCard``` and inside it, an ```MDBoxLayout```, which will hold all the elements (other than the background) of the Login screen.
3. Add an ```MDLabel``` for the application name ***Shoez***
4. Add two ```MDTextField```s for the email and password input.
5. Add two buttons: ***Login*** and ***Register***. The ***Login*** button will run a method to check whether the login information is valid and log the user in. The ***Register*** button will move the user to the Register screen.

``` .kv
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
                    root.parent.current='RegisterScreen'
                    email_input.text=''
                    password_input.text=''
```

### Login Screen: Programming the UX with python

1. Make two classes ```LoginScreen(MDScreen)``` and ```app_GUI(MDApp)```.
2. In ```app_GUI``` , add the method ```build(self)``` to make the app window.
3. ```run()```

``` python
class LoginScreen(MDScreen):
    """ This class creates the login screen"""
    

class app_GUI(MDApp):
    """ This class creates the GUI for the app"""

    def build(self):
        return


gui = app_GUI()
gui.run()

```

1. Create the ```try_login(self)``` method for login that takes the input value from the two ```TextEditField```s: email and password.
2. Include a ***guard clause*** - an if-statement that eliminates conditions that may cause error later on, protecting the system from crashing, bugs, and many more; its main purpose is to increase code readability.

``` python
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

```

The next step is to make two boolean expressions: one to check whether the user exists and one to check if the input password is correct.

1. The program has to query the database's ***users*** table for the user with the same ***email*** as the one in the input.
2. Include a ***guard clause*** to exclude the possibility where the email doesn't exist in the database.
3. Use ```check_password()``` to check if the input password correlates with the hashed password in the database of the user.

``` python
class LoginScreen(MDScreen):
    """ This class creates the login screen"""

    # This method takes the login information then cross check it with the database log the user in
    def try_login(self):
        ...

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
                        
```

### Register Screen: Creating the UI with KivyMD

I want the Register screen to look like the Login screen, only with several adjustments:

1. An extra ```TextEditField``` for username
2. The ***Login*** button is swapped with ***Register*** and vice versa
3. ***Register*** button will be linked to the ```register()``` function

``` .kv
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
                    root.parent.current='LoginScreen'
                    username_input.text=''
                    email_input.text=''
                    password_input.text=''
```

### Register Screen: Programming the UX with python

1. In the ```RegisterScreen(MDScreen)``` class, add the ```register()``` method, which will take the input from the ```TextEditFields``` to create and save a new user into the database.
3. Assign the input values of the three ```TextEditFields``` to a variable.
4. ***Guard clause*** stop method if any of the input is empty.
5. Use ```pass_hashed()``` to hash the input password.
6. Create an object ```new_user``` of the ```users``` class with the input values: ```username```, ```email```, ```password```.

``` python
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
        new_user = users(username=username_entered,
                         email=email_entered,
                         password=pass_hashed)
        
```

Now, I have to add the ```new_user``` into the ```users``` table. However, if a value contradicts with the row's properties, the program will exit automatically. For example, if the input email already exist in the database, there will be a contradiction because when I defined the rows of the ```users``` table, ```email``` is a ***UNIQUE*** variable, which means that there can only be one in that column.

Therefore, the program must scan the database to see whether the email has already been used by a user before committing to avoid program exit.

1. Assign ```is_duplicate``` to the result after querying the database for email duplicates.
2. ***Guard clause*** to stop the method if there is at least one duplicate.
3. Use ```session.add()```, which places the object ```new_user``` into a placeholder - pending changes - that can later be added into the database.
4. Use ```session.commit()``` and ```session.close()``` commit the changes.
5. Move to Home screen.

``` python
class RegisterScreen(MDScreen):
    """ This class creates the register screen"""

    # This method creates a new user account and add it to the database
    def register(self):
        ...

        # Scan the database for the account with the same email
        is_duplicate = (session.query(users).
                        filter(users.email == email_entered).
                        first())

        # Stops method if email already linked to a user
        if is_duplicate:
            print("Email already linked to an account.")
            return

        # Add new_user to the table
        session.add(new_user)
        session.commit()
        session.close()
        self.parent.current = "LoginScreen"

```

### Home screen

The Home screen shows a welcome message displaying the user's username with two buttons: ***Tables*** and ***Logout***.

``` .kv
<HomeScreen>:
    MDBoxLayout:
        orientation: "vertical"
        size_hint: 1, .9
        pos_hint: {"top": 1}

        MDLabel:
            id: name_label
            halign: "center"
            font_style: "H1"
            color: 0, 0, 0, 1


    MDRectangleFlatButton:
        id: table_button
        text: "Table"
        text_color: 55/255, 173/255, 255/255, 1
        size_hint: .4, None
        pos_hint: {"center_x": .5, "center_y": .25}

        on_release:
            root.parent.current = "TableScreen"

    MDRaisedButton:
        id: logout_button
        text: "Logout"
        size_hint: .4, None
        pos_hint: {"center_x": .5, "center_y": .16}
        md_bg_color: .4, .4, .4, 1
        on_release:
            root.parent.current = "LoginScreen"
```

The ```HomeScreen(MDScreen)``` class will have the ```on_pre_enter()``` method, which runs prior to loading the window. This method will find and display the welcome message.

``` python
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

```

### Table screen






### Software Update
The software will receive updates as per user's requests. Since the number of user is still small, updating based on the user's feedbacks allows for a more transparent process and guarantees that the user is satisfied with the changes. Also, the software update will be a direct changeover - changing to the new system immediately. The advantage to this is that it's the quickest and most efficient method. However, the drawback is that if the system were to fail, it would fail completely, but because the system is simple and relatively small, the disadvantage is insignificant. Lastly, the update will be sent via mail and completely optional, as some user may prefer using the previous versions. To proceed with the direct-changeover update, opening the update package will automatically delete the previous version (with the exception of the database), and install the new version of the system.


## Criteria D: Functionality


## Apendix (as of 3:14PM, Apr 18)


## Citation
1. Robinson, D. (2017, September 6). The incredible growth of python. Stack Overflow Blog. Retrieved March 22, 2022, from https://stackoverflow.blog/2017/09/06/incredible-growth-python/ 
2. Carbonnelle, P. (n.d.). PYPL popularity of Programming Language index. index. Retrieved March 22, 2022, from https://pypl.github.io/PYPL.html 
3. Rodríguez, A. (2021). Welcome to KIVYMD's documentation!. Welcome to KivyMD's documentation! - KivyMD 1.0.0.dev0 documentation. Retrieved March 26, 2022, from https://kivymd.readthedocs.io/en/latest/ 
4. Gantan, X. (2014, March 12). Overview of SQLALCHEMY's expression language and Orm queries. Python Central. Retrieved March 27, 2022, from https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/ 
5. Wikimedia Foundation. (2022, April 3). PBKDF2. Wikipedia. Retrieved April 21, 2022, from https://en.wikipedia.org/wiki/PBKDF2#Purpose_and_operation 
6. Datatables. DataTables - KivyMD 1.0.0.dev0 documentation. (n.d.). Retrieved April 19, 2022, from https://kivymd.readthedocs.io/en/latest/components/datatables/ 
