import mysql.connector

db_name = "library_management_db"
user = "root"
password = "0711"
host = "127.0.0.1"

class Genre:
    def __init__(self, name="", description="", category=""):
        self.__name = name
        self.__description = description
        self.__category = category
    def getGenreName(self):
        return self.__name
    def setGenreName(self, new_name):
        self.__name = new_name
    def getDescription(self):
        return self.__description
    def setDescription(self, new_description):
        self.__description = new_description
    def getCategory(self):
        return self.__category
    def setCategory(self, new_category):
        self.__category = new_category

class Book(Genre):
    def __init__(self, title, author_id, ISBN, publication_date, availability, genre_id):
        self.__title = title
        self.__author_id = author_id
        self.__isbn = ISBN
        self.__publication_date = publication_date
        self.__availability = availability
        super().__init__(genre_id)
        
    def getTitle(self):
        return self.__title
    def setTitle(self, new_title):
        self.__title = new_title
    def getAuthor(self):
        return self.__author_id
    def setAuthor(self, new_author):
        self.__author_id = new_author
    def getISBN(self):
        return self.__isbn
    def setISBN(self, new_isbn):
        self.__isbn = new_isbn
    def getPublicationDate(self):
        return self.__publication_date
    def setPublicationDate(self, new_date):
        self.__publication_date = new_date
    def getAvailability(self):
        return self.__availability
    def setAvailability(self, new_availability):
        self.__availability = new_availability

class User:
    def __init__(self, name, id, borrowed_books):
        self.__name = name
        self.__library_id = id
        self.__borrowed_books = borrowed_books
    def getUserName(self):
        return self.__name
    def setUserName(self, new_name):
        self.__name = new_name
    def getID(self):
        return self.__library_id
    def setID(self, new_id):
        self.__library_id = new_id
    def getBorrowedBooks(self):
        return self.__borrowed_books
    def setBorrowedBooks(self, new_list):
        self.__borrowed_books = new_list
    def addBorrowedBook(self, book_isbn, book_title):
        self.__borrowed_books.update({book_isbn: book_title})
    def deleteBorrowedBook(self, book_isbn, book_title):
        self.__borrowed_books.pop(book_isbn)

class Author:
    def __init__(self, name, bio):
        self.__name = name
        self.__bio = bio
    def getAuthorName(self):
        return self.__name
    def setAuthorName(self, new_name):
        self.__name = new_name
    def getBio(self):
        return self.__bio
    def setBio(self, new_bio):
        self.__bio = new_bio

