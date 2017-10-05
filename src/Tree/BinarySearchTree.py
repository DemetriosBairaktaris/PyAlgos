from random import randrange as randomNumberFromRange

class Node:

    def __init__(self, value=None):

        self.value = value
        self.left = None
        self.right = None

    def getRight(self):

        return self.right

    def getLeft(self):

        return self.left

    def getValue(self):

        return self.value

    def setValue(self, value):

        self.value = value

    def setRight(self, right):

        self.right = right

    def setLeft(self, left):

        self.left = left


class BinarySearchTree:
    def __init__(self):

        self.root = None

    def emptyTree(self):

        self._setRoot(None)

    def _setRoot(self, valueToBeSet):

        self.root = valueToBeSet

    def pushValue(self, valueToBePushed):

        currentNode = self.root
        setNode = None

        if currentNode is None:
            setNode = self._setRoot

        while currentNode is not None:
            if currentNode.getValue() > valueToBePushed:
                setNode = currentNode.setLeft
                currentNode = currentNode.getLeft()

            elif currentNode.getValue() < valueToBePushed:
                setNode = currentNode.setRight
                currentNode = currentNode.getRight()
            else:
                return   #value is already in the tree

        newNode = Node(valueToBePushed)
        setNode(newNode)

    def traverseInOrderAndCollect(self, node=None, nodeList=[]):

        if node is None:
            return

        if node.getLeft() is not None:
            nodeList.append(self.traverseInOrderAndCollect(node.getLeft(), nodeList))

        nodeList.append(node.getValue())

        if node.getRight() is not None:
            nodeList.append(self.traverseInOrderAndCollect(node.getRight(), nodeList))

    def _removeNoneTypes(self, listToOperateOn):

        return [node for node in listToOperateOn if node is not None]

    def __str__(self):
        nodeList = []
        self.traverseInOrderAndCollect(self.root, nodeList)
        nodeList = self._removeNoneTypes(nodeList)
        return str(nodeList)


def main():

    tree = BinarySearchTree()
    for i in range(2000):
        tree.pushValue(randomNumberFromRange(20000))
    print tree

    tree.emptyTree()
    print tree


if __name__ == '__main__':
    main()
