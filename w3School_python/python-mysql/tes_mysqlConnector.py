import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
)
myCursor = mydb.cursor()
myCursor.execute("SHOW DATABASES")

for x in myCursor:
  print(x)