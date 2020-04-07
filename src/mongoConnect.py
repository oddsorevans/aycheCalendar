from pymongo import MongoClient
import connectionStrings #updated 4/1/2020
import datetime
import time
import pprint
import bcrypt

#function adds a user into the database
def addUser(fn, ln, email, bd, usern, passwd):
    #hash password
    salt = bcrypt.gensalt()
    #use encode() to turn string to byte for processing
    hashed = bcrypt.hashpw(passwd.encode(), salt)
    #turn from byte to string
    hashed = hashed.decode()
    #creates dictionary to store
    newUser = {
        'stFirstName' : fn,
        'stLastName' : ln,
        'stEmail' : email,
        'birthday' : bd,
        'stUsername' : usern,
        'stPassword' : hashed
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
    isThere = records.find_one(
        {"stUsername" : usern}
    )
    #close and return value
    client.close()
    # used to test performance
    #elapsed = time.time() - start
    #print(elapsed)

    #if nothing returned, false
    if isThere is None:
        return False
    #username exists, check password
    else:
        if bcrypt.checkpw(passwd.encode(), isThere["stPassword"].encode()):
            return True
        else:
            return False

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