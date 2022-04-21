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

### Login Screen

***Setting up the database with ORM and SQLAlchemy***

The database plays two important roles in the application, managing the users and Shoes. I create a seperate python file ```database_models.py``` specifically for handling the database. To start with, import the necessary modules and declare ```Base```.

``` python
# Import database_models
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base

# Call Base
Base = declarative_base()

```

Next, make two classes, one for each tables: ```users(Base)``` and ```Shoes(Base)```. Also, give ```__tablename__``` and rows' names and datatypes. The ```users(Base)``` class has 4 rows: ```id``` (primary key), ```username```, ```email```, and ```password```.

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
        
```

The ```Shoes(Base)``` class has 8 rows: ```id``` (primary key), ```brand```, ```model```, ```size```, ```material```, ```color```, ```price```, and ```user_id```. With ```user_id``` being the ***Foreign Key*** that links the shoe with a user.

``` python
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

Lastly, I have to import the classes into the ```main.py``` file where the app will be running from. In addition, create the database with SQLAlchemy using ```create_engine()```, ORM with ```sessionmaker()```, and finally assigning the database handler as ```session```.

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

***Password hashing***

Password hashing is a method to secure a password by converting it into an encrypted representation of itself. The hashed password will then be stored into the database. In case of a security breach, your account/password is most likely safe because it is saved as a seemingly random string. For this application, I'll be using the PBKDF2-SHA256 hash, which is one of the most common hashes that focuses on countering brute-force attacks<sup>[[5]](https://en.wikipedia.org/wiki/PBKDF2#Purpose_and_operation)</sup> - requires a lot of computational power to crack. For example, hash the string ```ilovecomsci``` with PBKDF2-SHA256, 1000 iterations will give you ```$pbkdf2-sha256$1000$KoVwLuVcaw1BiPGe897bGw$pAjrkYKpAyc7Fcu7b6vJ9.L0qzTOtOCKOmmXaKDDSMU```.

I allocated a different python file ```password_hash.py``` for this task. To begin hasing passwords in python, I need to download the passlib library. In the terminal of the IDE (PyCharm in my case), run the command ```pip install passlib```, and import it into the python file. Use CryptContext to set the parameters (```schemes```, ```default```, ```pbkdf2_sha256__default_rounds```) for the hash function.

``` python
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=65893
)

```

Then, create two functions: ```encrypt_password()``` for encrypting the password and ```check_password()``` for checking the password input and the hashed password.

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

***Instal and import KivyMD***

Before I can start programming the Login screen, I need to install the KivyMD library via the terminal, using the command line ```pip install kivymd```, which will automatically begin the installation process. After that, I will be able to import the library into my python file and use it. For the application, I needed to imported from KivyMD as follow.

``` python
# Import kivymd for GUI design
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
```

***Creating the UI with KivyMD***

The first step to creating a Login screen is designing and making the interface. I'll be using KivyMD library to create the UI (user interface) for the Login screen and the entire application. Start by assigning a ```SreenManager```, which is used to manage multiple screens, then include all the screens/pages in the application as follow.

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

Then, proceed to create the Login screen. Firstly, I set the background as an image using ```FitImage``` inside an ```MDBoxLayout``` that covers the whole window.

``` .kv
# Define the login screen
<LoginScreen>:
    MDBoxLayout:
        orientation: "vertical"

        FitImage:
            source: 'shoez_login_background.jpg'
            opacity: .85
```

Secondly, add an ```MDCard``` and an ```MDBoxLayout``` inside of it. This will hold all the elements (other than the background) of the Login screen.

``` .kv
# Define the login screen
<LoginScreen>:
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
```

Next, I'll include the name of the application - ***Shoez*** - as an MDLabel and two ```MDTextField```s for the email and password input.

``` .kv
# Define the login screen
<LoginScreen>:
    MDCard:
        ...

        MDBoxLayout:
            ...

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
```

Lastly, two buttons: ***Login*** and ***Register***. The ***Login*** button will run a method to check whether the login information is valid and log the user in. The ***Register*** button will move the user to the Register screen.

``` .kv
# Define the login screen
<LoginScreen>:
    MDCard:
        ...

        MDBoxLayout:
            ...
            
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

After building the UI, I'll now move to creating the python code for the Login screen.

***Programming the UX with python***

First, I want to be able view the GUI/window of the app, make a class with the name ```LoginScreen(MDScreen)``` inheriting from ```MDScreen``` (leave empty for now) and another class ```app_GUI(MDApp)``` inheriting from ```MDApp``` to build the app. In ```app_GUI``` , add the method ```build(self)``` to make the app window.

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

With this, I can view the Login screen - useful when creating the UI as it helps to visualize the KivyMD code. Secondly, create the ```try_login(self)``` method for login that takes the input value from the two ```TextEditField```s: email and password. Also, include a ***guard clause*** - an if-statement that eliminates certain conditions that may cause error later on, protecting the system from crashing, bugs, and many more; it's main purpose is to increase code readability - to stop the method if either input is empty.

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

The next step is to make two boolean expressions: one to check whether the user exists and one to check if the input password is correct. Firstly, the program has to query the database's ***users*** table for the user with the same ***email*** as the one in the input. Secondly, include a ***guard clause*** to exclude the posibility where the email doesn't exist in the database. Finally, use ```check_password()``` to check if the input password correlates with the hashed password in the database of the user.

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







### Software Update
The software will recieve update as per user's requests. Since the number of user is still small, updating based on the user's feedbacks allows for a more transparent process and guarantees that the user is satisfied with the changes. Also, the sofetware update will be a direct changeover - changing to the new system immediately. The advantage to this is that it's the quickest and most efficient method. However, the drawback is that if the system were to fail, it would fail completely, but because the system is simple and relatively small, the disadvantage is insignificant. Lastly, the update will be sent via mail and completely optional, as some user may prefer using the previous versions. To proceed with the direct-changeover update, opening the update package will automatically delete the previous version (with the exeption of the database), and install the new version of the system.


## Criteria D: Functionality


## Apendix (as of 3:14PM, Apr 18)


## Citation
1. Robinson, D. (2017, September 6). The incredible growth of python. Stack Overflow Blog. Retrieved March 22, 2022, from https://stackoverflow.blog/2017/09/06/incredible-growth-python/ 
2. Carbonnelle, P. (n.d.). PYPL popularity of Programming Language index. index. Retrieved March 22, 2022, from https://pypl.github.io/PYPL.html 
3. Rodríguez, A. (2021). Welcome to KIVYMD's documentation!. Welcome to KivyMD's documentation! - KivyMD 1.0.0.dev0 documentation. Retrieved March 26, 2022, from https://kivymd.readthedocs.io/en/latest/ 
4. Gantan, X. (2014, March 12). Overview of SQLALCHEMY's expression language and Orm queries. Python Central. Retrieved March 27, 2022, from https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/ 
5. Wikimedia Foundation. (2022, April 3). PBKDF2. Wikipedia. Retrieved April 21, 2022, from https://en.wikipedia.org/wiki/PBKDF2#Purpose_and_operation 
6. Datatables. DataTables - KivyMD 1.0.0.dev0 documentation. (n.d.). Retrieved April 19, 2022, from https://kivymd.readthedocs.io/en/latest/components/datatables/ 
