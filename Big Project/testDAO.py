from dogsDAO import dogsDao as dogsDao
    
dogs = {
    'IKCReg':"yes",
    'RegNum': 1,
    'age':12,
    'breed':'vizsla',
    'price':100
}

returnValue = dogsDao.getAll()
print(returnValue)
