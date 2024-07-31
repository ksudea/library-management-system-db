# library-management-system-db
Mini-Project: Library Management System with MySQL Database Integration

Command-line interface (CLI) for the Library Management System with separate menus for each class of the system.

Main Menu:
  1. Book Operations
  2. User Operations
  3. Author Operations
  4. Genre Operations
  5. Quit
     
Book Operations:
  1. Add a new book
  2. Borrow a book
  3. Return a book
  4. Search for a book
  5. Display all books
     
User Operations:
  1. Add a new user
  2. View user details
  3. Display all users
     
Author Operations:
  1. Add a new author
  2. View author details
  3. Display all authors
     
Genre Operations:
  1. Add a new genre
  2. View genre details
  3. Display all genres


# How to run app on CLI
## Linux / Git Bash
(Recommended)
Run the following (make sure you're in the same directory as the project)

$ ln -s lib.sh lib-db

Next, type "./lib-db" in git bash/shell. The app should be running now!

## Windows

Run Windows Command Prompt as administrator.

Run the following:

$ mklink lib-db lib.bat

# Demo Video

https://youtu.be/QNWSgcmefwo

# Overview of Modules

1. library_interface.py handles the bulk of user interaction/input and menu options.
2. library_manager.py contains much of the "logic" of the application; it contains functions that implement the options in the various menus.
3. library_data_interaction.py contains the functions that interact with the database through mysql.connector. The library_manager functions contain calls to library_data_interaction functions which handle database querying and return any output.
4. validation_handler.py contains functions for validation of user input, often using regex, to make sure they are in line with library & database standards (e.g. proper ISBN numbers, proper date formatting, etc)
5. library_classes.py contain the class definitions for Genre, Book, User, Author
6. db_table_setup.sql contains the SQL scripts used to create the database and tables. The tables are as follows:
## Library Database Tables
![Screenshot (252)](https://github.com/user-attachments/assets/e04ef914-7239-4bc8-b205-21e56bc8b7d4)


Note: The repository also includes a text file of sample ISBNs to use when adding books to the library. 

Repo: https://github.com/ksudea/library-management-system-db/
