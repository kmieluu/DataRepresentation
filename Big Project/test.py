import mysql.connector

class DogsDao :
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="dogs"
            #user=""
            #"passwd"="root" for mySQL
        )
        print("connection made")

DogsDao = DogsDao


