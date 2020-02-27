import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSlot
from LoginWindow import LoginWindow

app = QApplication(sys.argv)

window = LoginWindow()
window.show()

app.exec_()