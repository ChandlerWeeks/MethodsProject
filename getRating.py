import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="project1")

mycursor = db.cursor()

ion = input("Enter Rating")
mycursor.execute("Select FROM Inventory WHERE Rating=ion")
