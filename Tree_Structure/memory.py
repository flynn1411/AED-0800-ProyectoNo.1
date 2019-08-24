from tree import *

class MemoryHandler:
    def __init__(self):
        self.aTree = Tree()

    def _save(self):
        pass

    def saveTree(self, node, memoryContent = "", depth = 0):
        if(not node):
            return ""

        else:
            if(not isinstance(node.value, Directory)):
                memoryContent = ("%s%s\n%s"%(memoryContent, node.value.name, self.saveTree(node.next, "\t"*depth, depth)))

            else:
                children = ""
                if(node.value.children.first):
                    children = self.saveTree(node.value.children.first, "\t"*(depth+1), depth+1)

                memoryContent = ("%s%s/\n%s%s"%(memoryContent, node.value.name, children, self.saveTree(node.next, "\t"*depth, depth)))
        
        return memoryContent

    def packNode(self, name, parent):
        if(name[len(name)-1] == "/"):
            name = name.split("/")
            name = name[0]
            return self.aTree._add(name, "D", parent)
        else:
            return self.aTree._add(name, "F", parent)


    def loadTree(self, memoryContent):
        if(memoryContent == ""):
            return 

        else:
            path = [self.aTree.root]
            rows = memoryContent.split("\n")
            #Se hace un pop para remover el ultimo elemento, el cual es un espacio en blanco
            rows.pop()
            currentDepth = 0
            
            for i in range (len(rows)-1):
                rowDepth = rows[i].count("\t")
                nodeName = rows[i].strip()
                lastIndex = len(path)-1

                #Si el numero de espacios es mayor al la profundidad actual,
                #se mueve un paso mas adentro porque solo se puede ir un paso a la vez 
                #cuando uno se mueve hacia adelante
                if(rowDepth > currentDepth):
                    #Asumo que el del nodo a agregar es el elemento previo del arreglo
                    newParent = rows[i-1].strip()

                    if(newParent[len(newParent)-1] == "/"):
                        newParent = newParent.split("/")
                        newParent = newParent[0]

                    path.append(self.aTree._search(newParent, path[lastIndex]))
                    #No se utiliza la variable last index en este caso porque se agrega
                    #otro elemento al arreglo, esto tambien se hace en caso que se deba
                    #recorrer mas profundamente en el arbol

                    self.packNode(nodeName, path[len(path)-1])
                    currentDepth += 1

                #Si el numero de espacios es menor al de la profundidad actual,
                #tengo que ir hacia atras usando la diferencia entre la profundidad
                #y el numero de espacios (currentDepth - rowDepth)
                elif(rowDepth < currentDepth):
                    while(rowDepth < currentDepth):
                        path.pop()
                        currentDepth -= 1

                    self.packNode(nodeName, path[len(path)-1])

                #Si el numero de espacios es el mismo al de la profundidad actual,
                #simplemente se agrega el nuevo nodo al ultimo elemento de path
                else:
                    self.packNode(nodeName, path[lastIndex])
                    
                

tree = Tree()

tree._add("hola", "F", tree.root)
tree._add("e", "D", tree.root)
tree._add("a.txt", "F", tree.root.value.children.first)
tree._add("log", "D", tree.root)
tree._add("xdxd", "F", tree.root.value.children.first)
tree._add("archivo", "D", tree.root.value.children.first)
tree._add("archivo2", "D", tree.root.value.children.first.value.children.first.next)
tree._add("Prueba", "F", tree.root.value.children.first.value.children.first.next.value.children.first)
tree._add("Hola", "F", tree.root.value.children.first.next.next)

memoryHandler = MemoryHandler()
content = memoryHandler.saveTree(tree.root.value.children.first)


"""file = open("Memory/prueba.mem", "w")
file.write(content)
file.close()

file2 = open("Memory/prueba.mem", "r")
fileContent = file2.read()
file2.close()"""

memoryHandler.loadTree(content)
loadedTree = memoryHandler.saveTree(memoryHandler.aTree.root.value.children.first)
print(loadedTree)

"""
e/
    a.txt
    archivo
hola
log/
    Hola
"""