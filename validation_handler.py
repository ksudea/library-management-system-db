# Validation helper methods for input

import re

def book_title_validate(title):
    match = re.match(r"\b([A-Za-z,0-9. ']{2,})+", title)
    if match != None:
          return True
    return False

#Matches ISBN13 (13 chars that start with 978 or 979) in the following formats:
# XXX-X-XXXX-XXXX-X
# XXX X XXXX XXXX X
# XXXXXXXXXXXXX
def book_ISBN_validate(isbn):
    match = re.match(r"\b(97(8|9){1}){1}[- \s]?[0-9]{1}[- \s]?[0-9]{4}[- \s]?[0-9]{4}[- \s]?[0-9]{1}$", isbn)
    if match != None:
          return True
    return False

def book_ISBN_database_format(isbn):
     db_isbn = re.sub('[ ,-]', '', isbn)
     return db_isbn

#Matches the following formats:
#MM DD YYYY or MM/DD/YYYY or MM-DD-YYYY
def book_publication_date_validate(date):
    match = re.match(r"^[0-9]{1,2}[\/\- ]?[0-9]{1,2}[\/\- ]?[0-9]{4}$", date)
    if match != None:
          return True
    return False

def book_date_database_format(date):
     db_date = re.sub('[ ,-]', '/', date)
     return db_date

#Matches availability = Available or Borrowed
def book_availability_validate(availability):
    match = re.match(r"^(Available|Borrowed)", availability)
    if match != None:
          return True
    return False

#At least 3 chars
def user_id_validate(id):
    match = re.match(r"\b([A-Za-z,0-9. ']{3,})+", id)
    if match != None:
          return True
    return False

#Name validation for user name, author name, and genre name (2 or more valid characters)
def name_validate(name):
    match = re.match(r"\b([A-Z-,a-z. ']{2,})+", name)
    if match != None:
          return True
    return False
