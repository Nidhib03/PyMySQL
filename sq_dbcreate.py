import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="nbs",
passwd ="NBs3#NBs"
)

#preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE geeks4geeks")