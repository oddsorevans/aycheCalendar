import sys
import eventHandler
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QGridLayout, QGroupBox, QVBoxLayout, QPushButton, QCalendarWidget, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot, QDate
from CreateEventWindow import CreateEventWindow

class monthObject(QWidget):
    def __init__(self, uname):
        super().__init__()

        self.events = eventHandler.events(uname)

        grid = QGridLayout()
        #upcoming events
        grid.addWidget(self.createUCEScrollBox(), 0, 0, 3, 3)
        #events for specific day
        grid.addWidget(self.createDayEventObject(), 0, 4, 3, 3)
        #creates calendar
        grid.addWidget(self.createCelendar(), 3, 0, 6, 7)
        #creates button groupbox
        grid.addWidget(self.createButtonsObject(), 0, 3, 3, 1)

        self.createUCEList()

        self.setLayout(grid)

    def createUCEList(self):
        self.UCEvents = QGroupBox("")

        self.title = QLabel(self)
        self.desc = QLabel(self)
        self.notes = QLabel(self)
        self.sTime = QLabel(self)
        self.eTime = QLabel(self)
        self.UCEvbox = QVBoxLayout()

        for things in self.events.allEvents:
            #self.rgbColor = f"rgb:{tuple(things['iaColor'])}"
            #self.UCEvents.styleSheet("background-color:rgbColor")

            self.title.setText(things['stTitle'])
            self.desc.setText(things['stDesc'])
            self.notes.setText(things['stAddNotes'])
            self.sTime.setText(str(things['date']))
            self.eTime.setText(str(things['dateEndTime']))

            self.UCEvbox.addWidget(self.title)
            self.UCEvbox.addWidget(self.desc)
            self.UCEvbox.addWidget(self.notes)
            self.UCEvbox.addWidget(self.sTime)
            self.UCEvbox.addWidget(self.eTime)

            self.UCEvbox.addStretch(1)
            self.UCEvents.setLayout(self.UCEvbox)
            self.UCEScroll.setWidget(self.UCEvents)
        

    def createCelendar(self):
        self.calGroupBox = QGroupBox("")

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumHeight(350)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.calendar)
        self.vbox.addStretch(1)
        self.calGroupBox.setLayout(self.vbox)

        return self.calGroupBox

    #creates groupbox for Upcoming Events
    def createUCEScrollBox(self):
        self.UCEGroupBox = QGroupBox("")

        self.UCE = QLabel(self)
        self.UCE.setText("Upcoming Events")

        self.UCEScroll = QScrollArea()
        self.UCEScroll.setWidget(self.UCE)
        self.UCEScroll.setMinimumHeight(125)
 
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.UCEScroll)
        self.vbox.addStretch(1)
        self.UCEGroupBox.setLayout(self.vbox)

        return self.UCEGroupBox

    #creates groupbox for events for the day
    def createDayEventObject(self):
        self.DayEventGroupBox = QGroupBox("")

        self.dayE = QLabel(self)
        self.dayE.setText("Events for the day")

        self.DayEventScroll = QScrollArea()
        self.DayEventScroll.setWidget(self.dayE)
        self.DayEventScroll.setMinimumHeight(125)
 
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.DayEventScroll)
        self.vbox.addStretch(1)
        self.DayEventGroupBox.setLayout(self.vbox)

        return self.DayEventGroupBox

    def createButtonsObject(self):
        self.LogoGroupBox = QGroupBox("")

        self.logo = QLabel(self)
        self.logo.setText("Buttons")

        self.createButton = QPushButton('Create Event', self)
        self.UpdateEventsButton = QPushButton('Update Events', self)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.createButton)
        self.vbox.addWidget(self.UpdateEventsButton)
        self.vbox.addStretch(1)
        self.LogoGroupBox.setLayout(self.vbox)

        self.createButton.clicked.connect(self.createButton_click)
        self.createButton.clicked.connect(self.UpdateEventsButton_click)

        return self.LogoGroupBox

    @pyqtSlot()
    def createButton_click(self):
        self.ECWin = CreateEventWindow(self.events)
        self.ECWin.show()

    @pyqtSlot()
    def UpdateEventsButton_click(self):
        self.createUCEList()


#class UCEObject()
    #def __init__(self, title, desc, notes, sTime, eTime, color, origin):
        #super().__init__()
        #self.Title = title
        #self.Desc = desc
        #self.Notes = notes
        #self.sTime = sTime
        #self.eTime = eTime
        #self.color = color
        #self.origin = origin