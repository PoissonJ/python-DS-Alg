import sys

class Vertex(object):

  def __init__(self, name):
    self.name = name
    self.visited = False
    self.predecessor = None
    self.adjacenciesList = []
    self.minDistance = sys.maxsize

  # Need these two methods to be able to use a min heap as a built in
  # Data Structure. This overrides the comparator and less than functions.
  def __cmp__(self, otherVertex):
    # Compare the 2 min distances
    return self.cmp(self.minDistance, otherVertex.minDistance)

  def __lt__(self, other):
    # Return the smallest distance
    selfPriority = self.minDistance
    otherPriority = other.minDistance

    return selfPriority < otherPriority
