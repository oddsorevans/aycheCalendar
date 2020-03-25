from pymongo import MongoClient
import datetime

def addUser(fn, ln, email, bd, usern, passwd):
    newUser = {
        'stFirstName' : fn,
        'stLastName' : ln,
        'stEmail' : email,
        'birthday' : bd,
        'stUsername' : usern,
        'stPassword' : passwd
    }
    return newUser

client = MongoClient("mongodb://Ayche:3Y8yqtb23lSdbVmf@ayche-shard-00-00-7twqa.mongodb.net:27017,ayche-shard-00-01-7twqa.mongodb.net:27017,ayche-shard-00-02-7twqa.mongodb.net:27017/test?ssl=true&replicaSet=Ayche-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('Data')
records = db.users
records.insert_one(addUser(
    'test',
    'test',
    'test@test.test',
    datetime.datetime(1999,2,26,0,0,0),
    'test',
    'test'
))