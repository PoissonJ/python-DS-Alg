dict = {'Joe': 14, 'Adam': 26, 'Emily': 56}

# O(1)
print dict['Joe']

dict['Joe'] = 15 # update

# dict.clear() to remove all entries
# del dict to remove the whole dictionary itself

# duplicate keys are allowed!!

print dict.items() # return everything back

print dict.keys()
print dict.values()

print 'sorted by age (value)'
for k, v in sorted(dict.items(), key=lambda (k, v): v):
  print '{}\'s age is {}'.format(k, v)

print 'sorted by name (key)'
for k, v in sorted(dict.items()):
  print '{}\'s age is {}'.format(k, v)
