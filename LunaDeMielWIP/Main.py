import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QListWidgetItem
from PyQt5.uic import loadUi
from Nucleo.tree import *
from Nucleo.memory import *

class MainPage(QDialog):
    def __init__(self):
        
        #Cargar la interfaz
        super(MainPage, self).__init__()
        loadUi('Nucleo/Principal.ui', self)
        
        #Cargar el arbol
        self.memoryHandler = MemoryHandler()
        self.arbol = self.memoryHandler.tree
        
        file = open("Memory/arbolA.mem","r")
        content = file.read()
        file.close()
        self.memoryHandler.loadTree(content)

       
        #Seguimiento de los padres
        self.padres = [self.arbol.root]
       
        
        #inicializar el programa 
        self.mostrarLista(self.arbol.root.value.children.first)
        


        #Acciones del programa
        self.carpeta.clicked.connect(self.abrirC)
        self.archivo.clicked.connect(self.abrirA)
        self.Lista.itemDoubleClicked.connect(self.navegar)
            #self.borrar.clicked.connect(self.borrar)

    
    
    
    
    #Todasl las funciones de la interfaz
    def guardado(self,cadena):
        
        file = open("Memory/arbolA.mem","w")
        file.write(cadena)
        file.close()
        
      
    def mostrarLista(self,current):
        """itm = QListWidgetItem(cadena);
        itm.setIcon(QIcon(r"icono.png"));"""

        array =["."]
        filaCarpetas = LinkedList()
        filaArchivos = LinkedList()

        #Comprobar si esta vacio
        if(current):
            if(not current.value.name == self.arbol.root.value.children.first.value.name):
                array.append("..")
                self.Lista.addItems(array)
                
            while(current):
                item = QListWidgetItem(current.value.name)
                if(isinstance(current.value, Directory)):
                    item.setIcon(QIcon(r"Nucleo/Iconos/folder.png"))
                    print(item.icon())
                    filaCarpetas.push(Node(item))
                
                else:
                    item.setIcon(QIcon(r"Nucleo/Iconos/file.png"))
                    filaArchivos.push(Node(item))

                #self.Lista.addItem(item)
                #array.append(current.value.name)
                current = current.next
                    
            #array.append(current.value.name)
            currentCarpeta = filaCarpetas.pop()
            while(currentCarpeta):
                self.Lista.addItem(currentCarpeta.value)
                currentCarpeta = filaCarpetas.pop()

            currentArchivo = filaArchivos.pop()
            while(currentArchivo):
                self.Lista.addItem(currentArchivo.value)
                currentArchivo = filaArchivos.pop()
        
        else:
            array.append("..")
            self.Lista.addItems(array)
        
        
        #Mostrar la lista        
        #self.Lista.addItems(array) 
        
              
        

    def navegar(self):
        
        valor = self.Lista.selectedItems()[0].text()     
        self.Lista.clear()
        if(valor == ".."):
            self.back()

        else:
            
            #Encontrar el nodo       
            encontrado = self.arbol._search(valor,self.padres[len(self.padres)-1])

            if(encontrado and isinstance(encontrado.value , Directory)):
                      
                #Guardar el padre 
                self.padres.append(encontrado)
 
                #Mostrar los hijos del nodo
                temporal = encontrado.value.children.first
                self.mostrarLista(temporal)

            else:
                self.mostrarLista(self.padres[len(self.padres)-1].value.children.first)

       
        
    def back(self):

        self.Lista.clear()
        
        if(len(self.padres) > 1):
           
            self.padres.pop(len(self.padres)-1)
            regresar = self.padres[len(self.padres)-1]
            dad = regresar.value.children.first
            self.mostrarLista(dad)
        
        else:
            self.mostrarLista(self.arbol.root.value.children.first)   
       

             


    def abrirC(self):
        #Importar
        from Nucleo.Abrircarpeta import AbrirCarpeta
        a = AbrirCarpeta()

        #Accion 
        a.CCarpeta.clicked.connect(a.obtenerString)
               
        #Finalizar sin cerrar  
        a.exec_()

        #Agregar archivo al arbol
        self.arbol._add(a.word, "D", self.padres[len(self.padres)-1])
        cadena = self.memoryHandler.saveTree(self.arbol.root.value.children.first)
        self.guardado(cadena)
        
        
        #Mostrar el arbol
        self.Lista.clear()

        #Mostrar hijos
        if(len(self.padres) > 1):
            self.mostrarLista(self.padres[len(self.padres)-1].value.children.first)
            print(self.padres[len(self.padres)-1])

        else:
            self.mostrarLista(self.arbol.root.value.children.first)
        




    def abrirA(self):
        #Importar
        from Nucleo.Abrirarchivo import AbrirArchivo
        b = AbrirArchivo()

        #Accion 
        b.CArchivo.clicked.connect(b.obtenerString)

        #Finalizar sin cerrar  
        b.exec_()

        #Agregar file al arbol
        self.arbol._add(b.word, "F", self.padres[len(self.padres)-1])
        cadena = self.memoryHandler.saveTree(self.arbol.root.value.children.first)
        self.guardado(cadena)

        #Mostrar hijos
        self.Lista.clear()
        if(len(self.padres) > 1):
            self.mostrarLista(self.padres[len(self.padres)-1].value.children.first)
            print(self.padres[len(self.padres)-1])

        else:
            self.mostrarLista(self.arbol.root.value.children.first)




    def borrar(self):
        pass

        """ aBorrar = self.Lista.selectedItems()[0].text()
        self.arbol._delet(aBorrar,self.padres[len(self.padres)-1]) """
        
        

    
app=QApplication(sys.argv)
widget=MainPage()
widget.show()
sys.exit(app.exec_())  
