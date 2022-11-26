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


class ShoppingCart:
    def __init__(self, userID):
        self.cart = []
        self.cartID = []
        self.total_price = 0
        self.userID = userID

        cursor.execute(f"SELECT cartID FROM shoppingcart WHERE UserID = {self.userID}")
        self.cartID = cursor.fetchall()

        if self.cartID is not None:
            pass
        else:
            cursor.execute(f"SELECT UserID FROM user WHERE UserID = {userID}")
            self.cartID += cursor.fetchall()
            cursor.executemany(f"INSERT INTO shoppingcart (UserID) VALUES (%s)", self.cart[0][0])
            connection.commit()

        cursor.execute(f"SELECT ItemName, Price, Quantity FROM cartitems WHERE cartID = {self.cartID[0][0]}")
        self.cart = cursor.fetchall()

        for x in range(len(self.cart)):
            self.total_price += float(self.cart[x][1] * self.cart[x][2])

    def addItem(self, item):
        cursor.execute(f"SELECT ItemID FROM inventory WHERE ItemName='{item}'")
        item_id = cursor.fetchall()

        cursor.execute(f"SELECT ItemName FROM inventory WHERE ItemName='{item}'")
        item_name = cursor.fetchall()

        cursor.execute(f"SELECT Price FROM inventory WHERE ItemID='{item_id[0][0]}'")
        item_price = cursor.fetchall()

        cursor.execute(f"SELECT CartID FROM shoppingcart WHERE UserID='{self.userID}'")
        cart_id = cursor.fetchall()

        item_in_cart = False
        for x in range(len(self.cart)):
            if f'{item_name[0][0]}' == f'{self.cart[x][0]}':
                item_in_cart = True
        if not item_in_cart:
            cursor.execute(
                f"INSERT INTO cartitems (CartID, ItemID, ItemName, Price, Quantity) VALUES ('{cart_id[0][0]}', "
                f"'{item_id[0][0]}', '{item_name[0][0]}', '{item_price[0][0]}', 1)")
            connection.commit()

        else:
            cursor.execute(f"UPDATE cartitems SET Quantity=Quantity+1 WHERE ItemID = '{item_id[0][0]}'")
            connection.commit()

    def removeItem(self, item):
        cursor.execute(f"SELECT ItemID, Quantity FROM cartitems WHERE ItemName='{item}'")
        item_removal = cursor.fetchall()
        if f'{item_removal[0][1]}' == 1:
            cursor.execute(f"DELETE FROM cartitems WHERE ItemID = '{item_removal[0][0]}'")
            connection.commit()
        else:
            cursor.execute(f"UPDATE cartitems SET Quantity=Quantity-1 WHERE ItemID = '{item_removal[0][0]}'")
            connection.commit()

    def displayCart(self):
        while True:
            if len(self.cart) != 0:
                for x in range(len(self.cart)):
                    print(f'{self.cart[x][0]}', 'Price:', f'${self.cart[x][1]}', 'Quantity:', f'{self.cart[x][2]}')

                print("Total Price:", f'${self.total_price}')
                print('1) Remove item\n'
                      '2) Go back ')
                prompt = int(input())
                if prompt == 1:
                    ShoppingCart(user).removeItem(input('Enter the name of the item you wish to remove: '))
                elif prompt == 2:
                    return
            else:
                print('Cart is empty.\n'
                      '1) Go back')
                prompt = int(input())
                if prompt == 1:
                    return

    def checkout(self):
        cursor.execute(f"SELECT ItemID FROM cartitems WHERE CartID='{self.cartID[0][0]}'")
        item_id = cursor.fetchall()

        cursor.execute(f"SELECT ItemName FROM cartitems WHERE CartID='{self.cartID[0][0]}'")
        item_name = cursor.fetchall()

        cursor.execute(f"SELECT Price FROM cartitems WHERE CartID='{self.cartID[0][0]}'")
        item_price = cursor.fetchall()

        cursor.execute(f"SELECT Quantity FROM cartitems WHERE CartID='{self.cartID[0][0]}'")
        item_quantity = cursor.fetchall()

        cursor.execute(f"INSERT INTO orders (CartID, UserID, Price) VALUES "
                       f"('{self.cartID[0][0]}', '{self.userID}', '{self.total_price}')")
        connection.commit()

        cursor.execute(f"SELECT OrderID FROM orders WHERE UserID='{self.userID}'")
        order_id = cursor.fetchall()

        for x in range(len(self.cart)):
            cursor.execute(f"SELECT ItemID FROM inventory WHERE ItemName='{item_name[x][0]}'")
            item_stock_id = cursor.fetchall()
            cursor.execute(f"SELECT Stock FROM inventory WHERE ItemID='{item_stock_id[0][0]}'")
            item_stock = cursor.fetchall()

            if 0 >= item_stock[0][0] or item_stock[0][0] < item_quantity[x][0]:
                print('Sorry, unable to complete order.\n'
                      'Our stock may not be able to fulfill the order.')
            else:
                cursor.execute(f"INSERT INTO orderitems (OrderID, userID, ItemID, ItemName, Price, Quantity) VALUES "
                               f"('{order_id[0][0]}', '{self.userID}', '{item_id[x][0]}', '{item_name[x][0]}', "
                               f"'{item_price[x][0]}', '{item_quantity[x][0]}')")
                connection.commit()
                for i in range(item_quantity[x][0]):
                    cursor.execute(f"UPDATE inventory SET Stock=Stock-1 WHERE ItemName = '{item_name[x][0]}'")
                    connection.commit()
                cursor.execute(f"DELETE FROM cartitems WHERE CartID = '{self.cartID[0][0]}'")
