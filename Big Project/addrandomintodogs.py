import mysql.connector

db=mysql.connector.connect(
    host = 'localhost',
    user='root',
    password = 'root',
    database = 'dogs'

)

cursor = db.cursor()
sql = 'insert into dogs (IKCReg, RegNu, age, breed , price) values (%s, %s, %s, %s, %s)'
values = ("yes", 1, 12, "vizsla", 100)
cursor.execute(sql, values)

db.commit()
print ("1 record inserted, ID:", cursor.lastrowid)