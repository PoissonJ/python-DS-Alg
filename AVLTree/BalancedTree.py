from Node import Node

class BalancedTree(object):

    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        parentNode = self.rootNode

        if self.rootNode == None:
            parentNode = Node(data, None)
            self.rootNode = parentNode
        else:
            parentNode = self.rootNode.insert(data, self.rootNode)

        self.rebalanceTree(parentNode)

    def rebalanceTree(self, parentNode):
        self.setBalance(parentNode)

        if parentNode.balance < -1:
            if self.height(parentNode.leftChild.leftChild) >=
               self.height(parentNode.leftChild.rightChild):
                parentNode = self.rotateRight(parentNode)
            else:
                parentNode = self.rotateLeftRight(parentNode)

        if parentNode.balance > 1:
            if self.height(parentNode.rightChild.rightChild) >=
               self.height(parentNode.rightChild.leftChild):
                parentNode = self.rotateLeft(parentNode)
            else:
                parentNode = self.rotateRightLeft(parentNode)

        if parentNode.parentNode is not None:
            self.rebalanceTree(parentNode.parentNode)
        else:
            self.rootNode = parentNode
