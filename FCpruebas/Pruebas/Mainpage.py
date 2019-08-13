import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('Homepage.ui', self)
        
        self.pushButton_2.clicked.connect(self.retrieveText)
        self.pushButton_3.clicked.connect(self.move)
    
    def retrieveText(self):
        #Obteniendo el string
        words = self.plainTextEdit.toPlainText()
        words2 = "Hello " + words
        self.textEdit_2.setText(words2)
    
    def move(self):
        from Otherpage import SecondPage
        theclass = SecondPage()
        theclass.exec_()
        
        

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
