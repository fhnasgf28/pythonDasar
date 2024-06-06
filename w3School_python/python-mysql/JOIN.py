import mysql.connector

# create connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    database="mydatabase",
)
myCursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

myCursor.execute(sql)
myresult = myCursor.fetchall()

for x in myresult:
    print(x)
