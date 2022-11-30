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


class Movie:
    def __init__(self):
        self.movie_list = None
        self.movie_price = None
        self.movie_stock = None

    def display_movies(self):
        cursor.execute("SELECT * FROM movie ORDER BY Title")
        self.movie_list = cursor.fetchall()

        for x in range(len(self.movie_list)):
                cursor.execute(f"SELECT Price FROM inventory WHERE ItemName = '{self.movie_list[x][1]}'")
                self.movie_price = cursor.fetchall()

                cursor.execute(f"SELECT Stock FROM inventory WHERE ItemName = '{self.movie_list[x][1]}'")
                self.movie_stock = cursor.fetchall()

                if self.movie_stock[0][0] == 0 or self.movie_stock[0][0] is None:
                    print(f'Title: {self.movie_list[x][1]}', f'Price: ${self.movie_price[0][0]}',
                          f'Description: {self.movie_list[x][4]}', f'Out of Stock!')
                else:
                    print(f'Title: {self.movie_list[x][1]}', f'Price: ${self.movie_price[0][0]}',
                          f'Description: {self.movie_list[x][4]}', f'Stock: {self.movie_stock[0][0]}')
