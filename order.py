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

except:
    print("Failed connection.")
    sys.exit()

cursor = connection.cursor()

class Order:
    #constructor
    def __init__(self,cartID, orderID, orderTime, userID, itemID, quantity,date,time):
        self.cartID = cartID
        self.orderID = orderID
        self.orderTime = orderTime
        self.userID = userID
        self.itemID = itemID
        self.quantity = quantity
        #didnt use these for date and time?
        self.date = date
        self.time = time
    #getters per class diagram
    def get_CartID(cartID):
        cursor.execute("SELECT * FROM 'orders' WHERE cartID = '{}'".format(cartID))
        return cursor.fetchall()
    def get_OrderID(orderID):
        cursor.execute("SELECT * FROM 'orders' WHERE orderID = '{}'".format(orderID))
        return cursor.fetchall()
    def get_OrderTime(orderTime):
        cursor.execute("SELECT * FROM 'orders' WHERE orderTime = '{}'".format(orderTime))
        return cursor.fetchall()
    def get_UserID(userID):
        cursor.execute("SELECT * FROM 'orders' WHERE userID = '{}'".format(userID))
        return cursor.fetchall()
    def get_ItemID(itemID):
        cursor.execute("SELECT * FROM 'orders' WHERE itemID = '{}'".format(itemID))
        return cursor.fetchall()
    def get_Quanity(quantity):
        cursor.execute("SELECT * FROM 'orders' WHERE quantity = '{}'".format(quantity))
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
    def deleteHistory(userID):
        for key,value in ordereditems.items():
            if key == userID:
                value = ""
    def orderHistory(userID):
        global ordereditems
        itemsOrdered = "SELECT ItemName FROM 'orderitems' WHERE userID = '{}'".format(userID)
        cursor.execute(itemsOrdered)
        items = cursor.fetchall()
        #checking if user already made an order
        for key in ordereditems:
            if key == userID:
                ordereditems[key].append(items)
        #if not just create new key value
        else:
            dict1 = {userID:[items, date.today(), datetime.now()]}
            ordereditems.update(dict1)
        #print values
        for key, value in ordereditems.items():
            if key == userID:
                print(value)