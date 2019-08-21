from tree import *

class MemoryHandler():
    def __init__(self):
        pass

    def save(self, node, memoryContent = "", level = 1):
        if(not node):
            return ""

        else:
            if(not isinstance(node.value, Directory)):
                memoryContent = ("%s%s\n%s"%(memoryContent, node.value.name, self.save(node.next, memoryContent)))

            else:
                directoryName = node.value.name
                children = ""
                if(node.value.children.first):
                    spacing = "\t"*level
                    newLevel = level+1
                    children = self.save(node.value.children.first, spacing, newLevel)

                memoryContent = ("%s%s/\n%s%s"%(memoryContent, directoryName, children, self.save(node.next, memoryContent)))
        
        return memoryContent

                    
                

tree = Tree()

tree._add("hola", "F", tree.root)
tree._add("e", "D", tree.root)
tree._add("a.txt", "F", tree.root.value.children.first)
tree._add("log", "D", tree.root)
tree._add("xdxd", "F", tree.root.value.children.first)
tree._add("archivo", "D", tree.root.value.children.first)
tree._add("archivo2", "D", tree.root.value.children.first.value.children.first.next)
tree._add("Hola", "F", tree.root.value.children.first.next.next)

memoryHandler = MemoryHandler()
content = memoryHandler.save(tree.root.value.children.first)

file = open("prueba.mem", "w")
file.write(content)
file.close()

newN = 1
print("/t"*newN)

"""
e/
    a.txt
    archivo
hola
log/
    Hola
"""