from User import *
from Inventory import *
from shoppingcart import *
from order import *
from Book import *
from Movie import *
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


def logged_in_loop(userID):
    logged_in_user = get_user(userID)  # stores the logged in user in a variable
    while(True):
        print("Logged in successfully\n")
        command = input(
            "What would you like to do:\n"
            "delete - delete your account\n"
            "update - update account information\n"
            "logout - log out of your account\n"
            "history - view your order history\n"
            "view - display all the merchandise in a category\n"
            "cart - views the contents of a users shopping cart\n"
            "add - add an item to a shopping cart \n"
            "remove - remove an item from the shopping cart\n"
            "checkout - check out the items in a shopping cart \n"
            "exit - exit program\n"
            ">> "
        )
        if command == 'exit':
            print("Closing...")
            sys.exit()
        elif command == 'delete':
            logged_in_user.delete_user()
            break
        elif command == 'update':
            update_user(logged_in_user)
        elif command == "logout":
            print("Logging out...")
            break
        elif command == 'history':
            Order(userID).orderHistory()


def start_loop():
    while True:
        command = input(
            "What would you like to do:\n"
            "create - Create User\n"
            "login - Login to an existing account\n"
            "exit - Exit program\n"
            ">> "
        )
        if command == "exit":
            print("Closing...")
            sys.exit()
        elif command == "login":
            user = login()
            if user == None:
                print("Failed to log in\n")
                continue
            else:
                logged_in_loop(user)
                continue
        elif command == "create":
            create_user()
        else:
            print("Command does not exist")
            continue


if __name__ == '__main__':
    start_loop()


