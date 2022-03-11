# Database Unit3 Project 

**Table of Contents** 

1. [Planning](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-a-planning)


## Criteria A: Planning 

### Identified Problem 

My client, Cathy, needs a new system for recording down her CAS activity for IB. She is currently using Managebac, however the features are very user unfriendly since it loads slowly, and the features needed are hard to find and difficult to navigate. The client, therefore, wants a system which is made specifically for recording CAS activity. An additional issue my client has with Managebac is that it lacks a personalised interface, and so I will customise the new program to include a monkey theme because my client explicitly mentioned images of monkeys must be present to make it feel personal. 

### Proposed Solution 

My proposed solutions is to create a remote program using Python and the Kivy Library. The Kivy library provides a framework for both computer and phone applications, making it easy for the developer to implement a GUI (graphical user interface) in the application. This, in turn, makes the program much easier for the custotmer to use because they do not need to use the python console or terminal, but just the GUI screen provided. For the database itself, the data and tables will be stored and created using SQLAlchemy, and the relationships and queries will all be done using ORM (object-relational-mapping). Lastly, the program will include a log-in and registration feature, a page which the user can enter their CAS activities (date, activity name, activity type, duration per activity). After a consultation with the client, she approved of this plan. 
 
### Justification 

**Why Python and Kivy?**

Python is the most appropriate languaging to code in for this project. Other than the fact that, I, the developer, am most comfortable with it and thus will be able to create a more complex and elegant program, the language itself has several benefits. Firstly, it is currently the most popular programming language by a significant amount. According to PYPYL (Popularity of Programming Language), which measures each coding language's popularity by Google trends, concludes that python shares 30% of all computer language searches, while Java, the second most popular, shares only 18% [1]. Due to its popularity, this program can be easily understood by a larger number of developers and, furthermore, maintained. Python uses a simple syntax and offeres a wide variety of libraries -- add ons which can enhance your program with additional features [2]. The variety of libraries is very useful when needing to create a more complex program. However, there are a couple disadvantages to python. Pythonis a high-level language, meaning that it uses more abstraction and is less understandable to the computer as a trade off for having simple syntax . The consequences of this result in less control from the developer. Another disadvantage of python is that it does not run on a mobile application [2], but since the program will run on a computer, this does not interfere.


Kivy is a library created to work only for python. It is a framework which creates a GUI for the developer, which will mean the program will not run on the Python console or terminal, but via the GUI Screen. While Kivy uses its own language, it is simple, and will anyways need to run alongside with the python to write in the logic of the program. Kivy langauge organises its code with object-oriented-coding, which widgets and elements are classes [3]. The library is powerful because of the sheer number of features available, and is also supported for all devicess [4]. This allows my program to expand to multi-platforms if wanted. There are some significant set-backs with Kivy, such as major bugs with certain features, and little documentatioin available [4], but because my program will not recquire complex features, this will not have a significant impact. 

**Why SQLAlchemy and ORM?**

For the database, I will be using SQLAlchemy to create databases. SQLAlchemy is the python toolkit which works similarily like SQL but is in ORM. SQL is one of the most popular langue to interact with databases, with the ability of having almost all the functions related to data-table creating. SQLAlchemy is a more effiecient and simpler way of connecting to databases, with the advantage of obscuring or cutting down many of the tedious SQL tasks like connecting to servers and fetching data [5]. The reason why SQLAlchemy is so much more efficient is because it is an ORM (Object-relational-mapper), which make tasks (like queries) into objects. This results in a a high-level abstracted code. While in some cases it would be better to not obsscure some of the code with ORM, such as in a learning enviornment, for this project, it is preferred. 
