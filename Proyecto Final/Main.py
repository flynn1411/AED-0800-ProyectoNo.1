# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QDialog,QMessageaFileox,QListWidgetItem
from PyQt5.uic import loadUi
from Core.tree import *
from Core.memory import *

class MainPage(QDialog):
    def __init__(self):

        #Cargar la interfaz
        super(MainPage, self).__init__()
        loadUi('Core/MainInterface.ui', self)

        #Cargar el arbol A

        self.memoryHandler = MemoryHandler()
        self.treeA = self.memoryHandler.tree
        file = open("Memory/TreeA.mem","r")
        content = file.read()
        file.close()
        self.memoryHandler.loadTree(content)

        #Cargar el arbol B

        self.memoryHandler = MemoryHandler()
        self.treeB = self.memoryHandler.tree
        file = open("Memory/TreeB.mem","r")
        content = file.read()
        file.close()
        self.memoryHandler.loadTree(content)

        #Seguimiento de los saveParents

        self.saveParents = [self.treeA.root]
        """ self.saveParents = [self.treeB.root] """

        #inicializar el programa 
        self.showTree(self.treeA.root.value.children.first)
        """ self.showTree(self.treeB.root.value.children.first) """
        
        #Botones del programa
            #Arbol A
        self.AddFolderA.clicked.connect(self.folderWindow)
        self.AddFileA.clicked.connect(self.fileWindow)
        self.ViewTreeA.itemDoubleClicked.connect(self.surf)
        """ self.DeletA.clicked.connect(self.Delet) """

            #Arbol B
        """ self.AddFolerB.clicked.connect(self.folderWindow)
        self.AddFileB.clicked.connect(self.fileWindow)
        self.AddFolerB.clicked.connect(self.surf) """
        """ self.DeletA.clicked.connect(self.Delet) """



    # Todas las Funciones de la Interfaz    
    
    def save(self,chain):
        #Arbol A
        file = open("Memory/TreeA.mem","w")
        file.write(chain)
        file.close()
        
        #Arbol B
        """ file = open("Memory/TreeB.mem","w")
        file.write(cadena)
        file.close() """



    def showTree(self,current):

        array =["."]
        directoryQueue = LinkedList()
        fileQueue = LinkedList()
    
    #Arbol A
        #Comprobar si esta vacio
        if(current):
            if(not current.value.name == self.treeA.root.value.children.first.value.name):
                array.append("..")
                self.ViewTreeA.addItems(array)

            while(current):
                item = QListWidgetItem(current.value.name)
                if(isinstance(current.value, Directory)):
                    item.setIcon(QIcon("Core/svg/directoryIcon.png"))
                    item.setWhatsThis("Directory")
                    directoryQueue.push(Node(item))
                
                else:
                    item.setIcon(QIcon("Core/svg/fileIcon.png"))
                    item.setWhatsThis("File")
                    fileQueue.push(Node(item))

                current = current.next

            currentDirectory = directoryQueue.pop()
            while(currentDirectory):
                self.ViewTreeA.addItem(currentDirectory.value)
                currentDirectory = directoryQueue.pop()

            currentFile = fileQueue.pop()
            while(currentFile):
                self.Lista.addItem(currentFile.value)
                currentFile = fileQueue.pop()

        else:
            array.append("..")
            self.ViewTreeA.addItems(array)    

    def surf(self):

        selectedValue = self.ViewTreeA.selectedItems()[0].text()
        typeOfSelection = self.ViewTreeA.selectedItems()[0].whatsThis()

        if(valor == ".."):
            self.back()

        elif(typeOfSelection == "File"):
            self.showTree(self.saveParents[len(self.saveParents)-1].value.children.first)

        else:
            
            #Encontrar el nodo       
            Found = self.arbol._search(valor,self.saveParents[len(self.saveParents)-1], "D")

            if(Found and isinstance(Found.value , Directory)):
                      
                #Guardar el padre 
                self.saveParents.append(Found)
 
                #Mostrar los hijos del nodo
                temporal = Found.value.children.first
                self.showTree(temporal)

            else:
                self.showTree(self.saveParents[len(self.saveParents)-1].value.children.first)

    def back(self):

        self.ViewTreeA.clear()

        if(len(self.saveParents) > 1):
           
            self.saveParents.pop(len(self.saveParents)-1)
            goBack = self.saveParents[len(self.saveParents)-1]
            dad = goBack.value.children.first
            self.showTree(dad)
    

    def folderWindow(self):
            #Importar
        from Core.DirectoryDialog import DirectoryDialog
        aFolder = DirectoryDialog()

            #Accion de botones 
        aFolder.ConfirmFolder.clicked.connect(aFolder.getString)
        
            #Finalizar sin Cerrar
        aFolder.exec_()

            #Agregar archivo al arbol
        self.treeA._add(aFolder.word, "D", self.saveParents[len(self.saveParents)-1])
        chain = self.memoryHandler.saveTree(self.treeA.root.value.children.first)
        self.save(chain)

            #Mostrar el arbol
        self.ViewTreeA.clear()

            #Mostrar hijos
        if(len(self.saveParents) > 1):
            self.showTree(self.saveParents[len(self.saveParents)-1].value.children.first)
            
        else:
            self.showTree(self.treeA.root.value.children.first)
        






    def fileWindow(self):
            #Importar
        from Core.FileDialog import FileDialog
        aFile = AbrirArchivo()

            #Accion 
        aFile.ConfirmFile.clicked.connect(aFile.getString)

            #Finalizar sin cerrar  
        aFile.exec_()

            #Agregar file al arbol
        self.treeA._add(aFile.word, "F", self.saveParents[len(self.saveParents)-1])
        chain = self.memoryHandler.saveTree(self.treeA.root.value.children.first)
        self.guardado(chain)

            #Mostrar hijos
        self.ViewTreeA.clear()
        if(len(self.saveParents) > 1):
            self.mostrarLista(self.saveParents[len(self.saveParents)-1].value.children.first)
            print(self.saveParents[len(self.saveParents)-1])

        else:
            self.showTree(self.arbol.root.value.children.first)


    def Delet(self):
        pass





app=QApplication(sys.argv)
widget=MainPage()
widget.show()
sys.exit(app.exec_())  
