# Unit 3 Project 

## Table of Contents

1. [Planning](https://github.com/David-Hien/Unit-3/blob/main/Project.md#criteria-a-planning)


## Criteria A: Planning 

### Definition of Problem

My client's name is Nagisa Sato. She has a collection of shoes - both the ones currently in her possesion and the ones she would like to have. At the moment, my client does not use any application or system to organize her collection. For that reason, Nagisa wishes for an application that can store the data of her shoes and is able to organize it base on different factors as to help her keep a better track of the collection. In addition, my client wants to have a "wishlist" - list of shoes that she wants to add to her collection in the future - that is also organized to find the next pair to buy.

### Proposed Solution

My proposed solution is to create an application that uses Python as the main programming language, Kivymd Library for the GUI (Graphical User Interface), and SQLAlchemy to manipulate the database. The app will consist of a Login/Register screen, a page to show the shoe collections, and another page for the user to manually edit the collections. Two other additions are:
- a search function that can assist the user navigate large databases
- a sort function that rearrange the collection based on factors (eg. name, price, color) of the user's choice

***Python***

I chose Python as the programming language for the following reasons. Firstly, Python is widely used in various areas thanks to it simple syntax and focus on natural language, making it beginner friendly at the same time not losing much versitility. According to Stackoverflow blog by David Robinson<sup>[[1]](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)</sup>, Python is the fastest growing programming language, and is predicted to be the most in-demand language in 2020, which was proven to be true - according to PYPL PopularitY of Programming Language<sup>[[2]](https://pypl.github.io/PYPL.html)</sup>, Python ranked first with the most tutorial video views on Google. Also, because I'm familiar with this language, the process of developing this product will be more efficient. Secondly, Python supports OOP (Object-oriented programming). For this application, I believe it is more effective to approach using OOP, because it makes it much easier to navigate and understand the code, which means easy to locate errors, high code-reusability, and other developers - who might work on the project after you - won't have a hard time.

***Kivymd Library***

The Kivymd Library is an open-source library used as a framework for cross-platform applications<sup>[[3]](https://kivymd.readthedocs.io/en/latest/)</sup>. It is a tool for creating GUI (Graphical User Interface) for applications, which serves as a communicator between the input (keyboard, mouse, multitouch events, etc.) and the program, as well as between the program and the output (screen). This is an essential part of any application because it exponentially increases the app's usability and desirabilty - easier to understand, use, and charming visual aesthetics.

***SQLAlchemy and ORM***



### Success Criteria

1. User is able to Create, Add, Edit, Delete data in the table
2. The application has a login and register page
3. The login information and database is secured and the password is hashed
4. Able to transfer a row (an object) from one table to another
5. Upload image*
6. Function to sort the table based on different factors
7. Function to search specific information from a defined range
8. Uses OOP (Object-oriented programming)







### Citation
1. Robinson, D. (2017, September 6). The incredible growth of python. Stack Overflow Blog. Retrieved March 22, 2022, from https://stackoverflow.blog/2017/09/06/incredible-growth-python/ 
2. Carbonnelle, P. (n.d.). PYPL popularity of Programming Language index. index. Retrieved March 22, 2022, from https://pypl.github.io/PYPL.html 
3. Rodríguez, A. (2021). Welcome to KIVYMD's documentation!. Welcome to KivyMD's documentation! - KivyMD 1.0.0.dev0 documentation. Retrieved March 26, 2022, from https://kivymd.readthedocs.io/en/latest/ 
4. 
