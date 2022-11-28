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


class Book:
    def __init__(self):
        self.book_list = None

    def display_books(self):
        cursor.execute("SELECT * FROM book")
        self.book_list = cursor.fetchall()

        for x in self.book_list:
            print(x)

Book().display_books()