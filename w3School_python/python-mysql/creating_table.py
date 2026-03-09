import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database="mydatabase",
)
myCursor = mydb.cursor()
myCursor.execute("SHOW TABLES")

for x in myCursor:
  print(x)