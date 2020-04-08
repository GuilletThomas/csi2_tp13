from ex1 import Node
class BinaryTree:
    def __init__(self, root):
        self.__root = root

    def getRoot(self):
        return self.__root

node3 = Node(3, None, None)
node4 = Node(4, None, node3)
node6 = Node(6, None, None)
node5 = Node(5, node6, node4)

node18 = Node(18, None, None)
node21 = Node(21, None, None)
node19 = Node(19, node21, node18)
node17 = Node(17, node19, None)

nodeRoot = Node(12, node17, node5)

Root = BinaryTree(nodeRoot)