# Module for user interface, input validation, and interaction with library manager through operation choices

import library_manager
import validation_handler as vh


def book_operations():
  try:
    while True:
            print("""Book Operations:
                        1. Add a new book
                        2. Borrow a book
                        3. Return a book
                        4. Search for a book
                        5. Display all books
                        6. Return to main menu
            """)
            operation = int(input("Enter the number (1-6):"))
            if operation == 1:
              try:
                while True: 
                    book_title = input("Enter valid book title: ")
                    if not vh.book_title_validate(book_title):
                        raise Exception
                    book_author = input("Book author: ")
                    if not vh.name_validate(book_author):
                        raise Exception
                    print("Enter a valid ISBN-13 number (format: XXX-X-XXXX-XXXX-X or XXX X XXXX XXXX X or without spaces).")
                    book_isbn = input("Book ISBN: ")
                    if not vh.book_ISBN_validate(book_isbn):
                        raise Exception
                    book_isbn = vh.book_ISBN_database_format(book_isbn)
                    book_publication_date = input("Book publication date (format: MM/DD/YYYY): ")
                    if not vh.book_publication_date_validate(book_publication_date):
                        raise Exception
                    book_publication_date = vh.book_date_database_format(book_publication_date)
                    book_genre = input("Book genre (press enter to skip): ")
                    if not book_genre == "" and not vh.name_validate(book_genre):
                        raise Exception
                    book_genre_description = input("Book genre description(press enter to skip): ")
                    book_genre_category = input("Book genre category(press enter to skip): ")
                    library_manager.add_book(book_title, book_author, book_isbn, book_publication_date, book_genre, book_genre_description, book_genre_category)
                    break
              except Exception as e:
                  print(f"Error. {e}")
            elif operation == 2:
                print("You need both User ID and Book ISBN to borrow.")
                try:
                    user_id = input("Library user ID: ")
                    if vh.user_id_validate(user_id):
                        print("Enter a valid ISBN-13 number (format: XXX-X-XXXX-XXXX-X or XXX X XXXX XXXX X or without spaces).")
                        book_isbn = input("Library book ISBN: ")
                        if vh.book_ISBN_validate(book_isbn):
                            book_isbn = vh.book_ISBN_database_format(book_isbn)
                            print(library_manager.borrow_book(user_id, book_isbn))
                            break
                        else: 
                            print("Invalid book ISBN.")
                    else:
                        print("Invalid user ID.")
                except Exception as e:
                    print(f"Error! Check input. {e}")
            elif operation == 3: 
                print("You need both User ID and Book ISBN to return.")
                try:
                    user_id = input("Library user ID: ")
                    if vh.user_id_validate(user_id):
                        print("Enter a valid ISBN-13 number (format: XXX-X-XXXX-XXXX-X or XXX X XXXX XXXX X or without spaces).")
                        book_isbn = input("Library book ISBN: ")
                        if vh.book_ISBN_validate(book_isbn):
                            book_isbn = vh.book_ISBN_database_format(book_isbn)
                            print(library_manager.return_book(user_id, book_isbn))
                            break
                        else: 
                            print("Invalid book ISBN.")
                    else:
                        print("Invalid user ID.")
                except Exception as e:
                    print(f"Error! Check input. {e}")
            elif operation == 4:
                print("You need USBN, book title, or author to search for books.")
                try:
                    print("Enter a valid ISBN-13 number (format: XXX-X-XXXX-XXXX-X or XXX X XXXX XXXX X or without spaces).")
                    book_isbn = input("Book ISBN(press enter to skip): ")
                    if book_isbn == "" or vh.book_ISBN_validate(book_isbn):
                        book_isbn = vh.book_ISBN_database_format(book_isbn)
                        book_title = input("Library book title(press enter to skip): ")
                        if book_title == "" or vh.book_title_validate(book_title):
                            book_author = input("Library book author(press enter to skip): ")
                            if book_author == "" or vh.name_validate(book_author):
                                print(library_manager.search_for_book(book_isbn, book_title, book_author))
                                break
                            else:
                                print("Invalid book author name.")
                        else: 
                            print("Invalid book title.")
                    else:
                        print("Invalid book ISBN.")
                except Exception as e:
                    print(f"Error! Check input. {e}")
            elif operation == 5: 
                library_manager.display_all_books()
            elif operation == 6:
                break
            else:
                print("Incorrect input. Try again")
  except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-6 as an option.")
  except Exception as e:
      print(f"Error in book operations: {e}")

def user_operations():
    try:
        while True:
            print("""User Operations:
                        1. Add a new user
                        2. View user details
                        3. Display all users
                        4. Return to main menu
            """)
            operation = int(input("Enter the number (1-4):"))
            if operation == 1:
                user_name = input("Valid user name: ")
                if vh.name_validate(user_name):
                    user_id = input("Library user ID: ")
                    if vh.user_id_validate(user_id):
                        library_manager.add_user(user_name,user_id)
                    else:
                        print("Input valid user ID.")
                else:
                        print("Input valid user name.")
            elif operation == 2:
                user_id = input("Library user ID: ")
                if vh.user_id_validate(user_id):
                    library_manager.view_user_details(user_id)
                else:
                    print("Input valid user ID to view user details")
            elif operation == 3:
                library_manager.display_all_users()
            elif operation == 4:
                break
    except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-4 as an option.")
    except Exception as e:
        print(e)

def author_operations():
    try:
        while True:
            print("""Author Operations:
                        1. Add a new author
                        2. View author details
                        3. Display all authors
                        4. Return to main menu
            """)
            operation = int(input("Enter the number (1-4):"))
            if operation == 1:
                author_name = input("Enter valid author name: ")
                if vh.name_validate(author_name):
                    author_bio = input("Author bio(press enter to skip): ")
                    library_manager.add_author(author_name, author_bio)
                else:
                    print("Invalid title input. Try again")
            elif operation == 2: 
                author_name = input("Author name: ")
                if vh.name_validate(author_name):
                    library_manager.view_author_details(author_name)
                else:
                    print("Input valid user ID to view user details")
            elif operation == 3:
                library_manager.display_all_authors()
            elif operation == 4:
                break
    except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-4 as an option.")
    except Exception as e:
        print(e)

def genre_operations():
    try:
        while True:
            print("""Genre Operations:
                        1. Add a new genre
                        2. View genre details
                        3. Display all genres
                        4. Return to main menu
            """)
            operation = int(input("Enter the number (1-4):"))
            if operation == 1:
                genre_name = input("Enter valid genre name: ")
                if vh.name_validate(genre_name):
                    genre_description = input("Genre description(press enter to skip): ")
                    genre_category = input("Genre category (press enter to skip)")
                    library_manager.add_genre(genre_name, genre_description, genre_category)
                else:
                    print("Invalid genre name input. Try again")
            elif operation == 2: 
                genre_name = input("Genre name: ")
                if vh.name_validate(genre_name):
                    library_manager.view_genre_details(genre_name)
                else:
                    print("Input valid genre name to view details")
            elif operation == 3:
                library_manager.display_all_genres()
            elif operation == 4:
                break
    except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-4 as an option.")
    except Exception as e:
        print(e)