from tree import *


tree = Tree()

tree._add("hola", "F", tree.root)
tree._add("e", "D", tree.root)
tree._add("a.txt", "F", tree.root.value.children.first)
tree._add("log", "D", tree.root)
tree._add("xdxd", "F", tree.root.value.children.first)
tree._add("archivo", "D", tree.root.value.children.first)
tree._add("archivo2", "D", tree.root.value.children.first.value.children.first.next)
tree._add("Prueba", "F", tree.root.value.children.first.value.children.first.next.value.children.first)
tree._add("Hola", "F", tree.root.value.children.first.next.next)

array = []
#hola , e , log.

current = tree.root.value.children.first

while(current.next):

    array.append(current.value.name)
    current = current.next
    
array.append(current.value.name)

print(array)