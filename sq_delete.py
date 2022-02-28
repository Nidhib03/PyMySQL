# importing required library
import mysql.connector

# connecting to the database
dataBase = mysql.connector.connect(
					host = "localhost",
					user = "nbs",
					passwd = "NBs3#NBs",
					database = "geeks4geeks" )

# preparing a cursor object
cursorObject = dataBase.cursor()

# inserting data into the table
# query = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (%s, %s, %s, %s, %s)"

# attrValues = ("Rituraj Saha", "Information Technology", 1706256, "IT-3", 20)
# cursorObject.execute(query, attrValues)

# attrValues = ("Ritam Barik", "Information Technology", 1706254, "IT-3", 21)
# cursorObject.execute(query, attrValues)

# attrValues = ("Rishi Kumar", "Information Technology", 1706253, "IT-3", 21)
# cursorObject.execute(query, attrValues)

# # # deleting query
query = "DELETE FROM STUDENT WHERE ROLL = 1706254"
cursorObject.execute(query)
		
# q = "DELETE FROM Student WHERE Name NOT IN (SELECT Name FROM Student GROUP BY Name, Roll_no)"
# cursorObject.execute(q)

dataBase.commit()

# disconnecting from server
dataBase.close()