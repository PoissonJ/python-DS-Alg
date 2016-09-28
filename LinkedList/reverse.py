from LinkedList import LinkedList

linkedList = LinkedList()

linkedList.insertEnd(12)
linkedList.insertEnd(122)
linkedList.insertEnd(3)
linkedList.insertStart(31)
linkedList.insertEnd(40)
linkedList.insertEnd(100)
linkedList.insertEnd(99)
linkedList.insertEnd(51)
linkedList.insertEnd(2)
linkedList.insertEnd(300)
linkedList.insertEnd(9)
linkedList.insertEnd('hello')

linkedList.traverseList()

print 'Reversing...'
linkedList.reverse()

linkedList.traverseList()
