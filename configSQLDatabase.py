import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Juing02a",
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE consid")