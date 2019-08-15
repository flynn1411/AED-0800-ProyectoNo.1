#-*-coding: utf-8-*-
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
    
    def addInList(self, newNode):
        return self.addInListInner(newNode, self.first)

    def addInListInner(self, newNode, current):
        if(not self.first):
            self.first = newNode
            return True

        else:
            if(current.next):
                return self.addInListInner(newNode, current.next)

            else:
                current.next = newNode
                return True