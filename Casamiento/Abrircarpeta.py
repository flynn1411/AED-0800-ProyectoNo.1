import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

from Tree.tree import *

class AbrirCarpeta(QDialog):
    def __init__(self):
        #Cargar la UI
        super(AbrirCarpeta,self).__init__()
        loadUi('Carpeta.ui', self)
   
    def obtenerString(self):
        #Guardar el string
        word = self.carpetastring.toPlainText()
        self.guardado.setText(word)

        #Guardado en el arbol
        tree = Tree()
   
        tree._add(word, "D", tree.root)
        print(tree.root.value.children.first)


        
