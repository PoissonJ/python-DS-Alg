from Node import Node

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.counter = 0

    # O(N)
    def traverseList(self):

        currentNode = self.head

        print 'Traversing...'
        while currentNode is not None:
            print currentNode.data,
            currentNode = currentNode.nextNode
        print

    # O(1)
    def insertStart(self, data):

        self.counter += 1

        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # O(1)
    def size(self):
        return self.counter

    # O(N)
    def insertEnd(self, data):

        if self.head is None:
            self.insertStart(data)
            return

        self.counter += 1

        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    # O(N)
    def remove(self, data):

        self.counter -= 1

        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)
