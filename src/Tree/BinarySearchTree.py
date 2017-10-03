from math import sin


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

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            currentNode = self.root

            while 1:
                if currentNode.getValue() > value:
                    if currentNode.getLeft() is None:
                        currentNode.setLeft(Node(value))
                        break
                    else:
                        currentNode = currentNode.getLeft()
                elif currentNode.getValue() < value:
                    if currentNode.getRight() is None:
                        currentNode.setRight(Node(value))
                        break
                    else:
                        currentNode = currentNode.getRight()

    def traverseInOrder(self, node=None, l=[]):
        if node is None:
            return

        if node.getLeft() is not None:
            l.append(self.traverseInOrder(node.getLeft(), l))

        l.append(node.getValue())

        if node.getRight() is not None:
            l.append(self.traverseInOrder(node.getRight(), l))

    def __str__(self):
        l = []
        self.traverseInOrder(self.root, l)
        return str([x for x in l if x is not None])


def main():

    b = BinarySearchTree()
    for i in range(200):
        b.add(sin(i))
    print b


if __name__ == '__main__':
    main()
