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

    print("Successful connection.")
except:
    print("Failed connection.")
    sys.exit()

cursor = connection.cursor()


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

    def delete_user(self):
        cursor.execute("DELETE * FROM `user` WHERE UserID = '" + self.user_ID + "'")
        del self;
        connection.commit();

    def set_email(self, email):
        self.email = email
        cursor.execute("UPDATE user SET Email = '" + email + "' WHERE UserID = '" + self.user_ID + "'")

    def set_password(self, password):
        self.password = password
        cursor.execute("UPDATE user SET Password = '" + password + "' WHERE UserID = '" + self.user_ID + "'")

    def set_first(self, first):
        self.first = first;
        cursor.execute("UPDATE user SET FirstName = '" + first + "' WHERE UserID = '" + self.user_ID + "'")

    def set_last(self, last):
        self.last = last;
        cursor.execute("UPDATE user SET LastName = '" + last + "' WHERE UserID = '" + self.user_ID + "'")

    def set_address_line(self, address):
        self.address_line = address;
        cursor.execute("UPDATE user SET AddressLine = '" + address + "' WHERE UserID = '" + self.user_ID + "'")

    def set_city(self, city):
        self.city = city
        cursor.execute("UPDATE user SET City = '" + city + "' WHERE UserID = '" + self.user_ID + "'")

    def set_state(self, state):
        self.state = state
        cursor.execute("UPDATE user SET State = '" + state + "' WHERE UserID = '" + self.user_ID + "'")

    def set_zip(self, zip_code):
        self.zip_code = zip_code
        cursor.execute("UPDATE user SET ZipCode = '" + zip_code + "' WHERE UserID = '" + self.user_ID + "'")

    def set_card(self, card):
        self.card = card
        cursor.execute("UPDATE user SET Card = '" + card + "' WHERE UserID = '" + self.user_ID + "'")

    def update_address(self):
        address = input("What is your new address line")
        city = input("What is your new city")
        state = input("What is your new state")
        zip_code = input("what is your new state")

        self.set_address(address)
        self.set_city(city)
        self.set_state(state)
        self.set_zip(zip_code)
        connection.commit()

    def update_payment(self):
        card = int(input("What is your card number: "))
        self.set_card(card)
        connection.commit()