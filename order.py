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
        return cursor.fetchall()

    def get_OrderID(self):
        cursor.execute("SELECT OrderID FROM orders WHERE UserID = '{}'".format(self.userID))
        return cursor.fetchall()

    def get_OrderTime(self):
        cursor.execute("SELECT DateTime FROM orders WHERE UserID = '{}'".format(self.userID))
        return cursor.fetchall()

    def get_UserID(self):
        cursor.execute("SELECT UserID FROM orders WHERE UserID = '{}'".format(self.userID))
        return cursor.fetchall()

    def get_ItemID(self):
        cursor.execute("SELECT ItemID FROM orderitems WHERE UserID = '{}'".format(self.userID))
        return cursor.fetchall()

    def get_Quanity(self):
        cursor.execute("SELECT Quantity FROM orderitems WHERE ItemID = '{}'".format(self.itemID))
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
        
        cursor.execute("SELECT DateTime FROM order WHERE userID = '{}'".format(self.userID))
        time = cursor.fetchall()
       #format the time but since tuples immutable convert to list, change time, convert to tuple 
        list2 = list(time)
        for x in range(len(list2)):
            list2[x] = x.strftime("%m/%d/%Y %H:%M:%S"))
        time = tuple(list2)
        # checking if user already made an order
        for key in self.ordereditems:
            if key == self.userID:
                self.ordereditems[key].append(items,time)
        # if not just create new key value
        else:
            dict1 = {self.userID: [items,time]}
            self.ordereditems.update(dict1)
        # print values
        for key, value in self.ordereditems.items():
            if key == self.userID:
                for i in range(len(value[0])):
                    print(value[0][i], value[1][i])
             
# example method for datetime object printing
# grabs datetime tuples at that element and converts them into a properly formatted string
"""for x in range(len(value[1])):
    for i in value[1][x]:
        print(i.strftime("%m/%d/%Y %H:%M:%S"))"""

userId = 1
Order(userId).orderHistory()
