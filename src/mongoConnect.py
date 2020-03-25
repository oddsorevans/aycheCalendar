from pymongo import MongoClient
import datetime
import pprint

def addUser(fn, ln, email, bd, usern, passwd):
    newUser = {
        'stFirstName' : fn,
        'stLastName' : ln,
        'stEmail' : email,
        'birthday' : bd,
        'stUsername' : usern,
        'stPassword' : passwd
    }
    client = MongoClient("mongodb://Ayche:3Y8yqtb23lSdbVmf@ayche-shard-00-00-7twqa.mongodb.net:27017,ayche-shard-00-01-7twqa.mongodb.net:27017,ayche-shard-00-02-7twqa.mongodb.net:27017/test?ssl=true&replicaSet=Ayche-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('Data')
    records = db.users
    records.insert_one(newUser)

def checkLogin(usern, passwd):
    client = MongoClient("mongodb://Ayche:3Y8yqtb23lSdbVmf@ayche-shard-00-00-7twqa.mongodb.net:27017,ayche-shard-00-01-7twqa.mongodb.net:27017,ayche-shard-00-02-7twqa.mongodb.net:27017/test?ssl=true&replicaSet=Ayche-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database('Data')
    records = db.users
    pprint.pprint(records.find_one({
        '$and' : [
            {"stUsername" : "streams"},
            {"stPassword" : "mayonnaise"}
        ]
    }))

checkLogin("blah", "blah")