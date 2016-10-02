from Node import Node

class TST(object):

  def __init__(self):
    self.rootNode = None

  def put(self, key, value):
    self.rootNode = self.putItem(self.rootNode, key, value, 0)

  def putItem(self, node, key, value, index):

    c = key[index]

    if node == None:
      node = Node(c)

    # Only increment index if we have a match
    if c < node.character:
      node.leftNode = self.putItem(node.leftNode, key, value, index)
    elif c > node.character:
      node.rightNode = self.putItem(node.rightNode, key, value, index)

    # we have a match but the entire key has not been used yet
    elif  index < len(key) - 1:
      node.num += 1
      node.middleNode = self.putItem(node.middleNode, key, value, index + 1)

    else:
      node.num += 1
      node.value = value

    return node


  def get(self, key):
    node = self.getItem(self.rootNode, key, 0)

    if node == None:
      return None

    return node.value

  def getItem(self, node, key, index):

    if node == None:
      return None

    c = key[index]

    if c < node.character:
      return self.getItem(node.leftNode, key, index)
    elif c > node.character:
      return self.getItem(node.rightNode, key, index)
    elif index < len(key) - 1:
      return self.getItem(node.middleNode, key, index + 1)
    else:
      return node

  def getItemNum(self, node, key, index):

    if node == None:
      return 0

    c = key[index]

    if c < node.character:
      return self.getItemNum(node.leftNode, key, index)
    elif c > node.character:
      return self.getItemNum(node.rightNode, key, index)
    elif index < len(key) - 1:
      return self.getItemNum(node.middleNode, key, index + 1)
    else:
      return node.num

  def getNumberOfSimilar(self, searchTerm):
    """Gets the number of entries that start with the given search term"""
    ans = self.getItemNum(self.rootNode, searchTerm, 0)
    return ans
