#Implementation of python-puzzles/find_pythagorean_triplets

import itertools

def findPythagoreanTriplets(nums):
  for triad in set(itertools.combinations(nums,3)):
    sorted(triad)
    if triad[0]**2 + triad[1]**2 == triad[2]**2:
     return True
  return False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
