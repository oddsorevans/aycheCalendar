import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QGridLayout, QGroupBox, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from day import dayObject

class monthObject(QWidget):
    def __init__(self):
        super().__init__()

        groupObject = dayObject()
        createDay = groupObject.createGroup()

        grid = QGridLayout()
        grid.addWidget(createDay(), 0, 0)
        grid.addWidget(createDay(), 1, 0)
        grid.addWidget(createDay(), 0, 1)
        grid.addWidget(createDay(), 1, 1)
        #grid.addWidget(self.createDayObject(), 0, 0)
        #grid.addWidget(self.createDayObject(), 1, 0)
        #grid.addWidget(self.createDayObject(), 0, 1)
        #grid.addWidget(self.createDayObject(), 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("PyQt5 Group Box")
        self.resize(400, 300)

    def createDayObject(self):
        groupBox = QGroupBox("Best Food")

        number = QLabel(self)
        number.setText("dsafjkfdsa")

        vbox = QVBoxLayout()
        vbox.addWidget(number)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox