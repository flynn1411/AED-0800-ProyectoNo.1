#-*-coding: utf-8-*-

from Core.list import *

class Tree:
    def __init__(self):
        self.root = Node(Directory("/"))

    def _add(self, name, type, parentNode):
        if(type == 'F'):
            newNode = Node(File(name))
        else:
            newNode = Node(Directory(name))

        return parentNode.value.children.addInList(newNode)

    def _delete(self, deleteValue, parentNode, type = "D"):
        return parentNode.value.children.removeFromList(deleteValue, type)

    def _search(self, searchValue, parentNode, type = "D"):
        return parentNode.value.children.searchInList(searchValue, type)