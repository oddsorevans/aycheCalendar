import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, pyqtSlot
from month import monthObject

class CalendarWindow(QMainWindow):

    def __init__(self, uname):
        super().__init__()
        self.title = 'Ayche Calendar - Welcome '
        self.setWindowIcon(QIcon("logox64.png"))
        self.setStyleSheet("background-color:rgb(251,235,219)")
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 540
        self.username = uname
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title + self.username + '!')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.center()

        #creates calendar view
        self.date = monthObject(self.username)
        self.setCentralWidget(self.date)
        self.date.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())