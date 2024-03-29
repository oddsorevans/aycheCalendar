import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QGridLayout, QGroupBox, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from SignUpWindow import SignUpWindow
from CalendarWindow import CalendarWindow
from mongoConnect import checkLogin

class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Ayche Calendar'
        self.setWindowIcon(QIcon("logox64.png"))
        self.setStyleSheet("background-color:rgb(47,72,88)")
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 540
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.center()

        self.logoLabel = QLabel(self)
        self.logoPixmap = QPixmap('logox676.png')
        self.pixmap_resized = self.logoPixmap.scaled(230, 230, Qt.KeepAspectRatio)
        self.logoLabel.setPixmap(self.pixmap_resized)
        self.logoLabel.move(365, 20)
        self.logoLabel.resize(230, 230)

        # Create textbox
        self.username = QLineEdit(self)
        self.username.move(330, 270)
        self.username.resize(300, 40)
        self.username.setStyleSheet("background-color:rgb(251,235,219)")
        self.username.setPlaceholderText("Username")

        # Create textbox
        self.password = QLineEdit(self)
        self.password.move(330, 330)
        self.password.resize(300, 40)
        self.password.setStyleSheet("background-color:rgb(251,235,219)")
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        
        # Create a button in the window
        self.LoginButton = QPushButton('Login', self)
        self.LoginButton.setStyleSheet("background-color:rgb(251,235,219)")
        self.LoginButton.move(435, 390)

        # Create a button in the window
        self.SignupButton = QPushButton('Sign Up', self)
        self.SignupButton.setStyleSheet("background-color:rgb(251,235,219)")
        self.SignupButton.move(435, 440)
        
        # connect button to function on_click
        self.LoginButton.clicked.connect(self.login_click)
        self.SignupButton.clicked.connect(self.signup_click)
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    @pyqtSlot()
    def login_click(self):
        usernameValue = self.username.text()
        passwordValue = self.password.text()
        #check and see if user is in the database
        if checkLogin(usernameValue, passwordValue) is True:
            QMessageBox.question(self, '', "Login successful!", QMessageBox.Ok, QMessageBox.Ok)
            self.w = CalendarWindow(usernameValue)
            self.w.show()
            self.hide()
        else:
            QMessageBox.question(self, '', "Username or Password was Incorrect", QMessageBox.Ok, QMessageBox.Ok)
            self.username.setText("")
            self.password.setText("")

    def signup_click(self):
        self.w = SignUpWindow()
        self.w.show()
        self.hide()