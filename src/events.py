# Creating the event class that will handle all of the data held for each given event, as well as a table that can hold the events
import datetime

class event():

    def __init__(self, eName, eDate, eDuration, eStart, eEnd, eDay, eFamily, eNotes):
        super().__init__()
        self.name = eName # default name for event
        self.day = datetime.strptime(eDate, '%y-%m-%d') # day is stored as date time object
        self.duration = eDuration # how many days will it last?
        self.startTime = eStart # time event starts
        self.endTime = eEnd # time event starts
        self.allDay = eDay # is it all day? can override time
        self.family = eFamily # what group does it belong to?
        self.notes = eNotes # additional notes about event

class eventTable():
    def __init__(self):
        super().__init__()
        self.eventsTable = {} #dictionary to hold all events for user

    def addEvent(self, toAdd): # check for family presence, and then append event to eventTable list
