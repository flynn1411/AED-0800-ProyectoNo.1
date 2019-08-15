import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class AbrirArchivo(QDialog):
    def __init__(self):
        #Cargar la UI
        super(AbrirArchivo,self).__init__()
        loadUi('Archivo.ui', self)
   
    def obtenerString(self):
        #Guardar el string
        word = self.archivostring.toPlainText()
        self.guardadoarchivo.setText(word)
   
        


        
