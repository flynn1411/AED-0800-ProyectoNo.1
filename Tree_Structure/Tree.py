#-*-coding: utf-8-*-

from List import *

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
        else:
            parentNode = self.search(parentNode)

        return parentNode.value.children.addInList(newNode)

    def search(self, searchValue):
        return self.searchInner(searchValue, self.root)

    def searchInner(self, searchValue, currentNode):
        if(searchValue == currentNode.value.name):
            return currentNode
        
        else:
            if(isinstance(currentNode.value, Directory) and (currentNode.value.children.first)):
                if(self.searchInner(searchValue, currentNode.value.children.first)):
                    return self.searchInner(searchValue, currentNode.value.children.first)

                elif(self.searchInner(searchValue, currentNode.next)):
                    return self.searchInner(searchValue, currentNode.next)

                else:
                    return None

            else:
                if(currentNode.next):
                    if(self.searchInner(searchValue, currentNode.next)):
                        return self.searchInner(searchValue, currentNode.next)

                else:
                    return None

    def _delete(self, deleteValue, parentNode):
        pass

tree = Tree()

print(tree._add("hola", "D", "/"))
print(tree._add("e", "D", "/"))
print(tree._add("a.txt", "F", "hola"))
print(tree._add("log", "D", "/"))
print(tree._add("archivo", "F", "hola"))
print(tree._add("Hola", "F", "log"))
print("\n")

print(tree.search("archivo"))
print(tree.search("log"))
print("\n")

