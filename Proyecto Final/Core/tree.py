#-*-coding: utf-8-*-

from Core.list import *

class Tree:
    def __init__(self):
        self.root = Node(Directory("/"))

    def _add(self, newNode, parentNode, typeOfValue = "D"):
        if(not isinstance(newNode, Node)):
            if(typeOfValue == 'F'):
                newNode = Node(File(newNode))
            else:
                newNode = Node(Directory(newNode))

        return parentNode.value.children.addInList(newNode)

    


    def _delete(self, deleteValue, parentNode, type = "D"):
        return parentNode.value.children.removeFromList(deleteValue, type)

    def _search(self, searchValue, parentNode, type = "D"):
        return parentNode.value.children.searchInList(searchValue, type)