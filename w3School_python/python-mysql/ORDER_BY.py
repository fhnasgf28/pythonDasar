import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database="mydatabase",
)
myCursor = mydb.cursor()

sql = 'SELECT * FROM customers ORDER BY name'
myCursor.execute(sql)

myResult = myCursor.fetchall()

for x in myResult:
    print(x)
