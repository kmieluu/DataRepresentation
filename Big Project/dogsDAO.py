import mysql.connector

class DogsDao:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="dogs"
            #user=""
            #"passwd"="root" for mySQL
        )
        #print("connection made")

    def create(self, dogs):     
        cursor = self.db.cursor()
        sql = "INSERT INTO dogs (IKCReg, RegNum, age, breed, price, id) values (%s,%s,%s,%s,%s,%s)"
        values = [    
            dogs['IKCReg'],
            dogs['RegNum'],
            dogs['age'],
            dogs['breed'],
            dogs['price'],
            dogs['id']
            
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid   

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from dogs'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            #put dict object in the array
            returnArray.append(resultAsDict)
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql = 'select * from dogs where id = %s'
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)


    def update(self, dogs):
        cursor = self.db.cursor()
        sql = "update dogs set product = %s, quantity = %s, price = %s where id = %s"
        values = [    
            dogs['IKCReg'],
            dogs['RegNum'],
            dogs['age'],
            dogs['breed'],
            dogs['price'],
            dogs['id']
            
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return dogs   
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete * from dogs where id = %s'
        values = [id]
        cursor.execute(sql,values)
        return {}


dogsDao = DogsDao()
