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
        if(not self.first):
            self.first = newNode
            return True

        else:
            current = self.first;
            previous = None
            currentChildren = None

            while(current):
                #si el nombre del actual es menor al 







    def printList(self):
        current = self.first
        trail = " "

        while(current.next):
            trail = trail + current.value.name + "->"
            current = current.next

        trail = trail + current.value.name

        print(trail)

list = LinkedList()

list.addInList(Node(File("hola")))
list.printList()

list.addInList(Node(Directory("H0l@xd01")))
list.printList()

list.addInList(Node(File("Ariel")))
list.printList()

list.addInList(Node(File("hola")))
list.printList()

list.addInList(Node(Directory("Fernando")))
list.printList()