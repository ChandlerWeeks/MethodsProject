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
        self.quantity = 0
        self.price = 0

        cursor.execute(f"SELECT cartID FROM shoppingcart WHERE UserID = '{self.userID}'")
        self.cartID = cursor.fetchall()

        if len(self.cartID) != 0:
            pass
        else:
            cursor.execute(f"INSERT INTO shoppingcart (UserID) VALUES ('{self.userID}')")
            connection.commit()

    def addItem(self):
        while True:
            add_item = input('Enter the name of the item you wish to add (c to cancel): ')
            if add_item == 'c':
                return
            elif add_item == '':
                continue
            cursor.execute(f"SELECT ItemName FROM inventory WHERE ItemName='{add_item}'")
            item_name = cursor.fetchall()
            if not item_name:
                print('Item not found in inventory.\n')
                continue

            cursor.execute(f"SELECT ItemID FROM inventory WHERE ItemName='{item_name[0][0]}'")
            item_id = cursor.fetchall()

            cursor.execute(f"SELECT Price FROM inventory WHERE ItemID='{item_id[0][0]}'")
            self.price = cursor.fetchall()

            cursor.execute(f"SELECT CartID FROM shoppingcart WHERE UserID='{self.userID}'")
            cart_id = cursor.fetchall()

            cursor.execute(f"SELECT ItemName FROM cartitems WHERE cartID='{cart_id[0][0]}'")
            self.cart = cursor.fetchall()

            item_in_cart = False
            for x in range(len(self.cart)):
                if f'{item_name[0][0]}' == f'{self.cart[x][0]}':
                    item_in_cart = True

            if not item_in_cart:
                cursor.execute(
                    f"INSERT INTO cartitems (CartID, ItemID, ItemName, Price, Quantity) VALUES ('{cart_id[0][0]}', "
                    f"'{item_id[0][0]}', '{item_name[0][0]}', '{self.price[0][0]}', 1)")
                connection.commit()

            else:
                cursor.execute(f"UPDATE cartitems SET Quantity=Quantity+1 WHERE ItemID = '{item_id[0][0]}'")
                connection.commit()
            return print('Item added\n')

    def removeItem(self):
        while True:
            remove_item = input('Enter the name of the item you wish to remove (c to cancel): ')
            if remove_item == 'c':
                return
            elif remove_item == '':
                continue
            cursor.execute(f"SELECT ItemID, Quantity FROM cartitems WHERE ItemName='{remove_item}'")
            item_removal = cursor.fetchall()
            if not item_removal:
                print('Item not found in cart.\n')
                continue
            if item_removal[0][1] <= 1:
                cursor.execute(f"DELETE FROM cartitems WHERE ItemID = '{item_removal[0][0]}'")
                connection.commit()
            else:
                cursor.execute(f"UPDATE cartitems SET Quantity=Quantity-1 WHERE ItemID = '{item_removal[0][0]}'")
                connection.commit()
            return print('Item removed\n')

    def clearCart(self):
        cursor.execute(f"DELETE FROM cartitems WHERE CartID = '{self.cartID[0][0]}'")
        connection.commit()
        return print('Cart cleared.')

    def displayCart(self):
        while True:
            self.total_price = 0
            cursor.execute(f"SELECT ItemName, Price, Quantity FROM cartitems WHERE cartID = '{self.cartID[0][0]}'")
            self.cart = cursor.fetchall()

            for x in range(len(self.cart)):
                self.total_price += float(self.cart[x][1] * self.cart[x][2])

            print('Cart')
            print(''.ljust(100, '-'))
            if len(self.cart) != 0:
                for x in range(len(self.cart)):
                    print(f'{self.cart[x][0]},', 'Price:', f'${self.cart[x][1]}', 'Quantity:', f'{self.cart[x][2]}')

                print(''.ljust(100, '-'))
                print("Total price: ${0:.4g}".format(self.total_price))
                print(''.ljust(20, '-'))
                print('1) Remove item\n'
                      '2) Go back ')
                prompt = (input())
                if prompt == '1':
                    ShoppingCart(self.userID).removeItem()
                elif prompt == '2':
                    return
                else:
                    continue
            else:
                print('Cart is empty.\n'
                      '1) Go back')
                prompt = input()
                if prompt == '1':
                    return
                else:
                    continue

    def checkout(self):
        order_id = None
        cursor.execute(f"SELECT ItemName, Price, Quantity FROM cartitems WHERE cartID = '{self.cartID[0][0]}'")
        self.cart = cursor.fetchall()

        for x in range(len(self.cart)):
            self.total_price += float(self.cart[x][1] * self.cart[x][2])

        cursor.execute(f"SELECT ItemID FROM cartitems WHERE CartID='{self.cartID[0][0]}'")
        item_id = cursor.fetchall()

        cursor.execute(f"SELECT ItemName FROM cartitems WHERE CartID='{self.cartID[0][0]}'")
        item_name = cursor.fetchall()

        cursor.execute(f"SELECT Price FROM cartitems WHERE CartID='{self.cartID[0][0]}'")
        self.price = cursor.fetchall()

        cursor.execute(f"SELECT Quantity FROM cartitems WHERE CartID='{self.cartID[0][0]}'")
        self.quantity = cursor.fetchall()

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

            if 0 >= item_stock[0][0] or item_stock[0][0] < self.quantity[x][0]:
                print('Sorry, unable to complete order.\n'
                      'Our stock may not be able to fulfill the order.')
            else:
                try:
                    cursor.execute(
                        f"INSERT INTO orderitems (OrderID, userID, ItemID, ItemName, Price, Quantity) VALUES "
                        f"('{order_id[0 - 1][0]}', '{self.userID}', '{item_id[x][0]}', '{item_name[x][0]}', "
                        f"'{self.price[x][0]}', '{self.quantity[x][0]}')")
                    connection.commit()
                    for z in range(self.quantity[x][0]):
                        cursor.execute(f"UPDATE inventory SET Stock=Stock-1 WHERE ItemName = '{item_name[x][0]}'")
                        connection.commit()
                    cursor.execute(f"DELETE FROM cartitems WHERE CartID = '{self.cartID[0][0]}'")
                    connection.commit()
                except Exception as e:
                    print('Something went wrong', e)
        return print('Checkout complete.')
