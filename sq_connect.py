# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="nbs",
passwd ="NBs3#NBs"
)
print(dataBase)
# Disconnecting from the server
dataBase.close()