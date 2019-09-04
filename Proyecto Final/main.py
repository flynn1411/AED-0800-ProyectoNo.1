# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox,QListWidgetItem
from PyQt5.uic import loadUi
from Core.tree import *
from Core.memory import *

class MainPage(QDialog):
    def __init__(self):


        #Cargar la interfaz
        super(MainPage, self).__init__()
        loadUi('Core/MainInterface.ui', self)

        #Cargar el treeA A

        self.memoryHandler = MemoryHandler()
        self.treeA = self.memoryHandler.tree
        file = open("Memory/Tree-A.mem","r")
        content = file.read()
        file.close()
        self.memoryHandler.loadTree(content)

        #Cargar el arbol B

        self.memoryHandler = MemoryHandler()
        self.treeB = self.memoryHandler.tree
        file = open("Memory/Tree-B.mem","r")
        content = file.read()
        file.close()
        self.memoryHandler.loadTree(content)

        #Seguimiento de los saveParents

        self.saveParentsA = [self.treeA.root]
        self.saveParentsB = [self.treeB.root]

        #inicializar el programa 
        self.showTree(self.treeA.root.value.children.first, "A")
        self.showTree(self.treeB.root.value.children.first, "B")
        
        #Botones del programa
            #Arbol A
        self.AddFolderA.clicked.connect(self.folderWindowA)
        self.AddFileA.clicked.connect(self.fileWindowA)
        self.ViewTreeA.itemDoubleClicked.connect(self.surfA)
        self.DeletA.clicked.connect(self.DeleteA)
        self.CopytoB.clicked.connect(self.CopyAtoB)

            #Arbol B
        self.AddFolderB.clicked.connect(self.folderWindowB)
        self.AddFileB.clicked.connect(self.fileWindowB)
        self.ViewTreeB.itemDoubleClicked.connect(self.surfB)
        self.DeletB.clicked.connect(self.DeleteB)
        self.CopyToA.clicked.connect(self.CopyBtoA)

            #Cerrar el programa 
        self.close.clicked.connect(self.quit)



    # Todas las Funciones de la Interfaz    .
    def quit(self):
        quit()
    
    def save(self,chain, tree):
        fileName = ""

        if(tree == "A"):
            fileName = "Memory/Tree-A.mem"
        else:
            fileName = "Memory/Tree-B.mem"

        file = open(fileName,"w")
        file.write(chain)
        file.close()



    def showTree(self,current, tree):

        array =["."]
        directoryQueue = LinkedList()
        fileQueue = LinkedList()
        currentTree = None

        if(tree == "A"):
            listView = self.ViewTreeA
            currentTree = self.treeA
        else:
            listView = self.ViewTreeB
            currentTree = self.treeB
    
        #Comprobar si esta vacio
        if(current):
            if(not current.value.name == currentTree.root.value.children.first.value.name):
                array.append("..")
                listView.addItems(array)

            while(current):
                item = QListWidgetItem(current.value.name)
                if(isinstance(current.value, Directory)):
                    if(current.value.children.first):
                        item.setIcon(QIcon("Core/svg/directoryWithChildren.png"))

                    else:
                        item.setIcon(QIcon("Core/svg/emptyDirectory.png"))

                    item.setWhatsThis("Directory")
                    directoryQueue.push(Node(item))
                
                else:
                    self.setFileIcon(item)
                    item.setWhatsThis("File")
                    fileQueue.push(Node(item))

                current = current.next

            currentDirectory = directoryQueue.pop()
            while(currentDirectory):
                listView.addItem(currentDirectory.value)
                currentDirectory = directoryQueue.pop()

            currentFile = fileQueue.pop()
            while(currentFile):
                listView.addItem(currentFile.value)
                currentFile = fileQueue.pop()

        else:
            array.append("..")
            listView.addItems(array)

    def setFileIcon(self, item):
        if(item.text().count(".mp3") > 0):
            item.setIcon(QIcon("Core/svg/mp3.png"))
            
        elif(item.text().count(".mp4") > 0):
            item.setIcon(QIcon("Core/svg/mp4.png"))

        elif(item.text().count(".txt") > 0):
            item.setIcon(QIcon("Core/svg/txt.png"))
        
        elif(item.text().count(".cpp") > 0):
            item.setIcon(QIcon("Core/svg/cpp.png"))
        
        elif(item.text().count(".html") > 0):
            item.setIcon(QIcon("Core/svg/html.png"))

        elif(item.text().count(".py") > 0):
            item.setIcon(QIcon("Core/svg/py.png"))
        
        elif(item.text().count(".jar") > 0):
            item.setIcon(QIcon("Core/svg/jar.png"))

        elif(item.text().count(".js") > 0):
            item.setIcon(QIcon("Core/svg/javascript.png"))

        elif(item.text().count(".json") > 0):
            item.setIcon(QIcon("Core/svg/json.png"))

        elif(item.text().count(".psd") > 0):
            item.setIcon(QIcon("Core/svg/psd.png"))

        else:
            item.setIcon(QIcon("Core/svg/fileIcon.png"))

    def surfA(self):
        selectedValue = self.ViewTreeA.selectedItems()[0].text()
        typeOfSelection = self.ViewTreeA.selectedItems()[0].whatsThis()
        self.ViewTreeA.clear()

        if(selectedValue == ".."):
            self.back("A")

        elif(typeOfSelection == "File"):
            self.showTree(self.saveParentsA[len(self.saveParentsA)-1].value.children.first, "A")

        else:

            #Encontrar el nodo
            Found = self.treeA._search(selectedValue,self.saveParentsA[len(self.saveParentsA)-1], "D")

            if(Found and isinstance(Found.value , Directory)):

                #Guardar el padre 
                self.saveParentsA.append(Found)
 
                #Mostrar los hijos del nodo
                current = Found.value.children.first
                self.showTree(current, "A")

            else:
                self.showTree(self.saveParentsA[len(self.saveParentsA)-1].value.children.first, "A")

    def back(self, tree):

        if(tree == "A"):
            listView = self.ViewTreeA
            currentParents = self.saveParentsA
        else:
            listView = self.ViewTreeB
            currentParents = self.saveParentsB

        listView.clear()

        if(len(currentParents) > 1):
           
            currentParents.pop(len(currentParents)-1)
            goBack = currentParents[len(currentParents)-1]
            dad = goBack.value.children.first
            self.showTree(dad, tree)
    

    def folderWindowA(self):
            #Importar
        from Core.DirectoryDialog import DirectoryDialog
        aFolder = DirectoryDialog()

            #Accion de botones 
        aFolder.ConfirmFolder.clicked.connect(aFolder.getString)
        
            #Finalizar sin Cerrar
        aFolder.exec_()

            #Agregar archivo al treeA
        if(self.validateInput(aFolder.word)):
            self.treeA._add(aFolder.word , self.saveParentsA[len(self.saveParentsA)-1] , "D")
            chain = self.memoryHandler.saveTree(self.treeA.root.value.children.first)
            self.save(chain, "A")
        else:
            print("Error: El nombre ingresado no es permitido.")

            #Mostrar el treeA
        self.ViewTreeA.clear()

            #Mostrar hijos
        if(len(self.saveParentsA) > 1):
            self.showTree(self.saveParentsA[len(self.saveParentsA)-1].value.children.first, "A")
            
        else:
            self.showTree(self.treeA.root.value.children.first, "A")
        

    def fileWindowA(self):
            #Importar
        from Core.FileDialog import FileDialog
        aFile = FileDialog()

            #Accion 
        aFile.ConfirmFile.clicked.connect(aFile.getString)

            #Finalizar sin cerrar  
        aFile.exec_()

            #Agregar file al treeA 
        if(self.validateInput(aFile.word)):   
            self.treeA._add(aFile.word, self.saveParentsA[len(self.saveParentsA)-1], "F")
            chain = self.memoryHandler.saveTree(self.treeA.root.value.children.first)
            self.save(chain, "A")
        else:
            print("Error: El nombre ingresado no es permitido.")

            #Mostrar hijos
        self.ViewTreeA.clear()
        if(len(self.saveParentsA) > 1):
            self.showTree(self.saveParentsA[len(self.saveParentsA)-1].value.children.first, "A")

        else:
            self.showTree(self.treeA.root.value.children.first, "A")


    def DeleteA(self):
        parent = self.saveParentsA[len(self.saveParentsA)-1]
        for item in self.ViewTreeA.selectedItems():
            removeValue = item.text()
            typeOfItem = item.whatsThis()

            if(typeOfItem == "Directory"):
                self.treeA._delete(removeValue, parent , "D" )
            else:
                self.treeA._delete(removeValue, parent, "F")
        
        chain = self.memoryHandler.saveTree(self.treeA.root.value.children.first)
        self.save(chain, "A")
        self.ViewTreeA.clear()
        self.showTree(self.saveParentsA[len(self.saveParentsA)-1].value.children.first, "A")
       

    def CopyAtoB(self):

        for item in self.ViewTreeA.selectedItems():
            selectedValue = item.text()
            typeOfItem = item.whatsThis()

            if(typeOfItem == "File"):
                
                Found = self.treeA._search(selectedValue,self.saveParentsA[len(self.saveParentsA)-1], "F")
                if (Found):
                    self.treeB._add(Found , self.saveParentsB[len(self.saveParentsB)-1] , "F")

                else:
                    break
                
            else:
                Found = self.treeA._search(selectedValue,self.saveParentsA[len(self.saveParentsA)-1], "D")
                if (Found):
                    self.treeB._add(Found , self.saveParentsB[len(self.saveParentsB)-1] , "D")

                else:
                    break

        chain = self.memoryHandler.saveTree(self.treeB.root.value.children.first)
        self.save(chain, "B")        
        self.ViewTreeB.clear()
        self.showTree(self.saveParentsB[len(self.saveParentsB)-1].value.children.first, "B")
       
    #treeB

    def CopyBtoA(self):

        for item in self.ViewTreeB.selectedItems():
            selectedValue = item.text()
            typeOfItem = item.whatsThis()

            if(typeOfItem == "File"):
                
                Found = self.treeB._search(selectedValue,self.saveParentsB[len(self.saveParentsB)-1], "F")
                if (Found):
                    self.treeA._add(Found , self.saveParentsA[len(self.saveParentsA)-1] , "F")

                else:
                    break
                
            else:
                Found = self.treeB._search(selectedValue,self.saveParentsB[len(self.saveParentsB)-1], "D")
                if (Found):
                    self.treeA._add(Found , self.saveParentsA[len(self.saveParentsA)-1] , "D")

                else:
                    break
        
        chain = self.memoryHandler.saveTree(self.treeA.root.value.children.first)
        self.save(chain, "A")
        self.ViewTreeA.clear()
        self.showTree(self.saveParentsA[len(self.saveParentsA)-1].value.children.first, "A")
                

    def surfB(self):
        selectedValue = self.ViewTreeB.selectedItems()[0].text()
        typeOfSelection = self.ViewTreeB.selectedItems()[0].whatsThis()
        self.ViewTreeB.clear()

        if(selectedValue == ".."):
            self.back("B")

        elif(typeOfSelection == "File"):
            self.showTree(self.saveParentsB[len(self.saveParentsB)-1].value.children.first, "B")

        else:

            #Encontrar el nodo
            Found = self.treeB._search(selectedValue,self.saveParentsB[len(self.saveParentsB)-1], "D")

            if(Found and isinstance(Found.value , Directory)):

                #Guardar el padre 
                self.saveParentsB.append(Found)
 
                #Mostrar los hijos del nodo
                current = Found.value.children.first
                self.showTree(current, "B")

            else:
                self.showTree(self.saveParentsB[len(self.saveParentsB)-1].value.children.first, "B")

    def DeleteB(self):
        parent = self.saveParentsB[len(self.saveParentsB)-1]
        for item in self.ViewTreeB.selectedItems():
            removeValue = item.text()
            typeOfItem = item.whatsThis()

            if(typeOfItem == "Directory"):
                self.treeB._delete(removeValue, parent, "D")
            else:
                self.treeB._delete(removeValue, parent, "F")

        chain = self.memoryHandler.saveTree(self.treeB.root.value.children.first)
        self.save(chain, "B")
        self.ViewTreeB.clear()
        self.showTree(self.saveParentsB[len(self.saveParentsB)-1].value.children.first, "B")
        

    def folderWindowB(self):
            #Importar
        from Core.DirectoryDialog import DirectoryDialog
        bFolder = DirectoryDialog()

            #Accion de botones 
        bFolder.ConfirmFolder.clicked.connect(bFolder.getString)
        
            #Finalizar sin Cerrar
        bFolder.exec_()

            #Agregar archivo al treeA
        if(self.validateInput(bFolder.word)):
            self.treeB._add(bFolder.word , self.saveParentsB[len(self.saveParentsB)-1] , "D")
            chain = self.memoryHandler.saveTree(self.treeB.root.value.children.first)
            self.save(chain, "B")
        else:
            print("Error: El nombre ingresado no es permitido.")

            #Mostrar el treeB
        self.ViewTreeB.clear()

            #Mostrar hijos
        if(len(self.saveParentsB) > 1):
            self.showTree(self.saveParentsB[len(self.saveParentsB)-1].value.children.first, "B")
            
        else:
            self.showTree(self.treeB.root.value.children.first, "B")
        

    def fileWindowB(self):
            #Importar
        from Core.FileDialog import FileDialog
        bFile = FileDialog()

            #Accion 
        bFile.ConfirmFile.clicked.connect(bFile.getString)

            #Finalizar sin cerrar  
        bFile.exec_()

            #Agregar file al treeA
        if(self.validateInput(bFile.word)):
            self.treeB._add(bFile.word , self.saveParentsB[len(self.saveParentsB)-1] , "F")
            chain = self.memoryHandler.saveTree(self.treeB.root.value.children.first)
            self.save(chain, "B")
        else:
            print("Error: El nombre ingresado no es permitido.")

            #Mostrar hijos
        self.ViewTreeB.clear()
        if(len(self.saveParentsB) > 1):
            self.showTree(self.saveParentsB[len(self.saveParentsB)-1].value.children.first, "B")

        else:
            self.showTree(self.treeB.root.value.children.first, "B")


    def validateInput(self, inputValue):
        nameIsValid = True

        if(inputValue == "" or inputValue == " "):
            nameIsValid = False

        else:
            invalidCharacters = " /:*¡!¿?<>|"

            for i in range(len(invalidCharacters)-1):
                if(inputValue.count(invalidCharacters[i])):
                    nameIsValid = False
                    break

        return nameIsValid

app=QApplication(sys.argv)
widget=MainPage()
widget.show()
sys.exit(app.exec_())  