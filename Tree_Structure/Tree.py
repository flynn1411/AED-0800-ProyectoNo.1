#-*-coding: utf-8-*-

from LinkedList import *

class Tree:
    def __init__(self):
        self.root = Node(Directory("/"))

    def _add(self, name, type, parentNode):
        if(type == 'F'):
            newNode = Node(File(name))
        else:
            newNode = Node(Directory(name))

        if(not self.search(parentNode)):
            parentNode = self.root

        return parentNode.value.children.addInList(newNode)

    def search(self, searchValue):
        return self.searchInner(searchValue, self.root)

    def searchInner(self, searchValue, current):
        if(searchValue == current.value.name):
            return current
        
            
