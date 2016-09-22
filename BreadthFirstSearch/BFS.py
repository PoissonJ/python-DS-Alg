def bfs(startNode):

  queue = []
  startNode.visited = True
  queue.append(startNode)

  while queue:

    actualNode = queue.pop()
    print('%s ' % actualNode.name)

    for n in actualNode.adjacenciesList:
      if not n.visited:
        n.visited = True
        queue.append(n)
