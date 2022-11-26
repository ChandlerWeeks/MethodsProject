import mysql.connector
import sys
from datetime import date
from datetime import datetime

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


class Order:
    # constructor
    def __init__(self, userID):
        self.cartID = None
        self.orderID = None
        self.orderTime = None
        self.userID = userID
        self.itemID = None
        self.quantity = None
        # didnt use these for date and time?
        self.date = None
        self.time = None
        self.ordereditems = {}

    # getters per class diagram
    def get_CartID(self):
        cursor.execute("SELECT CartID FROM orders WHERE UserID = '{}'".format(self.userID))
        self.cartID = cursor.fetchall()

    def get_OrderID(self):
        cursor.execute("SELECT OrderID FROM orders WHERE UserID = '{}'".format(self.userID))
        self.orderID = cursor.fetchall()

    def get_OrderTime(self):
        cursor.execute("SELECT * FROM orders WHERE orderTime = '{}'".format(self.orderTime))
        return cursor.fetchall()

    def get_UserID(self):
        cursor.execute("SELECT UserID FROM orders WHERE UserID = '{}'".format(self.userID))
        return cursor.fetchall()

    def get_ItemID(self):
        cursor.execute("SELECT ItemID FROM orders WHERE itemID = '{}'".format(self.itemID))
        return cursor.fetchall()

    def get_Quanity(self):
        cursor.execute("SELECT * FROM orders WHERE quantity = '{}'".format(self.quantity))
        return cursor.fetchall()

    """def set_date(self, date):
        date1 = date.today()
        self.date = date1
        d = date1.strftime("%B %d, %Y")
        self.date = d
    def get_date(self):
        return self.date
    def set_time(self, time):
        time = datetime.now()
        self.time = time
        ct = time1.strftime("%H:%M:%S")
        self.time= ct
    def get_time(self):
        return self.time"""

    # sets value to emty
    def deleteHistory(self):
        for key, value in self.ordereditems.items():
            if key == self.userID:
                value = ""

    def orderHistory(self):
        itemsOrdered = "SELECT ItemName FROM orderitems WHERE userID = '{}'".format(self.userID)
        cursor.execute(itemsOrdered)
        items = cursor.fetchall()
        # checking if user already made an order
        for key in self.ordereditems:
            if key == self.userID:
                self.ordereditems[key].append(items)
        # if not just create new key value
        else:
            dict1 = {self.userID: [items, date.today(), datetime.now()]}
            self.ordereditems.update(dict1)
        # print values
        for key, value in self.ordereditems.items():
            if key == self.userID:
                print(value)


userId = 1
Order(userId).orderHistory()
