# Unit 3 Project 

## Table of Contents

1. [Planning](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-a-planning)
2. [Design](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-b-solution-overview)
3. [Development](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-c-development)
5. [Functionality](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-d-functionality)
6. [Apendix](https://github.com/David-Hien/Unit-3/blob/main/Project.md#apendix)
7. [Citation](https://github.com/David-Hien/Unit-3/blob/main/Project.md#citation)


## Criteria A: Planning 

### Definition of Problem

My client has a collection of shoes. They are facing a problem where they can't keep track of the collection and need a system to do so. At the moment, they do not use any application or system to help organize their collection. For that reason, my client wishes for an application that can store the data of their shoes and is able to organize it based on different factors to help them keep a better track of the collection.

### Proposed Solution

My proposed solution is to create an application that uses Python as the main programming language, Kivymd Library for the GUI (Graphical User Interface), and SQLAlchemy to manipulate the database. The app will consist of a Login/Register screen, a page to show the shoe collections, and another page for the user to manually edit the collections. The table can be sorted based on factors (eg. name, price, color) of the user's choice.

#### Python

I choose Python as the programming language for the following reasons. Firstly, Python is widely used in various areas thanks to its simple syntax and focus on natural language, making it beginner friendly at the same time not losing much versatility. According to Stackoverflow blog by David Robinson<sup>[[1]](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)</sup>, Python is the fastest growing programming language, and is predicted to be the most in-demand language in 2020, which was proven to be true - according to PYPL PopularitY of Programming Language<sup>[[2]](https://pypl.github.io/PYPL.html)</sup>, Python ranked first with the most tutorial video views on Google. Also, because I'm familiar with this language, the process of developing this product will be more efficient. Secondly, Python supports OOP (Object-oriented programming). For this application, I believe it is more effective to approach using OOP, because it makes it much easier to navigate and understand the code, which means easy to locate errors, high code-reusability, and other developers - who might work on the project after you - won't have a hard time.

#### Kivymd Library

The Kivymd Library is an open-source library used as a framework for cross-platform applications<sup>[[3]](https://kivymd.readthedocs.io/en/latest/)</sup>. It is a tool for creating GUI (Graphical User Interface) for applications, which serves as a communicator between the input (keyboard, mouse, multitouch events, etc.) and the program, as well as between the program and the output (screen). This is an essential part of any application because it exponentially increases the app's usability and desirability - easier to understand, use, and charming visual aesthetics.

#### SQLAlchemy and ORM

To operate the database, I choose to use SQLAlchemy. It's a declarative query language that is common for relational databases. Also, when identifying the issue and planning out the ER (Entity Relation) diagram and table, I noticed that classes have relation to each other. In this instance, a user has many shoes, and a shoe only has one user. In order to effectively address this, I choose to use an ORM (Object Relational Mapper) supported language, and among them, SQLAlchemy is highly compatible with Python that allows for Python construct<sup>[[4]](https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/)</sup>.

### Success Criteria

1. User is able to Add and Remove data in the table
2. User is able to Edit existing data
3. The application has a login and register page
4. The login information and database are secured and the password is hashed
5. Function to sort the table based on different factors
6. Follow good coding practises, which allow for future extensions by other developers


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

![LoginScreen](https://user-images.githubusercontent.com/89367058/164500231-e19a5401-af76-44d5-8144-f73e84136dd6.png)

***Figure 3:*** Flow diagram of the ```LoginScreen``` class

### <br/>

![RegisterScreen](https://user-images.githubusercontent.com/89367058/164502452-e3fbbdc1-6bce-4718-9ce9-7ef3c6813cda.png)

***Figure 4:*** Flow diagram of the ```RegisterScreen``` class

### <br/>

![edit_save](https://user-images.githubusercontent.com/89367058/164504865-775aec6d-9cd2-4973-8b94-45145eeb5301.png)

***Figure 4:*** Flow diagram of the ```edit_save``` method in the ```TableScreen``` class

### UML Diagram

![UML_diagram](https://user-images.githubusercontent.com/89367058/165523874-4164c1f5-a23e-4410-b4d9-4e8e0e76535f.png)

***Figure 6:*** UML diagram representing the classes in ```main.py```. Shows the methods of each class and the inheritance from KivyMD library.

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


### Record of Task
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

| Testing level    | Type of Testing                     | Success Criteria                                                                                                                                                                         | Procedure                                                                                                                                                                                                                                                                                                                                           | Success |
|------------------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Unit testing     | Login system test                   | User is able to log in after typing the correct email and password                                                                                                                       | In the Login screen, type "david@test" into the ***email input***, "david" into the ***password input***, and press the ***Login*** button.                                                                                                                                                                                                         | Yes     |
| Unit testing     | Login system test                   | User is unable to log in if either or both inputs are empty, or after typing the incorrect email or password. Instead, a helper text will appear indicating the error.                   | In the Login screen, leave the text fields blank and press ***Login*** button. Then, type an incorrect email into the ***email input***, anything into the ***password input***, and press the ***Login*** button. Then, type "david@test" into the ***email input***, anything (but "david") into the ***password input***, and press ***Login***. | Yes     |
| Unit testing     | Register system test                | User is able to register a new account with a new email address                                                                                                                          | In the Register screen, type anything into the ***username input***, "newuser@test" into the ***email input***, "password" into the ***password input***, and press the ***Register*** button.                                                                                                                                                      | Yes     |
| Unit testing     | Register system test                | User is unable to register a new account if any or all inputs are empty, or have the same email address as an existing account. Instead, a helper text will appear indicating the error. | In the Register screen, leave the text fields blank and press ***Login*** button. Then, type anything into the ***username input***, "david@test" into the ***email input***, "password" into the ***password input***, and press the ***Register*** button.                                                                                        | Yes     |
| Unit testing     | Table check_press test              | When check the box on a row, all the values in that row is transferred to the ```TextEditField```s.                                                                                      | In the Table screen, check the box next to any row.                                                                                                                                                                                                                                                                                                 | Yes     |
| Unit testing     | Table clear test                    | When ***Clear*** button is pressed, all the ```TextEditField```s are cleared.                                                                                                            | In the Table screen, put some value into the ```TextEditField```s, then press ***Clear***.                                                                                                                                                                                                                                                          | Yes     |
| Unit testing     | Table save system test              | When ***Save*** button is pressed, the table will reload with the selected row updated with the values in the ```TextEditField```s.                                                      | In the Table screen, check the box next to any row. Then, change the value of any or all columns and press ***Save***.                                                                                                                                                                                                                              | Yes     |
| Unit testing     | Table save system test              | When ***Save*** button is pressed, if any of the ```TextEditField```s (including ```id```) is empty, nothing will happen.                                                                | Do similar to the step above, however, leave a ```TextEditField``` blank.                                                                                                                                                                                                                                                                           | Yes     |
| Unit testing     | Table add system test               | When ***Add*** button is pressed, the table will reload with the a new row with the values in the ```TextEditField```s.                                                                  | In the Table screen, put a value into each ```TextEditField```, then press ***Add***.                                                                                                                                                                                                                                                               | Yes     |
| Unit testing     | Table add system test               | When ***Add*** button is pressed, if any of the ```TextEditField```s (excluding ```id```) is empty, nothing will happen.                                                                 | Do similar to the step above, however, leave a ```TextEditField``` blank.                                                                                                                                                                                                                                                                           | Yes     |
| Unit testing     | Table remove system test            | When ***Remove*** button is pressed, the table will reload and the selected row will disappear.                                                                                          | In the Table screen, check the box next to any row. Then, press ***Remove***.                                                                                                                                                                                                                                                                       | Yes     |
| Unit testing     | Table sort function                 | When the arrow key next to a column name is pressed, the table will be sorted based on that column's data.                                                                               | In the Table screen, click on all the arrow keys next to the column names.                                                                                                                                                                                                                                                                          | Yes     |
| Integration test | The app GUI functions               | The transition between pages is correct and there are no unaccounted for visual bugs.                                                                                                    | Check all the pages, transition and visual content                                                                                                                                                                                                                                                                                                  | Yes     |
| Code review      | Error/bugs and code efficiency test | No errors/exit messages/syntax/bugs                                                                                                                                                      | If all the Unit test worked, the criteria is met                                                                                                                                                                                                                                                                                                    | Yes     |
| Software review  | All system test                     | The program runs flawlessly throughout                                                                                                                                                   | If all the Unit test worked and the success criteria in Planning are met, the criteria is met                                                                                                                                                                                                                                                       | Yes     |

## Criteria C: Development

### Tools
1. Object-oriented programming (OOP)
2. KivyMD library
3. Relation database
4. SQLAlchemy, ORM (Object-relational mapping)
5. Guard clause

### Creating the UI

The UI (user interface) plays an important role in achieving the success criterias as it provides visuals and makes the interaction with the app’s function much simpler. I chose the KivyMD library because it supports OOP (object-oriented programming), which is highly compatible with the application.


### Creating the database

As the client requested, the app must include a storage system that stores data on the device. There are two tables to classify all the information: the users and the shoes. I used SQLAlchemy and ORM (object-relational mapping) because it provides an abstraction of database manipulation – the tables are represented by classes, instead of SQL commands.

#### How do we identify and differentiate between rows?

Because the properties of the ***objects*** within a ***table*** can vary greatly, it’s difficult and inefficient to ***identify*** and ***differentiate*** ***objects*** in a ***table***. Therefore, the answer is to add the ```id``` ***column*** that any ***object*** can refer to as the ***primary key***. The ***primary key*** is unique – there can only be one per ***column***. This meant that the program can ***identify*** and ***differentiate*** between ***objects*** using their ```id```. As a result, the program can accurately ***identify*** and ***edit***, ***add***, or ***remove*** ***objects*** with ease.

#### How do we know which shoe belongs to which collection/user?

The first thing that came to my mind was to create a ***table*** for each user instead of having one big ***table*** for everyone – which meant we can determine whose shoe it is just by the ***table*** name. The benefits are:
- **Faster query**:
    - The time complexity is the same in both cases – O(n), linear time – because both will have to ***query*** the entire table once.
    - With that being said, the ***table*** per ***tenant (user)*** method<sup>[[5]](https://www.eclipse.org/eclipselink/documentation/2.4/solutions/multitenancy003.htm)</sup> provides a slightly faster ***query*** because of the smaller ***table*** size.
- **Customizable**:
    - Given the access to the source code, any user can customize the ***columns***, ***data types***, ***etc.***
    - However, this is only possible with offline databases, which applies in this case, but in the grand scheme of things, it’s best to not allow direct access to the source code for privacy’s sake.

As apparent as the benefits, the downside is considerable:
- **Software-update**:
    - If a user ***customized*** their ***table*** the new software update will completely revert it to the original format.
    - They’re also at the risk of losing data or app crash if the ***customized table*** has different properties.

**Verdict**: It is a viable option to use the table per tenant method. However, the benefits it brings are not appealing enough to justify the downsides. Therefore, I opted for another solution, only having two tables – sacrificing an unnoticeable amount of run time for a much better code extendability and update potential.

#### Foreign key

So, how can I know ***whose shoe it is*** with only two ***tables***? The answer is simple – ***check the foreign key***. A ***foreign key*** acts as a bridge between ***tables***. It holds the address of the object in another ***table***. In this case, the shoe ***table*** has an extra ***column*** ```foreign_key```, which will hold the address of the user it belongs to.

#### Creating the database.

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


# Creates the database
db_engine = create_engine("sqlite:///orm_database.db")
Base.metadata.create_all(db_engine)

```


### How to secure login information

Because the login system requires to save the user’s login information inside the database, the email and password are susceptible to data leaks or attacks. My client values privacy stated in success criteria 4 – the login information and database are secured and the password is hashed. To tackle this problem, I enlisted the help from ```passlib``` library – a hashing library for Python – and specifically, the class ```CryptContext```.

Hashing is encrypting a value to secure it. In case of a security breach, your account/password is most likely safe because it is saved as a seemingly random string. I used the PBKDF2-SHA256 hash, which is one of the most powerful hashes that focuses on countering brute-force attacks<sup>[[6]](https://en.wikipedia.org/wiki/PBKDF2#Purpose_and_operation)</sup>. For example, hash the string ```ilovecomsci``` with PBKDF2-SHA256, 1000 iterations will give you ```$pbkdf2-sha256$1000$KoVwLuVcaw1BiPGe897bGw$pAjrkYKpAyc7Fcu7b6vJ9.L0qzTOtOCKOmmXaKDDSMU```.

After setting the parameters for the hash, I created two functions: ```encrypt_password()``` for encrypting the password and ```check_password()``` for checking the password input in comparison to the hashed password.

``` python
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=65893
)


def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_password(password, hashed):
    return pwd_context.verify(password, hashed)

```


### Login screen

As per the client’s request, the app will include a login/register function.

The problem I encountered when making the Login screen was checking if the login information was correct – corresponding to an existing user inside the database. My approach is to split it into 3 steps: ***getting the input***, ***querying the*** ```users``` ***database for users with the same*** ```email``` ***and*** ```password``` ***as the input***, and ***switching to the Home screen***.

#### 1. How to get the input

I assigned the input value from the two TextEditFields (```email``` and ```password```) to two local variables for convenience and code readability.

However, there is an issue – ***what if the input is blank***. ***Querying*** nothing will yield no value, also, the ```password_check()``` function does not take ```NoneType``` as an input – the program will exit with an ```AttributeError```. To prevent this issue and possible crash, I included a ***guard clause*** – an if-statement that eliminates conditions that may cause an error, protecting the system from crashing, bugs, and many more; its main purpose is to increase code readability. The ***guard clause*** will check if either the inputs are empty:
If yes, ```return``` – cancel the action of pressing the Login button, which does nothing.
If not, continue to the next step.

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

#### 2. Querying the ```users``` table

I assigned a ***boolean*** expression to check whether the ***email*** and ***password*** match the database.

``` python
class LoginScreen(MDScreen):
    """ This class creates the login screen"""

    # This method takes the login information then cross check it with the database log the user in
    def try_login(self):
        # Store the values inputed
        ...

        # Stops the method if either inputs is empty
        ...

        # Scan the database for the account with the same email
        current_user = (session.query(users).
                        filter(users.email == email_entered, check_password(pass_entered, current_user.password)).
                        first())
                        
```

However, I encountered another problem here, because of a property of the ```check_password()``` function, in most cases, it returns false even though the ***password*** typed is correct. This property is a security measure to protect the hashed strings in the case of the key being discovered, which meant using the same key on other hashed items will yield no result.

To counter this issue, I first search for the user with the same ***email*** – which is ***unique*** – and then check whether the input matches the corresponding ***password***. If the input is correct, log the user in.

``` python
class LoginScreen(MDScreen):
    """ This class creates the login screen"""

    # This method takes the login information then cross check it with the database log the user in
    def try_login(self):
        # Store the values inputed
        ...

        # Stops the method if either inputs is empty
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


### Register screen

Similar to the Login screen, the Register screen also takes the input from the user. The same problem of ***empty inputs*** arises, to which I used the same method: ***guard clause***.

Then, the program can add the ***new user*** to the ***table*** with the hashed ***password***.

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

        # Add new_user to the table
        session.add(new_user)
        session.commit()
        session.close()
        self.parent.current = "LoginScreen"
        
```

However, when I tested with an ***existing email***, the program exits. This is because I set the ```email``` ***column*** in the ```users``` ***table*** to be ***unique*** and if the same value is added, the program crashes. This problem was solved by ***querying*** the ***table*** for the ***email***. If the result is:
```type: class 'database_models.users'```, stop the method.
```NoneType```, continue and add the new user.

``` python
class RegisterScreen(MDScreen):
    """ This class creates the register screen"""

    # This method creates a new user account and add it to the database
    def register(self):
        # Store the values inputed
        ...

        # Stops method if input left blank
        ...

        # Hash the password (for security)
        ...

        # Update the database with the new account
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
        ...
        
```


### Table screen

This is the most important screen in the application, it’s going to ***display*** the shoe collection and host the main functions. According to the success criteria, the functions ***edit***, ***add***, and ***remove*** will be included in this screen. In addition, the client requested that there is a function to ***sort*** the ***table*** based on any ***column***.

#### Code repetition

Throughout the development of the Table screen, I noticed a major problem: code repetition. I recognized a pattern from my code, some of the methods’ commands are the same (or similar). For example, getting the current user (```type: class 'database_models.users'```), getting data from the ```Shoes``` table, etc. For that reason, I created separate methods for each of them to minimize repetition and at the same time, increase code readability.

``` python
class TableScreen(MDScreen):
    """ This class creates the table screen"""
    # Call table
    data_tables = None

    # This method queries the users table and return the current user
    def current_user(self):
        current_user_email = self.parent.ids.LoginScreen.ids.email_input.text

        # Query the user
        current_user = (session.query(users).
                        filter(users.email == current_user_email).
                        first())

        return current_user

    # This method queries the Shoes table and return its data as a list
    def get_shoes(self):
        # Query the Shoes table for rows with matching Foreign key to the user
        query = session.query(Shoes).filter(Shoes.user_id == self.current_user().id)
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
        
    # This method takes the value on the selected row of the table
    # and prints it on the according TextEdit fields
    def check_pressed(self, table, row):
        # Assign variables to store the values of the selected row
        shoe_id, brand, model, size, material, color, price = row

        # Print the values on the TextEdit fields
        self.ids.shoe_id.text = shoe_id
        self.ids.brand.text = brand
        self.ids.model.text = model
        self.ids.size.text = size
        self.ids.material.text = material
        self.ids.color.text = color
        self.ids.price.text = price

    # This method takes the input from the values in the TextEdit fields
    # and converted it into a row
    def get_row(self):
        # Assign variables to store the values of each TextEdit fields
        brand = self.ids.brand.text
        model = self.ids.model.text
        size = self.ids.size.text
        material = self.ids.material.text
        color = self.ids.color.text
        price = self.ids.price.text

        if (
                not brand or
                not model or
                not size or
                not material or
                not color or
                not price):
            print("Input missing")
            return

        # Format the values correctly for update
        row = (brand, model, size, material, color, price)
        return row
        
    # This method updates the table on display
    def update_table(self):
        # List of shoes (and attributes)
        result = self.get_shoes()

        # Updates the table
        self.data_tables.update_row_data(
            None, result
        )

    # This method clears the inputs
    def clear(self):
        # Clear all TextEdit fields
        self.ids.shoe_id.text = ""
        self.ids.brand.text = ""
        self.ids.model.text = ""
        self.ids.size.text = ""
        self.ids.material.text = ""
        self.ids.color.text = ""
        self.ids.price.text = ""
        
```

#### Edit, Add, and Remove methods

Although the process is highly technical, I didn’t face any worth-mentioning problems.

``` python
class TableScreen(MDScreen):
    """ This class creates the table screen"""
    
    ...

    # This method runs when the button "Save" is pressed
    def edit_save(self):
        # Checks if Shoe id is specified, doesn't run if shoe_id blank
        shoe_id = self.ids.shoe_id.text
        if not shoe_id:
            print("Shoe id missing")
            return

        # Row data
        updated_row = self.get_row()
        if not updated_row:
            return

        brand, model, size, material, color, price = updated_row

        # Update the Shoes table with the new data
        session.query(Shoes). \
            filter(Shoes.id == shoe_id). \
            update({Shoes.brand: brand,
                    Shoes.model: model,
                    Shoes.size: size,
                    Shoes.material: material,
                    Shoes.color: color,
                    Shoes.price: price})

        session.commit()
        session.close()

        # Refresh the table and TextEdit fields
        self.update_table()
        self.clear()

    # This method adds a new data row
    def add_item(self):
        # Row data
        new_row = self.get_row()
        if not new_row:
            return

        brand, model, size, material, color, price = new_row

        # Update the Shoes table with the new data
        new_shoe = Shoes(brand=brand,
                         model=model,
                         size=size,
                         material=material,
                         color=color,
                         price=price,
                         user_id=self.current_user().id)

        session.add(new_shoe)
        session.commit()
        session.close()

        # Refresh the table and TextEdit fields
        self.update_table()
        self.clear()

    # This method removes the data row
    def remove_item(self):
        # Checks if Shoe id is specified, doesn't run if shoe_id blank
        shoe_id = self.ids.shoe_id.text
        if not shoe_id:
            print("Shoe id missing")
            return

        session.query(Shoes). \
            filter(Shoes.id == shoe_id). \
            delete()

        session.commit()
        session.close()

        # Refresh the table and TextEdit fields
        self.update_table()
        self.clear()

    ...
        
```

#### Sort method

As my client specifically requested the ***sorting function***, my immediate ideas were to ***sort*** the ***table*** within the database or to sort the ***displayed table***. However, after some research, attempts, and comparisons, I realized several things:
- **Speed**:
    - The ***former*** takes ***more*** time as it requires two steps, ***ordering*** the ***table*** and ***updating*** the ***table***.
    - The ***latter*** takes ***less*** time as it only ***sorts*** the ***table***.
- **Feasibility**:
    - The ***former*** is ***less*** feasible as it requires a significant amount of commands and is extremely complicated.
    - The ***latter*** is ***more*** feasible as an example already exists on an online source – in the DataTables section<sup>[[7]](https://kivymd.readthedocs.io/en/latest/components/datatables/)</sup>.

As a result, I opted for the second solution, ***sorting*** the ***displayed table***.

``` python
class TableScreen(MDScreen):
    """ This class creates the table screen"""
    
    ...
    
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

    ...
        
```


### UI Screenshots

<img width="800" alt="Screen Shot 2022-04-22 at 0 06 47" src="https://user-images.githubusercontent.com/89367058/164490407-658cd929-be77-4474-b854-1d8302aa8484.png">

***Figure 8:*** Screenshot of the Login screen

<img width="800" alt="Screen Shot 2022-04-22 at 0 06 52" src="https://user-images.githubusercontent.com/89367058/164490726-c4ae7354-6be7-4888-99af-1e23a9f0260b.png">

***Figure 9:*** Screenshot of the Register screen

<img width="800" alt="Screen Shot 2022-04-22 at 0 07 18" src="https://user-images.githubusercontent.com/89367058/164490899-c2647c1e-6f2c-4804-af36-00446a07ec49.png">

***Figure 10:*** Screenshot of the Home screen

<img width="800" alt="Screen Shot 2022-04-22 at 0 07 33" src="https://user-images.githubusercontent.com/89367058/164491065-e6417ecf-67b6-40e2-9ceb-e7b655220a95.png">

***Figure 11:*** Screenshot of the Table screen

### Software Update
The software will receive updates as per user's requests. Since the number of user is still small, updating based on the user's feedbacks allows for a more transparent process and guarantees that the user is satisfied with the changes. Also, the software update will be a direct changeover - changing to the new system immediately. The advantage to this is that it's the quickest and most efficient method. However, the drawback is that if the system were to fail, it would fail completely, but because the system is simple and relatively small, the disadvantage is insignificant. Lastly, the update will be sent via mail and completely optional, as some user may prefer using the previous versions. To proceed with the direct-changeover update, opening the update package will automatically delete the previous version (with the exception of the database), and install the new version of the system.


## Criteria D: Functionality

### Video

https://drive.google.com/drive/folders/1FzhJcLJAgGHs3IJzMiZN1yAEJu4Z7Sej?usp=sharing

## Apendix

### Client's statement

https://user-images.githubusercontent.com/89367058/160220880-46e9df1f-ca53-4b7a-97ad-bdec87c4fe62.mov

<img width="636" alt="Screen Shot 2022-04-28 at 16 24 57" src="https://user-images.githubusercontent.com/89367058/165754037-88a00332-9c5a-48c4-91f6-eb712472b00a.png">

### Source code

#### database_models.py

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
    
```

#### passsword_hash.py

``` python
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=65893
)


def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_password(password, hashed):
    return pwd_context.verify(password, hashed)

```

#### main.py

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


class TableScreen(MDScreen):
    """ This class creates the table screen"""
    # Call table
    data_tables = None

    # This method queries the users table and return the current user
    def current_user(self):
        current_user_email = self.parent.ids.LoginScreen.ids.email_input.text

        # Query the user
        current_user = (session.query(users).
                        filter(users.email == current_user_email).
                        first())

        return current_user

    # This method queries the Shoes table and return its data as a list
    def get_shoes(self):
        # Query the Shoes table for rows with matching Foreign key to the user
        query = session.query(Shoes).filter(Shoes.user_id == self.current_user().id)
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
        shoe_id, brand, model, size, material, color, price = row

        # Print the values on the TextEdit fields
        self.ids.shoe_id.text = shoe_id
        self.ids.brand.text = brand
        self.ids.model.text = model
        self.ids.size.text = size
        self.ids.material.text = material
        self.ids.color.text = color
        self.ids.price.text = price

    # This method takes the input from the values in the TextEdit fields
    # and converted it into a row
    def get_row(self):
        # Assign variables to store the values of each TextEdit fields
        brand = self.ids.brand.text
        model = self.ids.model.text
        size = self.ids.size.text
        material = self.ids.material.text
        color = self.ids.color.text
        price = self.ids.price.text

        if (
                not brand or
                not model or
                not size or
                not material or
                not color or
                not price):
            print("Input missing")
            return

        # Format the values correctly for update
        row = (brand, model, size, material, color, price)
        return row

    # This method runs when the button "Save" is pressed
    def edit_save(self):
        # Checks if Shoe id is specified, doesn't run if shoe_id blank
        shoe_id = self.ids.shoe_id.text
        if not shoe_id:
            print("Shoe id missing")
            return

        # Row data
        updated_row = self.get_row()
        if not updated_row:
            return

        brand, model, size, material, color, price = updated_row

        # Update the Shoes table with the new data
        session.query(Shoes). \
            filter(Shoes.id == shoe_id). \
            update({Shoes.brand: brand,
                    Shoes.model: model,
                    Shoes.size: size,
                    Shoes.material: material,
                    Shoes.color: color,
                    Shoes.price: price})

        session.commit()
        session.close()

        # Refresh the table and TextEdit fields
        self.update_table()
        self.clear()

    # This method adds a new data row
    def add_item(self):
        # Row data
        new_row = self.get_row()
        if not new_row:
            return

        brand, model, size, material, color, price = new_row

        # Update the Shoes table with the new data
        new_shoe = Shoes(brand=brand,
                         model=model,
                         size=size,
                         material=material,
                         color=color,
                         price=price,
                         user_id=self.current_user().id)

        session.add(new_shoe)
        session.commit()
        session.close()

        # Refresh the table and TextEdit fields
        self.update_table()
        self.clear()

    # This method removes the data row
    def remove_item(self):
        # Checks if Shoe id is specified, doesn't run if shoe_id blank
        shoe_id = self.ids.shoe_id.text
        if not shoe_id:
            print("Shoe id missing")
            return

        session.query(Shoes). \
            filter(Shoes.id == shoe_id). \
            delete()

        session.commit()
        session.close()

        # Refresh the table and TextEdit fields
        self.update_table()
        self.clear()

    # This method updates the table on display
    def update_table(self):
        # List of shoes (and attributes)
        result = self.get_shoes()

        # Updates the table
        self.data_tables.update_row_data(
            None, result
        )

    # This method clears the inputs
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

#### app_GUI.kv

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
                helper_text: "Invalid email"
                helper_text_mode: "on_error"
                required: True
                icon_right: "email"

            MDTextField:
                id: password_input
                hint_text: "password"
                color: 1, 1, 1, 1
                helper_text: "Invalid password"
                helper_text_mode: "on_error"
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
                helper_text: "Invalid username"
                helper_text_mode: "on_error"
                required: True
                icon_right: "account"

            MDTextField:
                id: email_input
                hint_text: "email"
                color: 1, 1, 1, 1
                helper_text: "Invalid email"
                helper_text_mode: "on_error"
                required: True
                icon_right: "email"

            MDTextField:
                id: password_input
                hint_text: "password"
                color: 1, 1, 1, 1
                helper_text: "Invalid password"
                helper_text_mode: "on_error"
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


<TableScreen>
    MDRaisedButton:
        id: back_to_home_button
        text: "Back"
        pos_hint: {"right": .15, "top": .95}
        size_hint: None, None
        md_bg_color: .4, .4, .4, 1
        on_release:
            root.parent.current = "HomeScreen"

    MDBoxLayout:
        orientation: "vertical"
        pos_hint: {"center_x": .5, "top": .3}
        size_hint: .9, .3

        MDBoxLayout:
            orientation: "horizontal"
            pos_hint: {"top": 1}
            size_hint: 1, .6

            MDLabel:
                text: "Edit"
                font_size: 30
                pos_hint: {"left": .05, "bottom": .2}
                size_hint: .05, .5

            MDTextField:
                id: shoe_id
                hint_text: "id"
                pos_hint: {"left": .1, "bottom": .2}
                size_hint: .03, .5

            MDTextField:
                id: brand
                hint_text: "brand"
                pos_hint: {"left": .2, "bottom": .2}
                size_hint: .1, .5

            MDTextField:
                id: model
                hint_text: "model"
                pos_hint: {"left": .35, "bottom": 0}
                size_hint: .1, .5

            MDTextField:
                id: size
                hint_text: "size"
                pos_hint: {"left": .5, "bottom": 0}
                size_hint: .05, .5

            MDTextField:
                id: material
                hint_text: "material"
                pos_hint: {"left": .6, "bottom": 0}
                size_hint: .1, .5

            MDTextField:
                id: color
                hint_text: "color"
                pos_hint: {"left": .75, "bottom": 0}
                size_hint: .1, .5

            MDTextField:
                id: price
                hint_text: "price"
                pos_hint: {"left": .9, "bottom": 0}
                size_hint: .05, .5

        MDBoxLayout:
            orientation: "horizontal"
            pos_hint: {"bottom": 0}
            size_hint: 1, .4

            MDRaisedButton:
                text: "Save"
                size_hint: .1, .5
                pos_hint : {"center_x": .2, "center_y": .7}
                on_release:
                    root.edit_save()

            MDRaisedButton:
                text: "Add"
                md_bg_color: 0, .8, 0, 1
                size_hint: .1, .5
                pos_hint : {"center_x": .4, "center_y": .7}
                on_release:
                    root.add_item()

            MDRaisedButton:
                text: "Clear"
                md_bg_color: .4, .4, .4, 1
                size_hint: .1, .5
                pos_hint : {"center_x": .6, "center_y": .7}
                on_release:
                    root.clear()

            MDRaisedButton:
                text: "Remove"
                md_bg_color: 1, .1, .1, 1
                size_hint: .1, .5
                pos_hint : {"center_x": .8, "center_y": .7}
                on_release:
                    root.remove_item()

```

## Citation
1. Robinson, D. (2017, September 6). The incredible growth of python. Stack Overflow Blog. Retrieved March 22, 2022, from https://stackoverflow.blog/2017/09/06/incredible-growth-python/ 
2. Carbonnelle, P. (n.d.). PYPL popularity of Programming Language index. index. Retrieved March 22, 2022, from https://pypl.github.io/PYPL.html 
3. Rodríguez, A. (2021). Welcome to KIVYMD's documentation!. Welcome to KivyMD's documentation! - KivyMD 1.0.0.dev0 documentation. Retrieved March 26, 2022, from https://kivymd.readthedocs.io/en/latest/ 
4. Gantan, X. (2014, March 12). Overview of SQLALCHEMY's expression language and Orm queries. Python Central. Retrieved March 27, 2022, from https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/ 
5. “Using Table-Per-Tenant Multi-Tenancy | EclipseLink 2.4.x Understanding EclipseLink.” Eclipse.Org, 10 July 2013, www.eclipse.org/eclipselink/documentation/2.4/solutions/multitenancy003.htm.
6. Wikimedia Foundation. (2022, April 3). PBKDF2. Wikipedia. Retrieved April 21, 2022, from https://en.wikipedia.org/wiki/PBKDF2#Purpose_and_operation 
7. Datatables. DataTables - KivyMD 1.0.0.dev0 documentation. (n.d.). Retrieved April 19, 2022, from https://kivymd.readthedocs.io/en/latest/components/datatables/ 
