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

       
        self.padres = [self.arbol.root,]
        """ self.padre = self.arbol.root
        self.padres.append(self.padre) """

        self.mostrarLista(self.arbol.root.value.children.first)

        """ self.array = []
        #hola , e , log.
        #a.txt archivo xdxd
        current = self.arbol.root.value.children.first

        while(current.next):

            self.array.append(current.value.name)
            current = current.next
            
        self.array.append(current.value.name)

        self.Lista.addItems(self.array) """   







        #Accion 
        self.carpeta.clicked.connect(self.abrirC)
        self.archivo.clicked.connect(self.abrirA)
        self.o.clicked.connect(self.back)
        #self.borrar.clicked.connect(self.borrar)
        self.Lista.itemDoubleClicked.connect(self.navegar)
        







        
    def mostrarLista(self,current):
        
        
        self.array = []
        while(current.next):

            self.array.append(current.value.name)
            current = current.next
            
        self.array.append(current.value.name)

        #Mostrar la lista 
        self.Lista.addItems(self.array) 







    def navegar(self):
        
        
        #Encontrar el nodo 
        valor = self.Lista.selectedItems()[0].text()       
        encontrado = self.arbol._search(valor,self.padres[len(self.padres)-1])

        #Guardar el padre 
        self.padres.append(encontrado)
        
        #Limpar la lista                
        self.Lista.clear()

        #Mostrar los hijos del nodo
        
        temporal = encontrado.value.children.first
        
        self.mostrarLista(temporal)
        
        """ array2 = []
        while(temporal.next):

            array2.append(temporal.value.name)
            temporal = temporal.next
            
        array2.append(temporal.value.name)

        self.Lista.addItems(array2)    """
        















        
    def back(self):
    
        self.padres.pop(len(self.padres)-1)
        regresar = self.padres[len(self.padres)-1]

        dad = regresar.value.children.first

        self.mostrarLista(dad)   
         
        """ array3 = []
        while(regresar.next):

            array3.append(regresar.value.name)
            regresar = regresar.next
            
        array3.append(regresar.value.name)

        self.Lista.addItems(array3)    """
        
        








             


    def abrirC(self):
        #Importar
        from Abrircarpeta import AbrirCarpeta
        a = AbrirCarpeta()

        #Accion 
        a.CCarpeta.clicked.connect(a.obtenerString)
               
        #Finalizar sin cerrar  
        a.exec_()

        #Agregar archivo al arbol
        self.arbol._add(a.word, "D", self.padres[len(self.padres)-1])
        
        """ #Mostrar el arbol
        self.Lista.clear()
        self.mostrarLista(self.padres[len(self.padres)-1])
        """
        """ print(a.word)
        print(self.arbol.root.value.children.first.value.name) """





    def abrirA(self):
        #Importar
        from Abrirarchivo import AbrirArchivo
        b = AbrirArchivo()

        #Accion 
        b.CArchivo.clicked.connect(b.obtenerString)

        #Finalizar sin cerrar  
        b.exec_()

        #Agregar file al arbol
        self.arbol._add(b.word, "F", self.padres[len(self.padres)-1])

        """ #Mostrar el arbol
        self.Lista.clear()
        self.mostrarLista(self.padres[len(self.padres)-1])
        """

        """ print(b.word)
        print(self.arbol.root.value.children.first.value.name) """





    def borrar(self):
        pass

        """ aBorrar = self.Lista.selectedItems()[0].text()
        self.arbol._delet(aBorrar,self.padres[len(self.padres)-1]) """
        
        


        
        
  
       
        

    
app=QApplication(sys.argv)
widget=MainPage()
widget.show()
sys.exit(app.exec_())  
