import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5.uic import loadUi
from Tree.tree import *

class MainPage(QDialog):
    def __init__(self):
        #Cargar la UI
        super(MainPage, self).__init__()
        loadUi('Principal.ui', self)
        
        
        self.arbol = Tree()

        self.arbol._add("hola", "F", self.arbol.root)
        self.arbol._add("e", "D", self.arbol.root)
        self.arbol._add("a.txt", "F", self.arbol.root.value.children.first)
        self.arbol._add("log", "D", self.arbol.root)
        self.arbol._add("xdxd", "F", self.arbol.root.value.children.first)
        self.arbol._add("archivo", "D", self.arbol.root.value.children.first)
        self.arbol._add("archivo2", "D", self.arbol.root.value.children.first.value.children.first.next)
        self.arbol._add("Prueba", "F", self.arbol.root.value.children.first.value.children.first.next.value.children.first)
        self.arbol._add("Hola", "F", self.arbol.root.value.children.first.next.next)

        self.array = []
        #hola , e , log.
        #a.txt archivo xdxd
        current = self.arbol.root.value.children.first

        while(current.next):

            self.array.append(current.value.name)
            current = current.next
            
        self.array.append(current.value.name)






        self.Lista.addItems(self.array)   
        #Accion 
        self.carpeta.clicked.connect(self.abrirC)
        self.archivo.clicked.connect(self.abrirA)
        self.o.clicked.connect(self.mostrar)
        #self.borrar.clicked.connect(self.borrar)
        self.Lista.itemDoubleClicked.connect(self.navegar)
        


















    def navegar(self):
        
        valor = self.Lista.selectedItems()[0].text()
        print(valor)

        encontrado = self.arbol._search(valor,self.arbol.root)
        print(encontrado)
                
        self.Lista.clear()

        #current = self.arbol.root.value.children.first

        array2 = []
        temporal = encontrado.value.children.first
        print(temporal.value.name)
        while(temporal.next):

            array2.append(temporal.value.name)
            temporal = temporal.next
            
        array2.append(temporal.value.name)

        self.Lista.addItems(array2)   
        















        
    def mostrar(self):
             
        #str(self.arbol.root.value.children.first.value.name) 
        self.root = ["Funciono", self.arbol.root.value.children.first.value.name]
        self.Lista.addItems(self.array)   
        
         


    def abrirC(self):
        #Importar
        from Abrircarpeta import AbrirCarpeta
        a = AbrirCarpeta()

        #Accion 
        a.CCarpeta.clicked.connect(a.obtenerString)
               
        #Finalizar sin cerrar  
        a.exec_()

        nodoC = self.arbol.root
        self.arbol._add(a.word, "D", nodoC)
        print(a.word)
        print(self.arbol.root.value.children.first.value.name)





    def abrirA(self):
        #Importar
        from Abrirarchivo import AbrirArchivo
        b = AbrirArchivo()

        #Accion 
        b.CArchivo.clicked.connect(b.obtenerString)

        #Finalizar sin cerrar  
        b.exec_()

        nodoA = self.arbol.root
        self.arbol._add(b.word, "F", nodoActual)
        print(b.word)
        print(self.arbol.root.value.children.first.value.name)





    def borrar(self):
        pass

        """ valor = self.Lista.selectedItems()[0].text() """


        
        
  
       
        

    
app=QApplication(sys.argv)
widget=MainPage()
widget.show()
sys.exit(app.exec_())  
