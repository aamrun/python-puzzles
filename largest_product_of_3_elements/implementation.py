#Implementation of python-puzzles/largest_product_of_3_elements

import itertools

def maximum_product_of_three(lst):
  maximum = None

  for subset in itertools.combinations(lst,3):
    product = subset[0] * subset[1] * subset[2]

    if maximum is None or maximum < product:
     maximum = product

  return maximum

print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
