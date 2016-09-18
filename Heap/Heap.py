class MaxHeap(object):

    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] * MaxHeap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self, item):

        if self.isFull():
            print 'Heap is full...'
            return

        self.currentPosition = self.currentPosition + 1
        self.heap[self.currentPosition] = item
        self.fixUp(self.currentPosition)

    def fixUp(self, index):

        parentIndex = int((index - 1) / 2)

        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            index = parentIndex
            parentIndex = int((index - 1) / 2)

    def isFull(self):
        if self.currentPosition == MaxHeap.HEAP_SIZE:
            return True
        else:
            return False

    def fixDown(self, index, upto):

        while index < upto:

            leftChild = 2 * index + 1
            rightChild = 2 * index + 2

            if leftChild <= upto:

                childToSwap = None

                if rightChild > upto:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild

                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break

                index = childToSwap
            else:
                break

    # perform O(N logN) sorting IN PLACE
    def heapsort(self):
        for i in range(0, self.currentPosition + 1):

            # Get max value
            temp = self.heap[0]
            print("%d " % temp)


            # Swap the root node (max value) with the last node in the heap
            self.heap[0] = self.heap[self.currentPosition - i]
            self.heap[self.currentPosition - i] = temp

            # Make sure that after the swap, we will end up with a valid
            # max heap and only consider the nodes that have not been sorted
            # in the fix down algorithm
            self.fixDown(0, self.currentPosition - i - 1)
