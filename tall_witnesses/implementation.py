#Implementation of python-puzzles/tall_witnesses

def witnesses(heights):
  
  if heights is None or len(heights) == 0:
   return 0  
  elif len(heights)==1:
   return 1

  height_list = heights[::-1]

  num_witnesses = 1

  reference_height = height_list[0]

  for witness_height in height_list[1:]:
    if witness_height > reference_height:
     num_witnesses += 1
     reference_height = witness_height

  return num_witnesses

print(witnesses([3, 6, 3, 4, 1]))
# 3
