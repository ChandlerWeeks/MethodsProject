import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="project1"
    )
except:
    print("Failed connection.")
    sys.exit()

cursor = connection.cursor()


class Book:
    def __init__(self):
        self.book_list = None

    def display_books(self):
        cursor.execute("SELECT * FROM book ORDER BY Title")
        self.book_list = cursor.fetchall()

        for x in range(len(self.book_list)):
            cursor.execute(f"SELECT Price FROM inventory WHERE ItemName = '{self.book_list[x][1]}'")
            self.book_price = cursor.fetchall()

            cursor.execute(f"SELECT Stock FROM inventory WHERE ItemName = '{self.book_list[x][1]}'")
            self.book_stock = cursor.fetchall()

            if len(self.movie_stock) > 0:
                if self.book_stock[0][0] <= 0 or self.book_stock[0][0] is None:
                    print(f'Title: {self.book_list[x][1]}', f'ISBN: {self.book_list[x][2]}',
                      f'Author: {self.book_list[x][3]}',
                      f'Price: ${self.book_price[0][0]}', f'Out of Stock!')
                else:
                    print(f'Title: {self.book_list[x][1]}', f'ISBN: {self.book_list[x][2]}',
                      f'Author: {self.book_list[x][3]}',
                      f'Price: ${self.book_price[0][0]}', f'Stock: {self.book_stock[0][0]}')
