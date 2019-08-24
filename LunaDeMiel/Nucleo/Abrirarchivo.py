import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class AbrirArchivo(QDialog):
    def __init__(self):
        self.word = ""
        #Cargar la UI
        super(AbrirArchivo,self).__init__()
        loadUi('Archivo.ui', self)
   
    def obtenerString(self):
        #Guardar el string
        self.word = self.archivostring.toPlainText()
          
        


        
