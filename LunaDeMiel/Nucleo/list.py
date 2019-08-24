#-*-coding: utf-8-*-
from compare import*

"""
    Nodo
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
"""
    Clases de los valores de un nodo cualquiera
"""

#Directory
class Directory:
    def __init__(self, name):
        self.name = name
        self.children = LinkedList()

#File
class File:
    def __init__(self, name):
        self.name = name


"""
    Lista enlazada y sus metódos.
    Se ordenarán sus elementos utilizando la libreria Compare
"""
class LinkedList:
    def __init__(self):
        self.first = None

    def pop(self):
        if(not self.first):
            return None

        popped = self.first
        self.first = popped.next
        popped.next = None
        return popped
    
    def addInList(self, newNode):
        if(not self.first):
            self.first = newNode
            return True

        else:
            current = self.first
            previous = None
            compare = Compare()
            

            while(current):
                comparison = compare.compare(current.value.name, newNode.value.name)
                #si el nombre del actual es menor al que se desa agregar, se sigue recorriendo
                if(comparison < 0):
                    #Si el actual no tiene siguiente y se debe de seguir avanzando, el siguiente 
                    #del actual es el nuevo nodo
                    if(not current.next):
                        current.next = newNode
                        return True

                    else:
                        previous = current
                        current = current.next

                #Si el nombre del actual es el mismo al que se desea agregar, se reemplazan
                elif(comparison == 0):
                    #Se guardan los hijos del actual en el que se desea agregar
                    if(isinstance(newNode.value, Directory)):
                        newNode = self.mergeChildren(current, newNode)

                    #Si no hay previo, esto me indica que el nodo a reemplazar
                    #es el primero en la lista
                    if(not previous):
                        if(current.next):
                            newNode.next = current.next
                        
                        self.first = newNode
                        return True

                    else:
                        if(current.next):
                            newNode.next = current.next

                        previous.next = newNode
                        return True

                #Si el actual es mayor al que se desea agregar, se agrega el nuevo antes del actual
                else:
                    newNode.next = current
                    if(not previous):
                        self.first = newNode
                    else:
                        previous.next = newNode

                    return True
            return False


    def mergeChildren(self, oldNode, newNode):
        #Si el nodo a reemplazar no tiene hijos, solo se retorna el nodo nuevo
        if(not oldNode.value.children.first):
            return newNode

        else:
            currentChild = oldNode.value.children.pop()
            while(currentChild):
                newNode.value.children.addInList(currentChild)
                currentChild = oldNode.value.children.pop()

            #newNode.value.children.addInList(currentChild)
            return newNode

    def removeFromList(self, removevalue):
        current = self.first
        previous = None

        while(current):
            if(current.value.name == removevalue):
                #si no hay previo ni siguente, el que se desea borrar es el primero de la lista
                if(not previous and not current.next):
                    self.first = None
                    return True

                elif(not previous and current.next):
                    self.first = current.next
                    return True

                elif(previous and not current.next):
                    previous.next = None
                    return True
                
                else:
                    previous.next = current.next
                    return True

            else:
                previous = current
                current = current.next

    def searchInList(self, searchValue):
        return self.searchInnerInList(searchValue, self.first)

    def searchInnerInList(self, searchValue, current):
        if(not current):
            return None
        else:
            if(current.value.name == searchValue):
                return current
            else:
                return self.searchInnerInList(searchValue, current.next)

"""
    def printList(self):
        current = self.first
        trail = " "

        while(current.next):
            trail = trail + current.value.name + "->"
            current = current.next

        trail = trail + current.value.name

        print(trail)

list = LinkedList()

nodo0 = Node(Directory("hola"))
nodo0.value.children.addInList(Node(File("a.py")))
nodo0.value.children.addInList(Node(File("acdc.py")))

nodo1 = Node(Directory("hola"))
nodo1.value.children.addInList(Node(File("ab.py")))
nodo1.value.children.addInList(Node(File("uno.py")))

list.addInList(nodo0)
list.printList()

list.addInList(Node(Directory("H0l@xd01")))
list.printList()

list.addInList(Node(File("Ariel")))
list.printList()

list.addInList(nodo1)
list.printList()

list.addInList(Node(Directory("Fernando")))
list.printList()

list.addInList(Node(Directory("3Fernando")))
list.printList()

list.removeFromList("H0l@xd01")
list.printList()

print(list.searchInList("Fernando"))
"""