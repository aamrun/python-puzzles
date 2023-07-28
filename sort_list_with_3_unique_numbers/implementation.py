#Implementation of python-puzzles/sort_list_with_3_unique_numbers

def sortNums(nums):
  count_ones = nums.count(1)
  count_twos = nums.count(2)
  count_threes = nums.count(3)

  nums = []
  
  [nums.append(1) for i in range(0,count_ones)]

  [nums.append(2) for i in range(0,count_twos)]

  [nums.append(3) for i in range(0,count_threes)]

  return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
