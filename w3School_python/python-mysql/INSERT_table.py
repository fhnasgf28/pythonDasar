import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database="mydatabase",
)
myCursor = mydb.cursor()

sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
val = ('John', 'Highway 21')
myCursor.execute(sql, val)

mydb.commit()

print(myCursor.rowcount, 'record inserted')