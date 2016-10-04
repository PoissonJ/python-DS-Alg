class Counter(object):
  def __init__(self):
    self.count = 0
  def update(self):
    self.count += 1
  def getCount(self):
    return self.count


def permutations(string, step = 0):
  if step == len(string):
    print "".join(string)
    count_obj.update()

  for i in range(step, len(string)):
    str_copy = list(string)
    str_copy[step], str_copy[i] = str_copy[i], str_copy[step]
    permutations(str_copy, step + 1)

count_obj = Counter()

str = ':)'
permutations(str)

print count_obj.getCount()
