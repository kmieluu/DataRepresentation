from dogsDao import dogsDao

dogs = {
    'IKCReg':"Yes",
    'RegNum':123,
    'Age':12,
    'breed':"vizsla",
    'price':123,
    'ID':1,
    
}

returnvalue = dogsDao.create(dogs)
print(returnvalue)