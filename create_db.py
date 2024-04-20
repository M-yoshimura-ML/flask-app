# pip install mysql-connector
# pip install mysql-connector-python

# below command might get error
# pip install mysql-connector-python-rf

# pip install pymysql
# pip install cryptography
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3360",
    user="admin",
    password="password!admin"
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE flask_app3 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

