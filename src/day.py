#day object
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QGroupBox, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot

class dayObject(QWidget):
    def __init__(self):
        super().__init__()

        #self.container = QGroupBox("Date Group")
        #self.number = QLabel(self)
        #self.number.setText("#")
        #self.vbox = QVBoxLayout()
        #self.vbox.addWidget(self.number)
        #self.container.setLayout(self.vbox)

    def createGroup(self):
        self.container = QGroupBox("Date Group")

        self.number = QLabel(self)
        self.number.setText("dsafjkfdsa")

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.number)
        self.vbox.addStretch(1)
        self.container.setLayout(self.vbox)
        return self.container
        