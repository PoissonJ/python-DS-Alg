from TST import TST

tree = TST()

tree.put('apple', 100)
tree.put('app', 500)
tree.put('orange', 200)

print(tree.get('apple'))
print(tree.get('app'))
print(tree.get('orange'))

print tree.getNumberOfSimilar('app')
