# importing required library
import mysql.connector as mc
	
# connecting to the database
dataBase = mc.connect(
					host = "localhost",
					user = "nbs",
					passwd = "NBs3#NBs",
					database = "geeks4geeks" )
	
# preparing a cursor object
cursorObject = dataBase.cursor()
	
print("Displaying NAME and ROLL_no columns from the STUDENT table:")

# selecting query

query = "SELECT roll_no, name FROM Student"
query = "SELECT * FROM Student"
 # selected last query
query = "select * from Student where Roll_no >= 85;"

cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
	print(x)

# disconnecting from server
dataBase.close()