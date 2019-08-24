import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

#from Tree.tree import *

class AbrirCarpeta(QDialog):
    def __init__(self):
        self.word = ""
        #Cargar la UI
        super(AbrirCarpeta,self).__init__()
        loadUi('Nucleo/Carpeta.ui', self)
   
    def obtenerString(self):
        #Guardar el string
        self.word = self.carpetastring.toPlainText()
        
       
        

        
