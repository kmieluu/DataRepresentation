import mysql.connector

db=mysql.connector.connect(
    host = 'localhost',
    user='root',
    password = 'root',
    database = 'dogs'

)

cursor = db.cursor()
sql = 'CREATE TABLE test2 (IKCReg varchar(5), RegNu int PRIMARY KEY, age  int, breed varchar(250), price int)'

cursor.execute(sql)

print ("Connection made.")