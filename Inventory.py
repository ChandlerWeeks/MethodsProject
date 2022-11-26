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


# Getters all find matching items from table
def get_item_ID(item_ID):
    cursor.execute("SELECT * FROM 'Inventory' WHERE itemID = '{}'".format(item_ID))
    return cursor.fetchall()


def get_name(name):
    cursor.execute("SELECT * FROM 'Inventory' WHERE Name = '{}'".format(name))
    return cursor.fetchall()


class Inventory:
    # Creation of a new item in inventory
    def __init__(self, item_ID, name, price, rating, stock):
        self.item_ID = item_ID
        self.name = name
        self.price = price
        self.rating = rating
        self.stock = stock

        cursor.execute("INSERT INTO `inventory`(`ItemID`, `ItemName`, `Price`, `Rating`, `Stock`) "
                       "VALUES ('{}','{}','{}','{}','{}')".format(item_ID, name, price, rating, stock))
        connection.commit()





