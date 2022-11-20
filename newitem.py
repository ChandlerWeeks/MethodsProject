import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="project1")

mycursor = db.cursor()

ItemID = input("Enter ItemID")
ItemName = input("Enter ItemName")
Price = input("Enter Price")
Rating = input("Enter Rating")
Stock = input("Enter Stock")
mycursor.execute("INSERT INTO Inventory VALUES (ItemID, ItemName, Price, Rating, Stock)")
