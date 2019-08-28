from Core.tree import *

class MemoryHandler:
    def __init__(self):
        self.tree = Tree()

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
            return self.tree._add(name , parent , "D")
        else:
            return self.tree._add(name , parent , "F")


    def loadTree(self, memoryContent):
        if(memoryContent == ""):
            return 

        else:
            path = [self.tree.root]
            rows = memoryContent.split("\n")
            rows.pop()
            currentDepth = 0
            
            for i in range (len(rows)):
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

                    path.append(self.tree._search(newParent, path[lastIndex]))
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

                   