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
        self.AddFolderA.clicked.connect(lambda tree = "A": self.folderWindow(tree))
        self.AddFileA.clicked.connect(lambda tree = "A": self.fileWindow(tree))
        self.ViewTreeA.itemDoubleClicked.connect(lambda tree = "A": self.surf(tree))
        self.DeletA.clicked.connect(lambda tree = "A": self.Delete(tree))
        self.CopytoB.clicked.connect(lambda tree = "A": self.Copy(tree))

            #Arbol B
        self.AddFolderB.clicked.connect(lambda tree = "B": self.fileWindow(tree))
        self.AddFileB.clicked.connect(lambda tree = "B": self.fileWindow(tree))
        self.ViewTreeB.itemDoubleClicked.connect(lambda tree = "B": self.surf(tree))
        self.DeletB.clicked.connect(lambda tree = "B": self.Delete(tree))
        self.CopyToA.clicked.connect(lambda tree = "B": self.Copy(tree))

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

    def sendParameters(self, tree, function):
        if(tree == "A"):
            currentTree = self.treeA
            currentTreePath = self.saveParentsA
            currentTreeView = self.ViewTreeA

        else:
            currentTree = self.treeB
            currentTreePath = self.saveParentsB
            currentTreeView = self.ViewTreeB

        if(function == "addFolder"):
            pass

    def surf(self, tree):
        if(tree == "A"):
            currentTree = self.treeA
            currentTreePath = self.saveParentsA
            currentTreeView = self.ViewTreeA

        else:
            currentTree = self.treeB
            currentTreePath = self.saveParentsB
            currentTreeView = self.ViewTreeB

        selectedValue = currentTreeView.selectedItems()[0].text()
        typeOfSelection = currentTreeView.selectedItems()[0].whatsThis()
        currentTreeView.clear()

        if(selectedValue == ".."):
            self.back(tree)

        elif(typeOfSelection == "File"):
            self.showTree(currentTreePath[len(currentTreePath)-1].value.children.first, tree)

        else:

            #Encontrar el nodo
            Found = currentTree._search(selectedValue,currentTreePath[len(currentTreePath)-1], "D")

            if(Found and isinstance(Found.value , Directory)):

                #Guardar el padre 
                currentTreePath.append(Found)
 
                #Mostrar los hijos del nodo
                current = Found.value.children.first
                self.showTree(current, tree)

            else:
                self.showTree(currentTreePath[len(currentTreePath)-1].value.children.first, tree)

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
    

    def folderWindow(self, tree):
            #Importar
        from Core.DirectoryDialog import DirectoryDialog
        folderPrompt = DirectoryDialog()

            #Accion de botones 
        folderPrompt.ConfirmFolderWfolderWindow.clicked.connect(folderPrompt.getString)
        
            #Finalizar sin Cerrar
        folderPrompt.exec_()

        if(tree == "A"):
            currentTree = self.treeA
            currentTreePath = self.saveParentsA
            currentTreeView = self.ViewTreeA

        else:
            currentTree = self.treeB
            currentTreePath = self.saveParentsB
            currentTreeView = self.ViewTreeB

            #Agregar archivo al arbol actual

        if(self.validateInput(folderPrompt.word)):
            currentTree._add(folderPrompt.word , currentTreePath[len(currentTreePath)-1] , "D")
            chain = self.memoryHandler.saveTree(currentTree.root.value.children.first)
            self.save(chain, tree)
        else:
            print("Error")

            #Mostrar el arbol actual
        currentTreeView.clear()

            #Mostrar hijos
        if(len(currentTreePath) > 1):
            self.showTree(currentTreePath[len(currentTreePath)-1].value.children.first, tree)
            
        else:
            self.showTree(currentTree.root.value.children.first, tree)
        

    def fileWindow(self, tree):
            #Importar
        from Core.FileDialog import FileDialog
        filePrompt = FileDialog()

            #Accion 
        filePrompt.ConfirmFile.clicked.connect(filePrompt.getString)

            #Finalizar sin cerrar  
        filePrompt.exec_()

        if(tree == "A"):
            currentTree = self.treeA
            currentTreePath = self.saveParentsA
            currentTreeView = self.ViewTreeA

        else:
            currentTree = self.treeB
            currentTreePath = self.saveParentsB
            currentTreeView = self.ViewTreeB

            #Agregar file al arbol actual
        if(self.validateInput(filePrompt.word)):   
            currentTree._add(filePrompt.word, currentTreePath[len(currentTreePath)-1], "F")
            chain = self.memoryHandler.saveTree(currentTree.root.value.children.first)
            self.save(chain, tree)
        else:
            print("Error")

            #Mostrar hijos
        currentTreeView.clear()
        if(len(currentTreePath) > 1):
            self.showTree(currentTreePath[len(currentTreePath)-1].value.children.first, tree)

        else:
            self.showTree(currentTree.root.value.children.first, tree)


    def Delete(self, tree):
        if(tree == "A"):
            currentTree = self.treeA
            currentTreePath = self.saveParentsA
            currentTreeView = self.ViewTreeA

        else:
            currentTree = self.treeB
            currentTreePath = self.saveParentsB
            currentTreeView = self.ViewTreeB

        parent = currentTreePath[len(currentTreePath)-1]
        for item in currentTreeView.selectedItems():
            removeValue = item.text()
            typeOfItem = item.whatsThis()

            if(typeOfItem == "Directory"):
                currentTree._delete(removeValue, parent , "D" )
            else:
                currentTree._delete(removeValue, parent, "F")
        
        chain = self.memoryHandler.saveTree(currentTree.root.value.children.first)
        self.save(chain, tree)
        currentTreeView.clear()
        self.showTree(currentTreePath[len(currentTreePath)-1].value.children.first, tree)
       

    def Copy(self, tree):
        if(tree == "A"):
            departureTree = self.treeA
            departureTreePath = self.saveParentsA
            destinationTree = self.treeB
            destinationTreePath = self.saveParentsB
            treeView = self.ViewTreeA
            newTreeView = self.ViewTreeB
            newTree = "B"

        else:
            departureTree = self.treeB
            departureTreePath = self.saveParentsB
            destinationTree = self.treeA
            destinationTreePath = self.saveParentsA
            treeView = self.ViewTreeB
            newTreeView = self.ViewTreeA
            newTree = "A"
            

        for item in treeView.selectedItems():
            selectedValue = item.text()
            typeOfItem = item.whatsThis()

            if(typeOfItem == "File"):
                
                Found = departureTree._search(selectedValue,departureTreePath[len(departureTreePath)-1], "F")
                if (Found):
                    destinationTree._add(Found , destinationTreePath[len(destinationTreePath)-1] , "F")
                
                else:
                    pass
                
            else:
                Found = departureTree._search(selectedValue,departureTreePath[len(departureTreePath)-1], "D")
                if (Found):
                    destinationTree._add(Found , destinationTreePath[len(destinationTreePath)-1] , "D")

                else:
                    pass

        chain = self.memoryHandler.saveTree(destinationTree.root.value.children.first)
        self.save(chain, newTree)
        newTreeView.clear()
        self.showTree(destinationTreePath[len(destinationTreePath)-1].value.children.first, newTree)


    def validateInput(self, inputValue):
        nameIsValid = True

        if(inputValue == "" or inputValue == " "):
            nameIsValid = False

        else:
            invalidCharacters = "/:*¡!¿?<>|"

            for i in range(len(invalidCharacters)-1):
                if(inputValue.count(invalidCharacters[i])):
                    nameIsValid = False
                    break

        return nameIsValid





app=QApplication(sys.argv)
widget=MainPage()
widget.show()
sys.exit(app.exec_())  