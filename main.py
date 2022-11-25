from User import User
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


def createUser():
    print("Please insert the following information to create an account: ")
    email = input("Enter email address: ")
    password = input("Enter account password: ")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    address = input("Enter your address line: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zip_code = int(input("Enter your zip code: "))
    card = int(input("Enter your card number: "))

    temp = User(email, password, first, last, address, city, state, zip_code, card)
    return temp


# Asks a user for a username and password, and finds its matching pair in the table, returns none if no match is found
def login():
    email = input("What is your email address: ")
    password = input("What is your password: ")
    cursor.execute("SELECT Password FROM user WHERE Email = '{}'".format(email))
    found_password = cursor.fetchone()
    for x in range(len(found_password)):
        print(found_password[x])
        print(password)
        if found_password[x] == password:
            cursor.execute("Select UserID FROM user WHERE Email = '{}'".format(email))
            userID = cursor.fetchone()
            return userID[0]
    return None


def loggedInLoop(userID):
    while(True):
        print("Logged in successfully\n")
        command = input(
            "What would you like to do:\n"
            "delete - delete your account\n"
            "update - update account information\n"
            "logout - log out of your account"
            "exit - Exit program\n"
            ">> "
        )
        if command == 'exit':
            print("Closing...")
            sys.exit()
        elif command == 'delete':
            break #placeholder
        elif command == 'update':
            break #placeholder
        elif command == "logout":
            print("Logging out...")
            break


def startLoop():
    while True:
        command = input(
            "What would you like to do:\n"
            "create - Create User\n"
            "login - Login to an existing account\n"
            "exit - Exit program\n"
            ">> "
        )
        if(command == "exit"):
            print("Closing...")
            sys.exit
        elif (command == "login"):
            user = login()
            if (user == None):
                print("Failed to log in\n")
                continue
            else:
                loggedInLoop(user)
        elif (command == "create"):
            createUser()
        else:
            print("Command does not exist")
            continue


if __name__ == '__main__':
    startLoop()


