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

The UI (user interface) plays an important role in app development as it provides visuals and the experience. However, this process does not highlight my computational skills and for that reason, I decided not to include this in criteria C. Please refer to the [Apendix](https://github.com/David-Hien/Unit-3/blob/main/Project.md#apendix) for the source code.

### Creating the database

One of the most important components of the application is the database because most of the contents are built from the data stored inside of it. The two beings: the users and the shoes. I used SQLAlchemy and ORM (object-relational mapping) to serve several functions based on the success criteria, which are: ***create***, ***edit***, ***add***, and ***remove***.

#### Making the tables

The next step was to make the ***tables***, which will hold all the users’ and shoes’ data. Two important things to note about the ***tables*** are that they each need an ```id``` as a ***primary key*** and that it must be ***unique***. Thankfully, anytime a new user is registered or a new shoe is added, the ***primary key*** can be automatically generated and is ***unique***. Therefore, it is unnecessary to bother manually generating an ```id``` every time.

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

### Password hashing

My client values privacy stated in success criteria 4 – the login information and database are secured and the password is hashed. To tackle this problem, I enlisted the help from ```passlib``` library – a hashing library for Python – and specifically, the class ```CryptContext```.

Hashing is encrypting a value to secure it. In case of a security breach, your account/password is most likely safe because it is saved as a seemingly random string. I used the PBKDF2-SHA256 hash, which is one of the most powerful hashes that focuses on countering brute-force attacks<sup>[[6]](https://en.wikipedia.org/wiki/PBKDF2#Purpose_and_operation)</sup>. For example, hash the string ```ilovecomsci``` with PBKDF2-SHA256, 1000 iterations will give you ```$pbkdf2-sha256$1000$KoVwLuVcaw1BiPGe897bGw$pAjrkYKpAyc7Fcu7b6vJ9.L0qzTOtOCKOmmXaKDDSMU```.

In addition, I created two functions: ```encrypt_password()``` for encrypting the password and ```check_password()``` for checking the password input in comparison to the hashed password.

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


## Citation
1. Robinson, D. (2017, September 6). The incredible growth of python. Stack Overflow Blog. Retrieved March 22, 2022, from https://stackoverflow.blog/2017/09/06/incredible-growth-python/ 
2. Carbonnelle, P. (n.d.). PYPL popularity of Programming Language index. index. Retrieved March 22, 2022, from https://pypl.github.io/PYPL.html 
3. Rodríguez, A. (2021). Welcome to KIVYMD's documentation!. Welcome to KivyMD's documentation! - KivyMD 1.0.0.dev0 documentation. Retrieved March 26, 2022, from https://kivymd.readthedocs.io/en/latest/ 
4. Gantan, X. (2014, March 12). Overview of SQLALCHEMY's expression language and Orm queries. Python Central. Retrieved March 27, 2022, from https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/ 
5. “Using Table-Per-Tenant Multi-Tenancy | EclipseLink 2.4.x Understanding EclipseLink.” Eclipse.Org, 10 July 2013, www.eclipse.org/eclipselink/documentation/2.4/solutions/multitenancy003.htm.
6. Wikimedia Foundation. (2022, April 3). PBKDF2. Wikipedia. Retrieved April 21, 2022, from https://en.wikipedia.org/wiki/PBKDF2#Purpose_and_operation 
7. Datatables. DataTables - KivyMD 1.0.0.dev0 documentation. (n.d.). Retrieved April 19, 2022, from https://kivymd.readthedocs.io/en/latest/components/datatables/ 
