
import mysql.connector as mc

mydb = mc.connect(
    host = "localhost",
    user = "nbs",
    password = "NBs3#NBs",
    database = "geeks4geeks")

mycursor = mydb.cursor()

# sql = "INSERT INTO Student (Name, Roll_no) VALUES (%s, %s)"
# val = ("Ram", "85")
# mycursor.execute(sql, val)

sql = "INSERT INTO Student (Name, Roll_no) VALUES (%s, %s)"
val = [("Akash", 98),
	("Neel", 23),
	("Rohan", 43),
	("Amit", 87),
	("Anil", 45),
	("Megha", 55),
	("Sita", 95)]

# d = "DELETE FROM Student WHERE Name = 'Ram'"
# mycursor.execute(d)

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "detail inserted")

# disconnecting from server
mydb.close()

