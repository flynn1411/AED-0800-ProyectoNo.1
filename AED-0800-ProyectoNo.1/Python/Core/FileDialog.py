import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class FileDialog(QDialog):
    def __init__(self):
        self.word = ""
        #Cargar la UI
        super(FileDialog,self).__init__()
        loadUi('Core/AddFile.ui', self)
   
    def getString(self):
        #Guardar el string
        self.word = self.FileName.toPlainText()
          
        


        
