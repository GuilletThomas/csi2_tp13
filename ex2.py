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
        if node is None:
            return ""
        else:
            return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())

    def sumValues(self, node):
        if node is None:
            return 0
        else:
            return self.sumValues(node.getLeft()) + self.sumValues(node.getRight()) + int(node.getVal())

    def numberLeaves(self,node):
        if node is None:
            return 0
        elif (node.getRight()==None and node.getLeft() == None):
            return 1
        else:
            return self.numberLeaves(node.getLeft()) + self.numberLeaves(node.getRight())

    def numberInternalNodes(self, node):
        if node is None:
            return 0
        elif node.getRight() != None or node.getLeft() != None:
            return 1 + self.numberInternalNodes(node.getLeft()) + self.numberInternalNodes(node.getRight())
        else :
            return 0

    def height(self, node):
        if node is None:
            return -1
        else:
            leftHeight = self.height(node.getLeft())
            rightHeight = self.height(node.getRight())
            return max(leftHeight, rightHeight) + 1

    #def height(self, node):
            #if node == None:
                #return 0
            #return max(1 + self.size(node.getLeft()), 1 + self.size(node.getRight())) - 1


    def belongs(self, node, val):
        if node is None:
            return False
        if node.getVal()!=val:
            return self.belongs(node.getRight(),val) or self.belongs(node.getLeft(),val)
        else:
            return True



    #def ancestors(self, node, val):






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
    print(Root.sumValues(nodeRoot))
    print(Root.numberLeaves(nodeRoot))
    print(Root.numberInternalNodes(nodeRoot))
    print(Root.height(nodeRoot))
    print(Root.belongs(nodeRoot, 18))


