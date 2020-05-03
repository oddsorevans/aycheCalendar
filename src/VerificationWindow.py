import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QInputDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from mongoConnect import checkLogin

class VerificationWindow(QMainWindow):

    def __init__(self, vCorrect):
        super().__init__()
        self.title = 'Ayche Calendar'
        self.setWindowIcon(QIcon("logox64.png"))
        self.left = 10
        self.top = 10
        self.width = 100
        self.height = 100
        self.initUI()

        self.vCorrect = vCorrect
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
    
        # Create textbox
        self.vCode = QLineEdit(self)
        self.vCode.move(10, 10)
        self.vCode.resize(80,40)
        self.vCode.setPlaceholderText("Verification Code")
        
        self.vCode, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your verification code:')

        if ok:
            return self.verify_click

        # Create a button in the window
        #self.Verify = QPushButton('Verify', self)
        #self.Verify.move(20,60)
        
        # connect button to function on_click
        #self.Verify.clicked.connect(self.verify_click)
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    @pyqtSlot()
    def verify_click(self):
        vCodeValue = int(self.vCode.text())
        if vCodeValue == self.vCorrect:
            self.hide()
            return True
        else:
            QMessageBox.question(self, '', "Incorrect Verification Code. Please Try Again.", QMessageBox.Ok, QMessageBox.Ok)
            self.hide()
            return False