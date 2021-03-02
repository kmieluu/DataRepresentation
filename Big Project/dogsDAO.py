import mysql.connector

class dogsDao:
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
        sql = 'select * from stock'
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
        sql = 'select * from stock where id = %s'
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)


    def update(self, stock):
        cursor = self.db.cursor()
        sql = "update stock set product = %s, quantity = %s, price = %s where id = %s"
        values = [    
            stock['product'],
            stock['quantity'],
            stock['price'],
            stock['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return stock   
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete * from stock where id = %s'
        values = [id]
        cursor.execute(sql,values)
        return {}

    # function to convert result to dict
    def convertToDict(self, result):
        colnames = ['id','product','quantity','price']
        stock = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                stock[colName] = value
        return stock

stockDao = StockDao()
