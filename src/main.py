import sys
from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget, QLabel, QMenu
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from LoginWindow import LoginWindow

app = QApplication(sys.argv)

trayIcon = QSystemTrayIcon(QIcon("logox64.png"), parent = app)
trayIcon.setToolTip("Ayche Calendar")
trayIcon.show()

menu = QMenu()
exitAction = menu.addAction('Exit')
exitAction.triggered.connect(app.quit)

trayIcon.setContextMenu(menu)

window = LoginWindow()
window.show()

app.exec_()