from pymongo import MongoClient
import connectionStrings #updated 4/1/2020
import datetime
import time
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
    client = MongoClient(connectionStrings.connectionKey)
    db = client.get_database('Data')
    records = db.users
    #inserts student
    records.insert_one(newUser)
    #disconnect from server
    client.close()

def checkLogin(usern, passwd):
    #used to test performance
    #start = time.time()
    client = MongoClient(connectionStrings.connectionKey)
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
    # used to test performance
    #elapsed = time.time() - start
    #print(elapsed)
    if isThere is None:
        return False
    else:
        return True

def checkEmailUser(usern, email):
    client = MongoClient(connectionStrings.connectionKey)
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

# for i in range(0,1000):
#     checkLogin("streams", "mayonnaise")