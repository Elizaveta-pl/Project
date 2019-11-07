import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

from PyQt5.QtWidgets import QLCDNumber, QLineEdit






if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    ex.show()

    sys.exit(app.exec())