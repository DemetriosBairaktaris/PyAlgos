
class Node:

    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value = value

    def setRight(self,right):
        self.right = right

    def setLeft(self, left):
        self.left = left




class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            currentNode = self.root
            next = 0
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

    def traverse(self, node = None):
        if node is None:
            return
        else:
            self.traverse(node.getLeft())
            print node.getValue()
            self.traverse(node.getRight())


    def values(self):
        self.traverse(self.root)


def main():
    b = BinarySearchTree()
    b.add(4)
    b.add(2)
    b.add(32)
    b.values()


if __name__ == '__main__':
    main()