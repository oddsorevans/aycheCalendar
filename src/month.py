import sys
import datetime
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QGridLayout, QGroupBox, QVBoxLayout, QPushButton, QCalendarWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot, QDate

class monthObject(QWidget):
    def __init__(self):
        super().__init__()

        self.currentMonth = datetime.datetime.now().month
        self.currentYear = datetime.datetime.now().year

        grid = QGridLayout()
        #month
        grid.addWidget(self.createMonthObject(), 1, 2, 1, 7)
        #upcoming events
        grid.addWidget(self.createUCEObject(), 2, 0, 6, 2)
        #events for specific day
        grid.addWidget(self.createDayEventObject(), 2, 9, 6, 2)
        #days of the month
        rows, cols = (6, 7)
        self.days = np.ndarray(shape = (rows, cols), dtype=day)
        self.cDay = day()
        grid.addWidget(self.createCelendar(), 3, 3, 6, 7)
        grid.addWidget(self.createLogoObject(), 0, 0, 2, 2)
        grid.addWidget(self.createLogoNameObject(), 0, 2, 1, 7)

        self.setMonth("April")

        self.setLayout(grid)

    def setDay(self, day):
        self.number.setText(str(day))

    def setMonth(self, month):
        self.month.setText(str(month))

    def createCelendar(self):
        self.calGroupBox = QGroupBox("")

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.calendar)
        self.vbox.addStretch(1)
        self.calGroupBox.setLayout(self.vbox)

    def createMonthObject(self):
        self.monthGroupBox = QGroupBox("")
 
        self.month = QLabel(self)
        self.month.setText("Month")

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.month)
        self.vbox.addStretch(1)
        self.monthGroupBox.setLayout(self.vbox)

        return self.monthGroupBox

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

    def createLogoObject(self):
        self.LogoGroupBox = QGroupBox("")

        self.logo = QLabel(self)
        self.logo.setText("Logo")

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.logo)
        self.vbox.addStretch(1)
        self.LogoGroupBox.setLayout(self.vbox)

        return self.LogoGroupBox

    def createLogoNameObject(self):
        self.LogoNameGroupBox = QGroupBox("")

        self.logoName = QLabel(self)
        self.logoName.setText("Ayche Calendar")

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.logoName)
        self.vbox.addStretch(1)
        self.LogoNameGroupBox.setLayout(self.vbox)

        return self.LogoNameGroupBox


class day(QWidget):
    def __init__(self):
        super().__init__()
        self.dayGroupBox = QGroupBox("")

    def createDayObject(self, day):

        self.number = QLabel(self)
        self.number.setText(str(day))
        #self.date = datetime.datetime(2020, 5, int(day) % 29)
        self.date = day
        self.dayButton = QPushButton('Show Events', self)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.number)
        self.vbox.addWidget(self.dayButton)
        self.vbox.addStretch(1)
        self.dayGroupBox.setLayout(self.vbox)

        self.dayButton.clicked.connect(self.dayButton_click)
        return self.dayGroupBox
    
    @pyqtSlot()
    def dayButton_click(self):
        print(self.date)