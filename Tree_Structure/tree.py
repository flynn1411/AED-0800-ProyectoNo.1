#-*-coding: utf-8-*-

from list import *

class Tree:
    def __init__(self):
        self.root = Node(Directory("/"))

    def _add(self, name, type, parentNode):
        if(type == 'F'):
            newNode = Node(File(name))
        else:
            newNode = Node(Directory(name))

        return parentNode.value.children.addInList(newNode)

    def _delete(self, deleteValue, parentNode):
        return parentNode.value.children.removeNode(deleteValue)

tree = Tree()

print(tree._add("hola", "D", tree.root))
print(tree._add("e", "D", tree.root))
print(tree._add("a.txt", "F", tree.root.value.children.first))
print(tree._add("log", "D", tree.root))
print(tree._add("archivo", "F", tree.root.value.children.first))
print(tree._add("Hola", "F", tree.root.value.children.first.next.next))
print("\n")

