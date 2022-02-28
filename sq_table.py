# Enter the server name in host followed by your user and password along with the database name provided by you.

import mysql.connector
# connecting to the database
dataBase = mysql.connector.connect(
					host = "localhost",
					user = "nbs",
					passwd = "NBs3#NBs",
					database = "geeks4geeks" )
# creating table
studentRecord = """CREATE TABLE STUDENT (NAME VARCHAR(20) NOT NULL, BRANCH VARCHAR(50), ROLL INT NOT NULL, SECTION VARCHAR(5), AGE INT)"""
# preparing a cursor object
cursorObject = dataBase.cursor()
# table created
cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()

#OR

# Python code for creating Table in the Database Host: It is the server name. It will be "localhost" if you are using localhost database
def CreateTable():
	# Connecting To the Database in Localhost
	DataBase = mysql.connector.connect(
				host ="localhost",
				user ="nbs",
				password ="NBs3#NBs",
				database ="geeks4geeks")
	# Cursor to the database
	Cursor = DataBase.cursor()

	# Query for Creating the table The student table contains two columns Name and Name of data type varchar i.e to store string and Roll number of the integer data type.
	TableName ="CREATE TABLE Student( Name VARCHAR(255), Roll_no int);"

	Cursor.execute(TableName)
	print("Student Table is Created in the Database")
	return
# Calling CreateTable function
CreateTable()