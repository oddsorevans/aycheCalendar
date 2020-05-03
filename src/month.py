import sys
import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QGridLayout, QGroupBox, QVBoxLayout, QPushButton, QCalendarWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot, QDate
from CreateEventWindow import CreateEventWindow

class monthObject(QWidget):
    def __init__(self):
        super().__init__()

        self.currentMonth = datetime.datetime.now().month
        self.currentYear = datetime.datetime.now().year

        grid = QGridLayout()
        #upcoming events
        grid.addWidget(self.createUCEObject(), 0, 0, 3, 3)
        #events for specific day
        grid.addWidget(self.createDayEventObject(), 0, 4, 3, 3)
        #creates calendar
        grid.addWidget(self.createCelendar(), 3, 0, 6, 7)
        #creates button groupbox
        grid.addWidget(self.createButtonsObject(), 0, 3, 3, 1)

        self.setLayout(grid)

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
    def createUCEObject(self):
        self.UCEGroupBox = QGroupBox("")

        self.UCE = QLabel(self)
        self.UCE.setText("Upcoming Events")
 
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.UCE)
        self.vbox.addStretch(1)
        self.UCEGroupBox.setLayout(self.vbox)

        return self.UCEGroupBox

    #creates groupbox for events for the day
    def createDayEventObject(self):
        self.DayEventGroupBox = QGroupBox("")

        self.dayE = QLabel(self)
        self.dayE.setText("Events for the day")
 
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.dayE)
        self.vbox.addStretch(1)
        self.DayEventGroupBox.setLayout(self.vbox)

        return self.DayEventGroupBox

    def createButtonsObject(self):
        self.LogoGroupBox = QGroupBox("")

        self.logo = QLabel(self)
        self.logo.setText("Buttons")

        self.createButton = QPushButton('Create Event', self)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.createButton)
        self.vbox.addStretch(1)
        self.LogoGroupBox.setLayout(self.vbox)

        self.createButton.clicked.connect(self.createButton_click)

        return self.LogoGroupBox

    @pyqtSlot()
    def createButton_click(self):
        CreateEventWindow()