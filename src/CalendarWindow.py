import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, pyqtSlot
from month import monthObject

class CalendarWindow(QMainWindow):

    def __init__(self, uname):
        super().__init__()
        self.title = 'Ayche Calendar - Welcome '
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 540
        self.username = uname
        self.initUI()
        
        #self.textFont = QFont()
        #self.textFont.setPointSize(48)

        # Create Label
        #self.welcomeText = QLabel(self)
        #self.welcomeText.move(180, 0)
        #self.welcomeText.resize(800, 440)
        #self.welcomeText.setFont(self.textFont)
        #self.welcomeText.setText("Welcome " + self.username)

        #self.toText = QLabel(self)
        #self.toText.move(240, 100)
        #self.toText.resize(520, 440)
        #self.toText.setFont(self.textFont)
        #self.toText.setText("to AycheCalendar")
        
    
    def initUI(self):
        self.setWindowTitle(self.title + self.username + '!')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.center()

        #creates calendar view
        self.date = monthObject()
        self.setCentralWidget(self.date)
        self.date.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())