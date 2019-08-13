import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class SecondPage(QDialog):
    def __init__(self):
        super(SecondPage, self).__init__()
        loadUi('Secondpage.ui', self)
        