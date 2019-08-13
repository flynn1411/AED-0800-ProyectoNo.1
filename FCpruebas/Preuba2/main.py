import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class Life2Coding(QDialog):
    def __init__(self):
        super(Life2Coding,self).__init__()
        loadUi('life2coding.ui',self)
        self.setWindowTitle('Life2Coding PyQt5 Gui')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label.setText('Welcome:'+self.lineEdit.text())

app=QApplication(sys.argv)
widget=Life2Coding()
widget.show()
sys.exit(app.exec_())  
