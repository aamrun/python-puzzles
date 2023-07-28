#Implementation of python-puzzles/find_non_duplicate

def singleNumber(nums):
  for num in nums:
   if nums.count(num) == 1:
    return num

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
