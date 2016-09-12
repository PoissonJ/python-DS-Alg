from Queue import Queue

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.dequeue()
queue.dequeue()
print queue.size()
queue.dequeue()
print queue.size()
