# Module for the library management system: storing and interacting with library data such as books, users, authors, and genres.  
import library_data_interaction as di
from library_classes import Genre, Book, User, Author
from datetime import datetime, date

db_name = "library_management_db"
user = "root"
password = "0711"
host = "127.0.0.1"

#Add book to database, with genre details optional.
#If inputted author and/or genre do not exist in the database already, adds them to their respective tables.

def add_book(title, author, ISBN, publication_date, genre_name, genre_description, genre_category):
    try:
        author_id = di.get_author_id_by_name(author)
        if author_id == None:
            di.add_author(author, "")
            author_id = di.get_author_id_by_name(author)
        if genre_name == "":
            genre_id = None
        else:
            genre_id = di.get_genre_id_by_name(genre_name)
            if genre_id == None:
                di.add_genre(genre_name, genre_description, genre_category)
                genre_id = di.get_genre_id_by_name(genre_name)
        date_object = datetime.strptime(publication_date, '%m/%d/%Y').date()
        new_book = Book(title, author, ISBN, publication_date, "Available", genre_name)
        di.add_book(title, author_id, ISBN, date_object, genre_id)
    except Exception as e:
        print(f"Error occurred: {e}")

#Allows user with user_id to borrow book with ISBN if book is not already checked out (book availability)
def borrow_book(user_id, ISBN):
    try:
        book_id = di.get_book_id_by_ISBN(ISBN)
        user_db_id = di.get_user_database_id(user_id)
        if di.get_book_availability(book_id) == 1:
            di.add_borrowed_book(user_db_id, book_id, datetime.today())
            di.change_book_availability(book_id,0)
            book_title = di.get_book_title_by_id(book_id)
            return(f"User {user_id} borrowed book {book_title}")
        else:
            return "This book is already checked out!"
        
    except Exception as e:
        print(f"Error occurred: {e}")

#Allows user to return book, also reverting the book availability to available
def return_book(user_id, ISBN):
    try:
        book_id = di.get_book_id_by_ISBN(ISBN)
        user_db_id = di.get_user_database_id(user_id)
        borrowed_date = di.get_borrowed_date(user_db_id, book_id)
        return_date = date.today()
        di.return_borrowed_book(user_db_id, book_id, borrowed_date, return_date)
        di.change_book_availability(book_id,1)
        book_title = di.get_book_title_by_id(book_id)
        return(f"User {user_id} returned book {book_title}")
    except Exception as e:
        print(f"Error occurred: {e}")

#Allows you to search by ISBN, title, or author.
#ISBN search necessarily returns 1 book but title/author searches may return many
def search_for_book(ISBN="", title="", author=""):
    try:
        if ISBN == "" and title == "" and author == "":
            return("You must enter at least the ISBN or book title to search.")
        if ISBN != "":
            book = di.search_books_by_ISBN(ISBN)
            display_book(book)
            return "Finished"
        elif title != "":
            books = di.search_books_by_title(title)
            for book in books:
                display_book(book)
            return "Finished"
        elif author != "":
            authorId = di.get_author_id_by_name(author)
            books = di.search_books_by_author_id(authorId)
            for book in books:
                display_book(book)
            return "Finished"
        return("Book could not be found.")
    except Exception as e:
        print(f"Error occurred: {e}")

#Display all books in library
def display_all_books():
    try:
        books = di.get_all_books()
        for book in books:
            display_book(book)
    except Exception as e:
        print(f"Error occurred: {e}")

#Helper function for printing the details of a book based on the returned row from the books table in our database
def display_book(book):
    try:
            book_author = ""
            genre = ""
            if book[2] != None: 
                book_author = di.get_author_name_by_id(book[2])
            if book[3] != None:
                genre = di.get_genre_name_by_id(book[3])
            if book[6] == 0:
                availability = "Borrowed"
            else:
                availability = "Available"
            print(f"""Book Title: {book[1]} \n    Book Author: {book_author}\n    Book ISBN: {book[4]}\n
    Published: {book[5]}\n    Availability: {availability}\n    Book Genre: {genre}\n""")
    except Exception as e:
        print(f"Error occurred: {e}")

#Adds user
def add_user(name, id):
    try:
        new_user = User(name, id, {})
        di.add_user(name, id)
        print("Added new user!")
    except Exception as e:
        print(f"Error occurred: {e}")

#Displays details of a user with user_id
def view_user_details(user_id):
    try:
        user = di.get_user_by_user_id(user_id)
        if user == None:
            print("Could not find user with this ID.")
        else:
            user_db_id = di.get_user_database_id(user_id)
            user_borrowed_books = di.get_borrowed_book_list(user_db_id)
            print(user_borrowed_books)
            print(f"Library User ID: {user_id} \n    User name: {user[1]}\n")
            if user_borrowed_books == None:
                print("     No currently borrowed books.")
            else:
                print("     Borrowed books list:")
                for book_id in user_borrowed_books:
                    book = di.get_book_by_id(book_id[0])
                    display_book(book)
    except KeyError:
        print("Could not find user with this ID")
    except Exception as e:
        print(f"Error occurred: {e}")

#Displays all library users
def display_all_users():
    try:
        users = di.get_all_users()
        for user in users:
            print(f"Library User ID: {user[2]}   User name: {user[1]}\n")
    except Exception as e:
        print(f"Error occurred: {e}")

#Add new author with optional biography
def add_author(name, bio):
    try:
        new_author = Author(name, bio)
        di.add_author(name, bio)
        print("Added new author!")
    except Exception as e:
        print(f"Error occurred: {e}")

#Display author details by inputted name
def view_author_details(name):
    try:
        author_id = di.get_author_id_by_name(str(name))
        author = di.get_author_by_id(author_id)
        if author_id == None:
            print("Could not find author with this name.")
        else:
            print(f"Author Name: {author[1]}\n     Bio: {author[2]}")
    except Exception as e:
        print(f"Error occurred: {e}")

#Displays all authors stored in the library
def display_all_authors():
    try:
        authors = di.get_all_authors()
        for author in authors:
            print(f"Author Name: {author[1]}\n     Bio: {author[2]}")
    except Exception as e:
        print(f"Error occurred: {e}")

#Add new genre
def add_genre(name, description, category):
    try:
        new_genre = Genre(name, description, category)
        di.add_genre(name, description, category)
        print("Added new genre!")
    except Exception as e:
        print(f"Error occurred: {e}")

#View details of a genre by its name
def view_genre_details(name):
    try:
        genre_id = int(di.get_genre_id_by_name(name))
        genre = di.get_genre_by_id(genre_id)
        if genre == None:
            print("Could not find genre with this name.")
        else:
            print(f"Genre Name: {genre[1]}\n     Category: {genre[3]}\n     Description: {genre[2]}")
    except Exception as e:
       print(f"Error occurred: {e}")

#Display all genres in library
def display_all_genres():
    try:
        genres = di.get_all_genres()
        for genre in genres:
            print(f"Genre Name: {genre[1]}\n     Category: {genre[3]}\n     Description: {genre[2]}")
    except Exception as e:
        print(f"Error occurred: {e}")
