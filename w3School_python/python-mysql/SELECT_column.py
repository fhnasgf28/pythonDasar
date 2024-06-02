import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database="mydatabase",
)
myCursor = mydb.cursor()

myCursor.execute('SELECT name, address FROM customers')

myresult = myCursor.fetchall()

for x in myresult:
    print(x)

