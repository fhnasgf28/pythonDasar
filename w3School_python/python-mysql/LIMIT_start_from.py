import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database="mydatabase",
)
myCursor = mydb.cursor()

myCursor.execute('SELECT * FROM customers LIMIT 5 OFFSET 2')

my_result = myCursor.fetchall()


for x in my_result:
    print(x)
