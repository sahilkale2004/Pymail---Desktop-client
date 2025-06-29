import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin@123",  # Ensure this matches your .env file
    database="USER"
)

mycursor =mydb.cursor()

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)


    