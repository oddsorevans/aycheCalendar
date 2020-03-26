import sys
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from CalendarWindow import CalendarWindow
from mongoConnect import addUser
from mongoConnect import checkEmailUser

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

        # First_Name
        self.First_Name = QLineEdit(self)
        self.First_Name.move(330, 20)
        self.First_Name.resize(300,40)
        self.First_Name.setPlaceholderText("First Name")

        # Last_Name
        self.Last_Name = QLineEdit(self)
        self.Last_Name.move(330, 80)
        self.Last_Name.resize(300,40)
        self.Last_Name.setPlaceholderText("Last Name")

        # Email
        self.Email = QLineEdit(self)
        self.Email.move(330, 140)
        self.Email.resize(300,40)
        self.Email.setPlaceholderText("Email")

        # dob_label
        self.dob_label = QLabel(self)
        self.dob_label.move(330, 200)
        self.dob_label.resize(60,40)
        self.dob_label.setText("DOB")

        # dob_year
        self.dob_year = QLineEdit(self)
        self.dob_year.move(410, 200)
        self.dob_year.resize(60,40)
        self.dob_year.setPlaceholderText("YYYY")

        # dob_month
        self.dob_month = QLineEdit(self)
        self.dob_month.move(490, 200)
        self.dob_month.resize(60,40)
        self.dob_month.setPlaceholderText("MM")

        # dob_day
        self.dob_day = QLineEdit(self)
        self.dob_day.move(570, 200)
        self.dob_day.resize(60,40)
        self.dob_day.setPlaceholderText("DD")

        # Username
        self.username = QLineEdit(self)
        self.username.move(330, 260)
        self.username.resize(300,40)
        self.username.setPlaceholderText("Username")

        # Password
        self.password = QLineEdit(self)
        self.password.move(330, 320)
        self.password.resize(300,40)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        # Confirm_Password
        self.Confirm_Password = QLineEdit(self)
        self.Confirm_Password.move(330, 380)
        self.Confirm_Password.resize(300,40)
        self.Confirm_Password.setPlaceholderText("Confirm Password")
        self.Confirm_Password.setEchoMode(QLineEdit.Password)
        
        # Create a button in the window
        self.Submit = QPushButton('Submit', self)
        self.Submit.move(435,440)
        
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
        #set variables to make the add user cleaner
        fn = self.First_Name.text()
        ln = self.Last_Name.text()
        email = self.Email.text()
        #set bd from string to datetime
        bd = datetime(int(self.dob_year.text()), int(self.dob_month.text()), int(self.dob_day.text()), 0, 0, 0)
        username = self.username.text()
        password = self.password.text()

        if self.Confirm_Password != self.password:
            QMessageBox.question(self, '', "Password and confirm password do not match", QMessageBox.Ok, QMessageBox.Ok)
        #Have to check if it exists before adding to avoid duplicate accounts
        elif checkEmailUser(username, email) is True:
            QMessageBox.question(self, '', "Username or Email already exists", QMessageBox.Ok, QMessageBox.Ok)
            self.username.setText("")
            self.Email.setText("")
        #add user
        else:
            addUser(fn, ln, email, bd, username, password)

            QMessageBox.question(self, '', 'Account Created!', QMessageBox.Ok, QMessageBox.Ok)
            self.w = CalendarWindow()
            self.w.show()
            self.hide()