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


class Movie:
    def __init__(self):
        self.movie_list = None

    def display_movies(self):
        cursor.execute("SELECT * FROM movie ORDER BY Title")
        self.movie_list = cursor.fetchall()

        for x in self.movie_list:
            print(x)

Movie().display_movies()
