# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="nbs",
passwd ="NBs3#NBs"
)
# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
# cursorObject.execute("CREATE DATABASE TestDatabase")
cursorObject.execute("show databases")
lst = cursorObject.fetchall()
print(lst)