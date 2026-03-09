import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database="mydatabase",
)
myCursor = mydb.cursor()

sql = 'DELETE FROM customers WHERE address = "Mountain 21"'
myCursor.execute(sql)

mydb.commit()


print(myCursor.rowcount, 'record(s) deleted')
