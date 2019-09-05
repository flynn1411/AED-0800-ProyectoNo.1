import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi


class DirectoryDialog(QDialog):
    def __init__(self):
        self.word = ""
        #Cargar la UI
        super(DirectoryDialog,self).__init__()
        loadUi('Core/AddFolder.ui', self)
   
    def getString(self):
        #Guardar el string
        self.word = self.FolderName.toPlainText()
        
       
        

        
