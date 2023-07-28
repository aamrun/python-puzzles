#Implementation of python-puzzles/find_kth_largest_element_in_list

def findKthLargest(nums, k):
  sorted_nums = sorted(list(set(nums)))[::-1]
  
  if k > len(sorted_nums):
   return None
  else:
   return sorted_nums[k-1]

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5
