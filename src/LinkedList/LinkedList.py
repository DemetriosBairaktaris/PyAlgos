

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

    def __len__(self):
        return self.length

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
        if(index is not -1):
            self.removeIndex(index)
        #removeIndex decrements the self.length for us...
        #don't need to do it here


    def _isValidIndex(self,index):

        isValid = True
        if (index >= self.length or index < -self.length):
            isValid = False
        return isValid

    def _convertIndex(self,index):

        if self._isValidIndex(index):
            index = index % self.length
            index = abs(index)
        else:
            raise Exception("Index out of bounds")
        return index

    def removeIndex(self,index):

        index = self._convertIndex(index)
        if index == 0:
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

    l.removeIndex(len(l)-1)
    print l
    l.reverseIter()
    print l


if __name__ == '__main__':
    main()