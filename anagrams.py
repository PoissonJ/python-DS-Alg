def permutations(string, step = 0):
  global counter
  if step == len(string):
    print "".join(string)
    counter += 1

  for i in range(step, len(string)):
    str_copy = list(string)
    str_copy[step], str_copy[i] = str_copy[i], str_copy[step]
    permutations(str_copy, step + 1)

str = ':)'
counter = 0
permutations(str)
print counter
