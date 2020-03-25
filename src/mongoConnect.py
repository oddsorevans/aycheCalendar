from pymongo import MongoClient
import datetime
import pprint

#function adds a user into the database
def addUser(fn, ln, email, bd, usern, passwd):
    #creates dictionary to store
    newUser = {
        'stFirstName' : fn,
        'stLastName' : ln,
        'stEmail' : email,
        'birthday' : bd,
        'stUsername' : usern,
        'stPassword' : passwd
    }
    #connects to user list inside Data db of the Ayche cluster
    client = MongoClient("mongodb://Ayche:3Y8yqtb23lSdbVmf@ayche-shard-00-00-7twqa.mongodb.net:27017,ayche-shard-00-01-7twqa.mongodb.net:27017,ayche-shard-00-02-7twqa.mongodb.net:27017/test?ssl=true&replicaSet=Ayche-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('Data')
    records = db.users
    #inserts student
    records.insert_one(newUser)
    #disconnect from server
    client.close()

def checkLogin(usern, passwd):
    client = MongoClient("mongodb://Ayche:3Y8yqtb23lSdbVmf@ayche-shard-00-00-7twqa.mongodb.net:27017,ayche-shard-00-01-7twqa.mongodb.net:27017,ayche-shard-00-02-7twqa.mongodb.net:27017/test?ssl=true&replicaSet=Ayche-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('Data')
    records = db.users
    #uses AND to check if the pair exists. Either returns dict or Nonetype
    isThere = records.find_one({
        '$and' : [
            {"stUsername" : usern},
            {"stPassword" : passwd}
        ]
    })
    #close and return value
    client.close()
    if isThere is None:
        return False
    else:
        return True

def checkEmailUser(usern, email):
    client = MongoClient("mongodb://Ayche:3Y8yqtb23lSdbVmf@ayche-shard-00-00-7twqa.mongodb.net:27017,ayche-shard-00-01-7twqa.mongodb.net:27017,ayche-shard-00-02-7twqa.mongodb.net:27017/test?ssl=true&replicaSet=Ayche-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('Data')
    records = db.users
    #uses OR to check if either already exist in a user. 
    exists = records.find_one({
        '$or' : [
            {"stUsername" : usern},
            {"stEmail" : email}
        ]
    })
    #close and return value
    client.close()
    if exists is None:
        return False
    else:
        return True