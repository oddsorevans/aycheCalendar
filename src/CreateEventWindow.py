import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QInputDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from mongoConnect import checkLogin

class CreateEventWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Ayche Calendar'
        self.setWindowIcon(QIcon("logox64.png"))
        self.left = 10
        self.top = 10
        self.width = 100
        self.height = 100
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
    
        # Create textbox
        self.eTitle = QLineEdit(self)
        self.eTitle.move(50, 10)
        self.eTitle.resize(80,40)
        self.eTitle.setPlaceholderText("Event Title")

        self.eDesc = QLineEdit(self)
        self.eDesc.move(10, 10)
        self.eDesc.resize(80,40)
        self.eDesc.setPlaceholderText("Event Title")

        self.eTitle, ok = QInputDialog.getText(self, 'Create Event', '')

        if ok:
            return self.createEvent_click
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    @pyqtSlot()
    def createEvent_click(self):
        print('Event Created')