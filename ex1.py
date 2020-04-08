class Node:
    def __init__(self, val, right, left):
        self.__val = val
        self.__right = right
        self.__left = left

    def getVal(self):
        return self.__val
    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left

    def setLeft(self, d):
        self.__left = d
        return self.__left
    def setRight(self, d):
        self.__right = d
        return self.__right

x = Node(13,2,9)
print(x.getLeft())