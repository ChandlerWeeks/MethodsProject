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


class Order:
    # constructor
    def __init__(self, userID):
        self.cartID = None
        self.orderID = None
        self.orderTime = None
        self.userID = userID
        self.itemID = None
        self.quantity = None
        self.price = None
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

    # sets value to emty
    def deleteHistory(self):
        for key, value in self.ordereditems.items():
            if key == self.userID:
                value = ""

    # add price and order id
    def orderHistory(self):
        itemsOrdered = "SELECT ItemName FROM orderitems WHERE userID = '{}'".format(self.userID)
        cursor.execute(itemsOrdered)
        items = cursor.fetchall()

        # attempting to grab price Sums prices of items from orderitems table where userid matches best to not use user id bc user csan have mult ordres but not sure if i can just go off orderid here

        # grabs order id from order items where user id matches best to not use user id bc user can have mult orders but not sure what to go off
        cursor.execute("SELECT OrderID From orderitems WHERE userID = '{}'".format(self.userID))
        self.orderID = cursor.fetchall()

        for x in range(len(self.orderID)):
            cursor.execute("SELECT SUM(Price) FROM orderitems WHERE orderID = '{}'".format(self.orderID[x][0]))
            self.price = cursor.fetchone()[0]

        cursor.execute("SELECT DateTime FROM orderitems WHERE userID = '{}'".format(self.userID))
        time = cursor.fetchall()
        # format the time but since tuples immutable convert to list, change time, convert to tuple
        list2 = list(time)
        for x in range(len(list2)):
            for i in list2[x]:
                list2[x] = i.strftime("%m/%d/%Y")
        time = tuple(list2)
        # checking if user already made an order
        for key in self.ordereditems:
            if key == self.userID:
                self.ordereditems[key].append(items, time)
        # if not just create new key value
        else:
            dict1 = {self.userID: [items, time]}
            self.ordereditems.update(dict1)
        # print values
        print("Order History")
        for x in range(len(self.orderID)):
            if self.orderID[x - 1][0] != self.orderID[x][0] or len(self.orderID) == 1:
                print(''.ljust(100, '-'))
                print('Order ID:', self.orderID[x][0], 'Total price: ${0:.4g}'.format(self.price))
                print(''.ljust(100, '-'))
                for key, value in self.ordereditems.items():
                    if key == self.userID:
                        for i in range(len(value[0])):
                            for z in value[0][i]:
                                print('Item:', z, '|', 'Date:', value[1][i])
        return print(''.ljust(100, '-'))
