

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

        while currentNode is not None:
            l.append(currentNode.getValue())
            currentNode = currentNode.getNext()

        return str(l)

    def __contains__(self, item):
        return self.indexOf(item) is not -1

    def pop(self):
        self.root = self.root.next
        self.length -= 1

    def indexOf(self,value):
        index = -1
        counter = 0
        currentNode = self.root
        while currentNode is not None:
            if currentNode.getValue() == value:
                index = counter
                break
            else:
                counter +=1
                currentNode = currentNode.getNext()

        return index

    def removeValue(self,value):

        index = self.indexOf(value)
        self.removeIndex(index)
        #removeIndex decrements the self.length for us...
        #don't need to do it here

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
        while currentNode is not None:
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
    for i in range(4):
        l + i
    print l
    l.reverseRec(currentNode=l.root)
    print l
    l.removeValue(36)
    l.removeIndex(20)
    print 0 in l


if __name__ == '__main__':
    main()