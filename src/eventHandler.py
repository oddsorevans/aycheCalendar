#after the events are pulled by mongoConnect, this will hold the events, and search through them
import mongoConnect
import pprint
import bson
import datetime

class events():
    def __init__(self, usern):
        super().__init__()
        self.eventOwner = usern
        self.allEvents = mongoConnect.getUserEvents(usern)

    def printContents(self):
        pprint.pprint(self.allEvents)
    
    def updateEvent(self, origin, usern, date, title, desc, color, notes, endTime):
        #update in db
        mongoConnect.updateEvent(origin, usern, date, title, desc, color, notes, endTime)
        #update locally
        updated = {
            '_id':origin,
            'stUser':usern, #string
            'date':date, #datetime
            'stTitle':title, #string
            'stDesc':desc, #string
            'iaColor':color, #list length 3
            'stAddNotes':notes, #string
            'dateEndTime':endTime #datetime
        }
        self.allEvents[0].update(updated)
    
    def createEvent(self, usern, date, title, desc, color, notes, endTime):
        

# testing = events("streams")
# testing.printContents()
# origin = bson.ObjectId('5eada87cfca888703584f0db')
# testing.updateEvent(origin, "streams", datetime.datetime(2020, 5, 2, 0, 0), 'updated', 'this is updated', [15,15,15], 'i just updated this', datetime.datetime(2020,5,2,5,0))
# testing.printContents()