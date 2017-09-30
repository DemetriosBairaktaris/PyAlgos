

class Node:

    def __init__(self, value=None,next=None):
        self.value = value
        self.next = next

    def setValue(self, value):
        self.value = value

    def setNext(self, nextNode):
        self.next = nextNode

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next


class LinkedList:

    def __init__(self):
        self.root = None
        self.length = 0
        self.last = None

    def __add__(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.root = newNode
            self.last = self.root
        else:
            self.last.setNext(newNode)
            self.last = newNode

        self.length += 1

    def __str__(self):
        currentNode = self.root
        l = []

        while  currentNode!= None:
            l.append(currentNode.getValue())
            currentNode = currentNode.getNext()

        return str(l)

    def pop(self):
        self.root = self.root.next
        self.length -= 1

    def removeValue(self,value):
        previousNode = None
        currentNode = self.root
        while currentNode != None:
            if currentNode.getValue() == value:
                if previousNode == None:
                    self.pop()
                else:
                    previousNode.setNext(currentNode.getNext())

                self.length -= 1
                break
            else:
                placeHolder = currentNode
                currentNode = currentNode.getNext()
                previousNode = placeHolder

    def removeIndex(self,index):
        if(index >= self.length or index < -self.length):
            return
        index = index % self.length
        index = abs(index)
        if(index == 0 or index == 3):
            self.pop()
            return

        previousNode = None
        currentNode = self.root
        i = 0
        while i < index:
            placeholder = currentNode
            currentNode = currentNode.getNext()
            previousNode = placeholder
            i += 1

        previousNode.setNext(currentNode.getNext())
        self.length -= 1

    def reverseIter(self):
        prevNode = None
        currentNode = self.root
        while currentNode != None:
            nextNode = currentNode.getNext()
            currentNode.setNext(prevNode)
            prevNode = currentNode
            currentNode = nextNode
        self.root = prevNode

    def reverseRec(self ,prevNode = None, currentNode=None, nextNode = None):
        if currentNode is None:
            self.root = prevNode
        else:
            nextNode = currentNode.getNext()
            currentNode.setNext(prevNode)
            prevNode = currentNode
            currentNode = nextNode
            self.reverseRec(prevNode, currentNode, nextNode)

def main():
    l = LinkedList()
    for i in range(40):
        l + i
    print l
    l.reverseRec(currentNode=l.root)
    print l


if __name__ == '__main__':
    main()