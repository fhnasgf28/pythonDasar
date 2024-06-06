import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database="mydatabase",
)
myCursor = mydb.cursor()

sql = 'DELETE FROM customers WHERE address = %s'
adr = ("Yellow Garden 2",)
myCursor.execute(sql, adr)

mydb.commit()


print(myCursor.rowcount, 'record(s) deleted')
