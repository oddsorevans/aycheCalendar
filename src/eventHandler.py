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
        self.sortAllEvents()

    def printContents(self):
        pprint.pprint(self.allEvents)
    
    def updateEvent(self, origin, date, title, desc, color, notes, endTime):
        #update in db
        mongoConnect.updateEvent(origin, self.eventOwner, date, title, desc, color, notes, endTime)
        #update locally
        updated = {
            '_id':origin,
            'stUser':self.eventOwner, #string
            'date':date, #datetime
            'stTitle':title, #string
            'stDesc':desc, #string
            'iaColor':color, #list length 3
            'stAddNotes':notes, #string
            'dateEndTime':endTime #datetime
        }
        for events in self.allEvents:
            if origin == events['_id']:
                events.update(updated)
        self.sortAllEvents()#sort incase dates change
    
    def createEvent(self, date, title, desc, color, notes, endTime):
        mongoConnect.addEvent(self.eventOwner, date, title, desc, color, notes, endTime)
        origin = mongoConnect.getObjectId(self.eventOwner, title, date)
        toAdd = {
            '_id':origin,
            'stUser':self.eventOwner, #string
            'date':date, #datetime
            'stTitle':title, #string
            'stDesc':desc, #string
            'iaColor':color, #list length 3
            'stAddNotes':notes, #string
            'dateEndTime':endTime #datetime
        }
        self.allEvents.append(toAdd)#id doesnt exist, so adds
        self.sortAllEvents()

    def deleteEvent(self, origin):
        mongoConnect.deleteEvent(origin)
        for events in self.allEvents:
            if origin == events['_id']:
                self.allEvents.remove(events)

    def searchByDate(self, date):
        inOrder = []
        for events in self.allEvents:
            if date == events['date'].date():
                #pprint.pprint(events)
                inOrder.append(events)
        return sorted(inOrder, key = lambda i: i['date'])

    def searchByColor(self, color):
        inOrder = []
        for events in self.allEvents:
            if color == events['iaColor']:
                #pprint.pprint(events)
                inOrder.append(events)
        return sorted(inOrder, key = lambda i: i['date'])
    
    def sortAllEvents(self):
        self.allEvents = sorted(self.allEvents, key = lambda i: i['date'])
            
        
# testing = events("streams")
# testing.createEvent(datetime.datetime(2020,5,2,6,0,0), 'testing10', 'hello', [10,10,10], 'hopefully this gets sorted', datetime.datetime(2020,5,2,0,0,0))
# checking = testing.searchByDate(datetime.date(2020,5,2))
# pprint.pprint(checking)
# testing.printContents()