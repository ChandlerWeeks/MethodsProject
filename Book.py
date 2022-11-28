import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="project1"
    )

    print("Successful connection.")

except:
    print("Failed connection.")
    sys.exit()

cursor = connection.cursor()


class book:
    def __init__(self, book_id, title, isbn, author, genre, count, style, pages):
        self.book_id = book_id
        self.title = title
        self.isbn = isbn
        self.author = author
        self.genre = genre
        self.count = count
        self.style = style
        self.pages = pages
        cursor.execute('INSERT INTO book (BookID, Title, ISBN, Author, Genre, Count, Style, Pages) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format
                          (self.book_id, self.title, self.isbn, self.author, self.genre, self.count, self.style, self.pages))
        connection.commit()

        
def get_book_id(book_id):
    cursor.execute("SELECT * FROM 'book' WHERE BookID = '{}'".format(book_id))
    return cursor.fetchall()


def get_title(title):
    cursor.execute("SELECT * FROM 'book' WHERE Title = '{}'".format(title))
    return cursor.fetchall()


def get_author(author):
    cursor.execute("SELECT * FROM 'book' WHERE Author = '{}'".format(author))
    return cursor.fetchall()


def get_genre(genre):
    cursor.execute("SELECT * FROM 'book' WHERE Genre = '{}'".format(genre))
    return cursor.fetchall()

