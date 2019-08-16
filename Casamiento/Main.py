import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from Tree.tree import *

class MainPage(QDialog):
    def __init__(self):
        #Cargar la UI
        super(MainPage, self).__init__()
        loadUi('Principal.ui', self)
        
        
        self.arbol = Tree()

        
        self.josue = ["Hola" , "Mundo"]
        self.Lista.addItems(self.josue)   
        #Accion 
        self.carpeta.clicked.connect(self.abrirC)
        self.archivo.clicked.connect(self.abrirA)
        self.o.clicked.connect(self.mostrar)
        

    def mostrar(self):
             
        #str(self.arbol.root.value.children.first.value.name) 
        self.josue = ["Funciono"]
        self.Lista.addItems(self.josue)   
        
         
    def abrirC(self):
        #Importar
        from Abrircarpeta import AbrirCarpeta
        a = AbrirCarpeta()

        #Accion 
        prueba = a.CCarpeta.clicked.connect(a.obtenerString)
        
        
        #Finalizar sin cerrar  
        a.exec_()

        self.arbol._add(prueba, "D", self.arbol.root)
        print(prueba)
        print(self.arbol.root.value.children.first.value.name)

    def abrirA(self):
        #Importar
        from Abrirarchivo import AbrirArchivo
        b = AbrirArchivo()

        #Accion 
        b.CArchivo.clicked.connect(b.obtenerString)  

        #Finalizar sin cerrar  
        b.exec_()
  
       
        

    
app=QApplication(sys.argv)
widget=MainPage()
widget.show()
sys.exit(app.exec_())  
