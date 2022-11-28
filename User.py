import mysql.connector
import uuid
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


def update_user(user):
    arg = input("Would you like to update your card information(card) or address(address): ")
    if arg == "card":
        user.update_payment()
    elif arg == "address":
        user.update_address()
    else:
        print("Invalid input, cannot update " + arg)


# Create a new user object
def create_user():
    print("Please insert the following information to create an account: ")
    email = input("Enter email address: ")

    cursor.execute("SELECT * FROM USER WHERE Email = '{}'".format(email))
    temp = cursor.fetchall()
    if len(temp) > 0:
        print("Email already exists")
        return

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


def get_user(user_ID):
    cursor.execute("SELECT * FROM User WHERE UserID = '{}'".format(user_ID))
    data = cursor.fetchall()
    user = User(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5],
                data[0][6], data[0][7], data[0][8], data[0][9])
    return user


class User:
    def __init__(self, email, password, first, last, address_line, city, state, zip_code, card):
        self.email = email
        self.password = password
        self.first = first
        self.last = last
        self.address_line = address_line
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.card = card
        self.user_ID = uuid.uuid4()  # creates a unique id for each user
        cursor.execute('INSERT INTO user (Email, Password, FirstName, LastName, AddressLine, City, State, ZipCode, CardNumber, UserID) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format
                          (self.email, self.password, self.first, self.last, self.address_line, self.city, self.state, self.zip_code, self.card, self.user_ID))
        connection.commit()


    def __init__(self, email, password, first, last, address_line, city, state, zip_code, card, user_ID):
        self.email = email
        self.password = password
        self.first = first
        self.last = last
        self.address_line = address_line
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.card = card
        self.user_ID = user_ID

    def delete_user(self):
        cursor.execute("DELETE FROM user WHERE UserID = '" + str(self.user_ID) + "'")
        cursor.execute("DELETE FROM shoppingcart WHERE UserID = '{}'".format(self.user_ID))
        del self
        connection.commit()

    def set_email(self, email):
        self.email = email
        cursor.execute("UPDATE user SET Email = '" + email + "' WHERE UserID = '" + str(self.user_ID) + "'")

    def set_password(self, password):
        self.password = password
        cursor.execute("UPDATE user SET Password = '" + password + "' WHERE UserID = '" + str(self.user_ID) + "'")

    def set_first(self, first):
        self.first = first
        cursor.execute("UPDATE user SET FirstName = '" + first + "' WHERE UserID = '" + str(self.user_ID) + "'")

    def set_last(self, last):
        self.last = last
        cursor.execute("UPDATE user SET LastName = '" + last + "' WHERE UserID = '" + str(self.user_ID) + "'")

    def set_address_line(self, address):
        self.address_line = address
        cursor.execute("UPDATE user SET AddressLine = '" + address + "' WHERE UserID = '" + str(self.user_ID) + "'")

    def set_city(self, city):
        self.city = city
        cursor.execute("UPDATE user SET City = '" + city + "' WHERE UserID = '" + str(self.user_ID) + "'")

    def set_state(self, state):
        self.state = state
        cursor.execute("UPDATE user SET State = '" + state + "' WHERE UserID = '" + str(self.user_ID) + "'")

    def set_zip(self, zip_code):
        self.zip_code = zip_code
        cursor.execute("UPDATE user SET ZipCode = '" + zip_code + "' WHERE UserID = '" + str(self.user_ID) + "'")

    def set_card(self, card):
        self.card = card
        cursor.execute("UPDATE user SET Card = '" + card + "' WHERE UserID = '" + str(self.user_ID) + "'")

    def update_address(self):
        address = input("What is your new address line")
        city = input("What is your new city")
        state = input("What is your new state")
        zip_code = input("what is your new state")

        self.set_address_line(address)
        self.set_city(city)
        self.set_state(state)
        self.set_zip(zip_code)
        connection.commit()

    def update_payment(self):
        card = int(input("What is your card number: "))
        self.set_card(card)
        connection.commit()