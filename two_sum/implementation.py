#python-puzzles/two_sum

#Yes, this is kind of a hack. The ideal solution should not use any libraries, even if they are part of the language standard.

import itertools

def two_sum(list, k):
  for pair in itertools.combinations(list,2):
    if sum(pair)==k:
     return True
  return False

print(two_sum([4,7,1,-3,2], 5))

# True

