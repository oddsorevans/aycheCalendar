import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSlot

class SignUpWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Ayche Calendar Sign Up'
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 540
        self.initUI()
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
    
        # Create textbox
        self.username = QLineEdit(self)
        self.username.move(20, 20)
        self.username.resize(280,40)

        # Create textbox
        self.password = QLineEdit(self)
        self.password.move(20, 80)
        self.password.resize(280,40)
        
        # Create a button in the window
        self.Submit = QPushButton('Submit', self)
        self.Submit.move(90,140)
        
        # connect button to function on_click
        self.Submit.clicked.connect(self.submit_click)
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    @pyqtSlot()
    def submit_click(self):
        
        usernameValue = self.username.text()
        passwordValue = self.password.text()

        if usernameValue == "Daycee":
            if passwordValue == "Password":
                QMessageBox.question(self, 'Message - pythonspot.com', "Login successful!", QMessageBox.Ok, QMessageBox.Ok)
                self.username.setText("")
                self.password.setText("")
                self.close()
            else:
                QMessageBox.question(self, 'Message - pythonspot.com', "Invaid password. Try again.", QMessageBox.Ok, QMessageBox.Ok)
                self.password.setText("")
        else: 
            QMessageBox.question(self, 'Message - pythonspot.com', "That user is not registered, please signup", QMessageBox.Ok, QMessageBox.Ok)
            self.username.setText("")
            self.password.setText("")