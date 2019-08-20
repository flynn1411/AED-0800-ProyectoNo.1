from tree import *

class Memory():
    def __init__(self):
        pass

tree = Tree()

tree._add("hola", "D", tree.root)
tree._add("e", "D", tree.root)
tree._add("a.txt", "F", tree.root.value.children.first)
tree._add("log", "D", tree.root)
tree._add("archivo", "F", tree.root.value.children.first)
tree._add("Hola", "F", tree.root.value.children.first.next.next)

"""
hola/\n
    \ta.txt
    \tarchivo
e/\n
log/\n
    \tHola

"""