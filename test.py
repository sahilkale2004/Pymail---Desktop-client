import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="USER"
)

mycursor =mydb.cursor()

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)


    