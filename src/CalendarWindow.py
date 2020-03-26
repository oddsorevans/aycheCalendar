import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, pyqtSlot

class CalendarWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Ayche Calendar'
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 540
        self.initUI()
        
        self.textFont = QFont()
        self.textFont.setPointSize(60)
        
        # Create Label
        self.welcomeText = QLabel(self)
        self.welcomeText.move(240, 0)
        self.welcomeText.resize(480, 540)
        self.welcomeText.setFont(self.textFont)
        self.welcomeText.setText("Welcome")
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())