import sys
import datetime
import eventHandler
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QDateTimeEdit, QVBoxLayout, QColorDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot, QDate, QDateTime
from mongoConnect import checkLogin

class CreateEventWindow(QMainWindow):

    def __init__(self, events):
        super().__init__()
        self.events = events
        self.title = 'Ayche Calendar'
        self.setWindowIcon(QIcon("logox64.png"))
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 500
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()

        self.Event_Title = QLineEdit(self)
        self.Event_Title.move(0, 0)
        self.Event_Title.resize(300,40)
        #self.Event_Title.setStyleSheet("background-color:rgb(251,235,219)")
        self.Event_Title.setPlaceholderText("Event Title")

        self.Event_Desc = QLineEdit(self)
        self.Event_Desc.move(0, 60)
        self.Event_Desc.resize(300,40)
        #self.Event_Desc.setStyleSheet("background-color:rgb(251,235,219)")
        self.Event_Desc.setPlaceholderText("Description")

        self.Event_Notes = QLineEdit(self)
        self.Event_Notes.move(0, 120)
        self.Event_Notes.resize(300,40)
        #self.Event_Notes.setStyleSheet("background-color:rgb(251,235,219)")
        self.Event_Notes.setPlaceholderText("Notes")

        self.ColorButton = QPushButton('Open color dialog', self)
        self.ColorButton.setToolTip('Opens color dialog')
        self.ColorButton.move(0,300)
        self.ColorButton.clicked.connect(self.on_click)

        self.Submit = QPushButton('Submit', self)
        #self.Submit.setStyleSheet("background-color:rgb(251,235,219)")
        self.Submit.move(0,440)

        self.StartTime = QDateTimeEdit(QDate.currentDate())
        self.StartTime.setMinimumDate(QDate.currentDate().addDays(-365))
        self.StartTime.setMaximumDate(QDate.currentDate().addDays(365))
        self.StartTime.setDisplayFormat("MM/dd/yyyy hh:mm")
        self.StartTime.move(0, 40)
        self.StartTime.show()

        self.EndTime = QDateTimeEdit(QDate.currentDate())
        self.EndTime.setMinimumDate(QDate.currentDate().addDays(-365))
        self.EndTime.setMaximumDate(QDate.currentDate().addDays(365))
        self.EndTime.setDisplayFormat("MM/dd/yyyy hh:mm")
        self.EndTime.move(0, 100)
        self.EndTime.show()

        #self.form_widget = FormWidget(self)
        #self.setCentralWidget(self.form_widget)

        self.Submit.clicked.connect(self.submit_click)
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    @pyqtSlot()
    def submit_click(self):
        format = "%m/%d/%Y %H:%M"
        self.events.createEvent(datetime.datetime.strptime(self.StartTime.text(), format), self.Event_Title.text(), self.Event_Desc.text(), self.rgb, self.Event_Notes.text(), datetime.datetime.strptime(self.EndTime.text(), format))
        self.close()
        
    @pyqtSlot()
    def on_click(self):
        self.color = QColorDialog.getColor()
        h = self.color.name().lstrip('#')
        self.rgb = list(int(h[i:i+2], 16) for i in (0,2,4))
    
class FormWidget(QWidget):
    def __init__(self, parent):        
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.StartTime = QDateTimeEdit(QDate.currentDate())
        self.StartTime.setMinimumDate(QDate.currentDate().addDays(-365))
        self.StartTime.setMaximumDate(QDate.currentDate().addDays(365))
        self.StartTime.setDisplayFormat("MM/dd/yyyy hh:mm")

        self.EndTime = QDateTimeEdit(QDate.currentDate())
        self.EndTime.setMinimumDate(QDate.currentDate().addDays(-365))
        self.EndTime.setMaximumDate(QDate.currentDate().addDays(365))
        self.EndTime.setDisplayFormat("MM/dd/yyyy hh:mm")

        self.layout.addWidget(self.StartTime)
        self.layout.addWidget(self.EndTime)

        self.setLayout(self.layout)