import mysql.connector
import random 

db_name = "library_db"
user = "root"
password = "0711"
host = "127.0.0.1"

def add_borrowed_book(user_db_id, book_id, borrow_date):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor(buffered=True)
        query = """INSERT INTO borrowed_books (user_id, book_id, borrow_date, currently_checked_out) 
        VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (user_db_id, book_id, borrow_date, 1))
        conn.commit()
        print("Successfully checked out book!")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def return_borrowed_book(user_db_id, book_id, borrow_date, return_date):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor()
        query = """UPDATE borrowed_books SET return_date = %s,  currently_checked_out = 0 
        WHERE user_id = %s AND book_id = %s AND borrow_date = %s;"""
        cursor.execute(query, (return_date, user_db_id, book_id, borrow_date))
        conn.commit()
        print("Successfully returned book!")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def get_borrowed_date(user_db_id, book_id):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor()
        query = """SELECT borrow_date FROM borrowed_books
        WHERE user_id = %s AND book_id = %s AND currently_checked_out = 1"""
        cursor.execute(query, (user_db_id, book_id))
        borrow_date = cursor.fetchall()
        if len(borrow_date) == 0:
                return None
        return borrow_date[0][0]
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def get_book_availability(book_id):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor()
        query = """SELECT availability FROM books
        WHERE id = %s"""
        cursor.execute(query, (book_id,))
        availability = cursor.fetchall()
        if len(availability) == 0:
                return None
        return availability[0][0]
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def change_book_availability(book_id, availability):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor()
        query = """UPDATE books SET availability = %s 
        WHERE id = %s;"""
        cursor.execute(query, (availability,book_id))
        conn.commit()
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
      
def get_borrowed_book_list(user_db_id):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor()
        query = """SELECT book_id FROM borrowed_books
        WHERE user_id = %s AND currently_checked_out = 1"""
        cursor.execute(query, (user_db_id,))
        borrowed_books = cursor.fetchall()
        if len(borrowed_books) == 0:
                return None
        return borrowed_books
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def add_book(title, author_id, ISBN, publication_date, genre_id):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor()
        query = """INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) 
        VALUES (%s, %s, %s, %s, %s, 1)"""
        cursor.execute(query, (title, author_id, genre_id, ISBN, publication_date))
        conn.commit()
        print("Successfully added book!")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def get_book_by_id(id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM books WHERE id = %s"""
            cursor.execute(query, (id,))
            book = cursor.fetchall()
            if len(book) == 0:
                  return None
            book = book[0]
            return book
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_book_title_by_id(id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT title FROM books WHERE id = %s
            LIMIT 1;"""
            cursor.execute(query, (id,))
            title = cursor.fetchall()
            if len(title) == 0:
                  return None
            title = title[0]
            return title[0]
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_book_by_ISBN(isbn):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM books WHERE isbn = %s;"""
            cursor.execute(query, (isbn,))
            book = cursor.fetchall()
            if len(book) == 0:
                  return None
            book = book[0]
            return book
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_book_title_by_ISBN(id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT title FROM books WHERE isbn = %s
            LIMIT 1;"""
            cursor.execute(query, (id,))
            conn.commit()
            title = cursor.fetchall()
            if len(title) == 0:
                  return None
            title = title[0][0]
            return title
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_book_id_by_ISBN(isbn):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT id FROM books WHERE isbn = %s;"""
            cursor.execute(query, (isbn,))
            id = cursor.fetchall()
            if len(id) == 0:
                  return None
            id = id[0][0]
            return id
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_all_books():
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM books;"""
            cursor.execute(query)
            books = cursor.fetchall()
            if len(books) == 0:
                  return None
            return books
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def search_books_by_ISBN(isbn):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM books WHERE isbn = %s;"""
            cursor.execute(query, (isbn,))
            books = cursor.fetchall()
            if len(books) == 0:
                  return None
            book = books[0]
            return book
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def search_books_by_title(title):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM books WHERE title = %s;"""
            cursor.execute(query, (title,))
            books = cursor.fetchall()
            if len(books) == 0:
                  return None
            return books
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def search_books_by_author_id(author_id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM books WHERE isbn = %s;"""
            cursor.execute(query, (author_id,))
            books = cursor.fetchall()
            if len(books) == 0:
                  return None
            return books
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def add_author(name, bio):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor()
        query = """INSERT INTO authors (name, biography) 
        VALUES (%s, %s)"""
        cursor.execute(query, (name, bio))
        conn.commit()
        print("Successfully added author!")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def get_author_by_id(id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM authors WHERE id = %s
            LIMIT 1;"""
            cursor.execute(query, (id,))
            author = cursor.fetchall()
            if len(author) == 0:
                  return None
            return author[0]
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_author_name_by_id(id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT name FROM authors WHERE id = %s;"""
            cursor.execute(query, (id,))
            author = cursor.fetchall()
            if len(author) == 0:
                  return None
            return author[0][0]
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_author_id_by_name(author_name):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT id FROM authors WHERE name = %s;"""
            cursor.execute(query, (author_name,))
            id = cursor.fetchall()
            if len(id) == 0 or id == None:
                  return None
            return id[0][0]
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_all_authors():
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM authors;"""
            cursor.execute(query)
            authors = cursor.fetchall()
            if len(authors) == 0:
                  return None
            return authors
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def add_user(name, user_id):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor()
        query = """INSERT INTO users (name, user_id) 
        VALUES (%s, %s)"""
        cursor.execute(query, (name, user_id))
        conn.commit()
        print("Successfully added user!")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def get_user_database_id(user_id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT id FROM users WHERE user_id = %s"""
            cursor.execute(query, (user_id,))
            id = cursor.fetchall()
            if len(id) == 0:
                  return None
            return id[0][0]
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
            
def get_user_by_user_id(user_id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM users WHERE user_id = %s;"""
            cursor.execute(query, (user_id,))
            library_user = cursor.fetchall()
            if len(library_user) == 0:
                  return None
            return library_user[0]
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_all_users():
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM users;"""
            cursor.execute(query)
            users = cursor.fetchall()
            if len(users) == 0:
                  return None
            return users
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def add_genre(name, description, category):
    try:
        conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host,
        consume_results=True)
        cursor = conn.cursor()
        query = """INSERT INTO genres (name, description, category) 
        VALUES (%s, %s, %s)"""
        cursor.execute(query, (name, description, category))
        conn.commit()
        print("Successfully added genre!")
    except mysql.connector.Error as db_err:
        print(f"Database error: {db_err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def get_genre_by_id(id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM genres WHERE id = %s
            LIMIT 1;"""
            cursor.execute(query, (id,))
            genre = cursor.fetchall()
            if len(genre) == 0:
                  return None
            return genre[0]
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_genre_name_by_id(id):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT name FROM genres WHERE id = %s;"""
            cursor.execute(query, (id,))
            genre = cursor.fetchall()
            if len(genre) == 0:
                  return None
            return genre[0][0]
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_genre_id_by_name(genre_name):
    try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT id FROM genres WHERE name = %s
            LIMIT 1;"""
            cursor.execute(query, (genre_name,))
            id = cursor.fetchall()
            if len(id) == 0:
                  return None
            return id[0][0]
    except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
    except Exception as e:
            print(f"Error: {e}")
    finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def get_all_genres():
      try:
            conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
            consume_results=True)
            cursor = conn.cursor()
            query = """SELECT * FROM genres;"""
            cursor.execute(query)
            genres = cursor.fetchall()
            if len(genres) == 0:
                  return None
            return genres
      except mysql.connector.Error as db_err:
            print(f"Database error: {db_err}")
      except Exception as e:
            print(f"Error: {e}")
      finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()