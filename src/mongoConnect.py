from pymongo import MongoClient
import connectionStrings #updated 4/1/2020
import datetime
import time
import pprint
import bcrypt
import bson

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
    print(isThere)
    # used to test performance
    #elapsed = time.time() - start
    #print(elapsed)

    #if nothing returned, false
    if isThere is None:
        return False
    #username exists, check password
    else:
        return bcrypt.checkpw(passwd.encode(), isThere["stPassword"].encode())

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

def changePassword(usern, opass, npass):
    client = MongoClient(connectionStrings.connectionKey)
    db = client.get_database('Data')
    records = db.users
    #uses AND to check if the pair exists. Either returns dict or Nonetype
    isThere = records.find_one(
        {"stUsername" : usern}
    )
    #if nothing returned, false
    if isThere is None:
        client.close()
        return False
    #username exists, check password
    else:
        #password exists
        if bcrypt.checkpw(opass.encode(), isThere["stPassword"].encode()):
            #hash password
            salt = bcrypt.gensalt()
            #use encode() to turn string to byte for processing
            hashed = bcrypt.hashpw(npass.encode(), salt)
            #turn from byte to string
            hashed = hashed.decode()
            records.find_one_and_update({"stUsername" : usern}, {"$set" : {"stPassword" : hashed}})
            client.close()
            return True
        else:
            client.close()
            return False

def getUserEvents(usern):
    client = MongoClient(connectionStrings.connectionKey)
    db = client.get_database('Data')
    records = db.events

    #get all user events for that user. WIll be stored in a local JSON
    events = list(records.find({"stUser" : usern}))

    client.close()
    pprint.pprint(events)
    return events

def addEvent(usern, date, title, desc, color, notes, endTime):
    newEvent = {
        'stUser':usern, #string
        'date':date, #datetime
        'stTitle':title, #string
        'stDesc':desc, #string
        'iaColor':color, #list length 3
        'stAddNotes':notes, #string
        'dateEndTime':endTime #datetime
    }

    client = MongoClient(connectionStrings.connectionKey)
    db = client.get_database('Data')
    records = db.events
    records.insert_one(newEvent)
    client.close()

def updateEvent(origin, usern, date, title, desc, color, notes, endTime):
    query = {"_id":origin}
    updated = { "$set": {
        'stUser':usern, #string
        'date':date, #datetime
        'stTitle':title, #string
        'stDesc':desc, #string
        'iaColor':color, #list length 3
        'stAddNotes':notes, #string
        'dateEndTime':endTime #datetime
    } }

    client = MongoClient(connectionStrings.connectionKey)
    db = client.get_database('Data')
    records = db.events

    records.find_one_and_update(query, updated, upsert=True)
    client.close()
    print("event updated")

def deleteEvent(origin):
    client = MongoClient(connectionStrings.connectionKey)
    db = client.get_database('Data')
    records = db.events
    records.delete_one({"_id" : origin})
    client.close()

def deleteUser(usern, passwd):
    #check if usern and passwd are correct
    if checkLogin(usern, passwd):
        #delete all cases in the events database
        client = MongoClient(connectionStrings.connectionKey)
        db = client.get_database('Data')
        records = db.events
        records.delete_many({"stUser" : usern})
        #delete user
        records = db.users
        records.delete_one({"stUsername" : usern})
        client.close()
        return True
    else:
        return False

