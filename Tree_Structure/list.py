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
    
    def addInList(self, newNode):
        return self.addInListInner(newNode, self.first)

    def addInListInner(self, newNode, current):
        compare = Compare()

        if(not self.first):
            self.first = newNode
            return True

        else:
            previousNode = None
            orphans = None

            while(current.next):
                if(compare.compare(current.value.name, newNode.value.name) < 0):
                    previousNode = current
                    current = current.next

                elif(compare.compare(current.value.name, newNode.value.name) == 0):
                    if(isinstance(current, Directory) and current.value.children.first):
                        orphans = current.value.children.first
                        self.saveTheOrphans(orphans, newNode)

                    if(not previousNode):
                        self.first = newNode
                        self.first.next = current.next
                        return True
                    
                    else:
                        previousNode.next = newNode
                        newNode.next = current.next
                        return True
                
                else:
                    