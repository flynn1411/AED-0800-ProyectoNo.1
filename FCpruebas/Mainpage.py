import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('Pruebas/Homepage.ui', self)
        self.pushButton_2.clicked.connect(self.retrieveText)
    
    def retrieveText(self):
        words = self.plainTextEdit.toPlainText()
        self.textEdit_2.setText(words)
        

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
