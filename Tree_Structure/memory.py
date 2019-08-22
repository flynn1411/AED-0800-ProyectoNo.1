from tree import *

class MemoryHandler():
    def __init__(self):
        pass

    def save(self, node, memoryContent = "", depth = 0):
        if(not node):
            return ""

        else:
            if(not isinstance(node.value, Directory)):
                memoryContent = ("%s%s\n%s"%(memoryContent, node.value.name, self.save(node.next, "\t"*depth, depth)))

            else:
                children = ""
                if(node.value.children.first):
                    children = self.save(node.value.children.first, "\t"*(depth+1), depth+1)

                memoryContent = ("%s%s/\n%s%s"%(memoryContent, node.value.name, children, self.save(node.next, "\t"*depth, depth)))
        
        return memoryContent

                    
                

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

memoryHandler = MemoryHandler()
content = memoryHandler.save(tree.root.value.children.first)

file = open("prueba.mem", "w")
file.write(content)
file.close()

"""
e/
    a.txt
    archivo
hola
log/
    Hola
"""