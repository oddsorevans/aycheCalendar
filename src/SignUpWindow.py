import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSlot

class SignUpWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Ayche Calendar Sign Up'
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 960
        self.initUI()
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()

        # First_Name
        self.First_Name = QLineEdit(self)
        self.First_Name.move(20, 20)
        self.First_Name.resize(300,40)
        self.First_Name.setPlaceholderText("First Name")

        # Last_Name
        self.Last_Name = QLineEdit(self)
        self.Last_Name.move(20, 80)
        self.Last_Name.resize(300,40)
        self.Last_Name.setPlaceholderText("Last Name")

        # Email
        self.Email = QLineEdit(self)
        self.Email.move(20, 140)
        self.Email.resize(300,40)
        self.Email.setPlaceholderText("Email")

        # dob_label
        self.dob_label = QLabel(self)
        self.dob_label.move(20, 200)
        self.dob_label.resize(60,40)
        self.dob_label.setText("DOB")

        # dob_year
        self.dob_year = QLineEdit(self)
        self.dob_year.move(100, 200)
        self.dob_year.resize(60,40)
        self.dob_year.setPlaceholderText("YYYY")

        # dob_month
        self.dob_month = QLineEdit(self)
        self.dob_month.move(180, 200)
        self.dob_month.resize(60,40)
        self.dob_month.setPlaceholderText("MM")

        # dob_day
        self.dob_day = QLineEdit(self)
        self.dob_day.move(260, 200)
        self.dob_day.resize(60,40)
        self.dob_day.setPlaceholderText("DD")

        # Username
        self.username = QLineEdit(self)
        self.username.move(20, 260)
        self.username.resize(300,40)
        self.username.setPlaceholderText("Username")

        # Password
        self.password = QLineEdit(self)
        self.password.move(20, 320)
        self.password.resize(300,40)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        # Confirm_Password
        self.Confirm_Password = QLineEdit(self)
        self.Confirm_Password.move(20, 380)
        self.Confirm_Password.resize(300,40)
        self.Confirm_Password.setPlaceholderText("Confirm Password")
        self.Confirm_Password.setEchoMode(QLineEdit.Password)
        
        # Create a button in the window
        self.Submit = QPushButton('Submit', self)
        self.Submit.move(90,440)
        
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
        
        # usernameValue = self.username.text()
        # passwordValue = self.password.text()

        # if usernameValue == "Daycee":
        #     if passwordValue == "Password":
        #         QMessageBox.question(self, 'Message - pythonspot.com', "Login successful!", QMessageBox.Ok, QMessageBox.Ok)
        #         self.username.setText("")
        #         self.password.setText("")
        #         self.close()
        #     else:
        #         QMessageBox.question(self, 'Message - pythonspot.com', "Invaid password. Try again.", QMessageBox.Ok, QMessageBox.Ok)
        #         self.password.setText("")
        # else: 
        #     QMessageBox.question(self, 'Message - pythonspot.com', "That user is not registered, please signup", QMessageBox.Ok, QMessageBox.Ok)
        #     self.username.setText("")
        #     self.password.setText("")

        QMessageBox.question(self, 'Message - pythonspot.com', "Congrats " + self.First_Name.text() + " you have signed up!", QMessageBox.Ok)