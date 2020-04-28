from ex1 import Node
class BinaryTree:
    def __init__(self, root):
        self.__root = root

    def getRoot(self):
        return self.__root

    def isRoot(self, node):
        if node == self.__root:
            return True
        else :
            return False

    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.getLeft()) + 1 + self.size(node.getRight())

    def printValues(self, node):
        print(node.getVal())
        if node.getLeft() is None and node.getRight() is None:
            return node.getVal()

        else:
            return self.printValues(node.getLeft()) + 1 + self.printValues(node.getRight())









node3 = Node(3, None, None) #valeur,right,left
node4 = Node(4, None, node3)
node6 = Node(6, None, None)
node5 = Node(5, node6, node4)

node18 = Node(18, None, None)
node21 = Node(21, None, None)
node19 = Node(19, node21, node18)
node17 = Node(17, node19, None)

nodeRoot = Node(12, node17, node5)

Root = BinaryTree(nodeRoot)

if __name__ == "__main__":
    print(Root.size(nodeRoot))
    print(Root.printValues(nodeRoot))


