import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database="mydatabase",
)
myCursor = mydb.cursor()

sql = 'UPDATE customers SET address = %s WHERE address = %s'
val = ("Valley 345", 'Canyon 123')
myCursor.execute(sql, val)

mydb.commit()


print(myCursor.rowcount, 'record(s) deleted')
