# Python 2.7
"""
Author: Demetrios Bairaktaris
Description: Implementation of a Heap in Python
"""

import random


class Heap:
    def __init__(self):
        self.underLyingArray = []
        self.isMaxHeap = True

    def __add__(self, node):
        self.underLyingArray.append(node)
        self.floatUp()

    def maxHeapify(self):
        self.isMaxHeap = True
        self.heapify()

    def minHeapify(self):
        self.isMaxHeap = False
        self.heapify()

    def heapify(self):
        l = list(range(len(self.underLyingArray) / 2))
        l.reverse()
        for n in l:
            self.sinkDown(n)

    def mustExchange(self, child, parent):
        if child > parent and self.isMaxHeap:
            return True
        elif child < parent and not self.isMaxHeap:
            return True
        else:
            return False

    def compareChildren(self, left, right):
        if right is None:
            return 1
        if self.isMaxHeap:
            if left > right:
                return 1
            else:
                return 2
        else:
            if left < right:
                return 1
            else:
                return 2

    def floatUp(self, i=None):
        if i is None:
            i = len(self.underLyingArray) - 1

        node = self.underLyingArray[i]
        parent = self.underLyingArray[(i - 1) / 2]

        while self.mustExchange(node, parent):
            self.underLyingArray[i] = parent
            self.underLyingArray[(i - 1) / 2] = node
            i = (i - 1) / 2
            if i <= 0:
                break
            else:
                node = self.underLyingArray[i]
                parent = self.underLyingArray[(i - 1) / 2]

    def sinkDown(self, n):
        while 1:
            if (2 * n + 1) >= len(self.underLyingArray):
                break

            parentNode = self.underLyingArray[n]
            childLeft = self.underLyingArray[2 * n + 1]
            childRight = None

            if (2 * n + 2) < len(self.underLyingArray):
                childRight = self.underLyingArray[2 * n + 2]

            childNumber = self.compareChildren(childLeft, childRight)
            childToSwap = self.underLyingArray[2 * n + childNumber]

            if self.mustExchange(childToSwap, parentNode):
                placeholder = self.underLyingArray[n]
                self.underLyingArray[n] = self.underLyingArray[2 * n + childNumber]
                self.underLyingArray[2 * n + childNumber] = placeholder
                n = 2 * n + childNumber
            else:
                break

    def pop(self):
        root, leaf = self.underLyingArray[0], self.underLyingArray[-1]
        self.underLyingArray[0] = leaf
        self.underLyingArray[-1] = root
        self.underLyingArray.pop(-1)
        l = list(range(len(self.underLyingArray)))
        l.reverse()
        self.sinkDown(0)


def main():
    unorderedList = []
    for i in range(10):
        unorderedList.append(random.randrange(30))
    h = Heap()
    h.underLyingArray = list(unorderedList)
    h.maxHeapify()
    print h.underLyingArray
    h.minHeapify()
    h + 3
    h + 1000
    print h.underLyingArray


if __name__ == '__main__':
    main()
