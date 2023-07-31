#Implementation of python-puzzles/minimum_size_subarray_sum

#This is another almost one liner solution utilising Python's list comprehension feature, similar to the implementation of python-puzzles/longest_palindromic_substring
#The inner list comprehension generates the set of all non-empty subsets of the given number list.
#This list is then used in a dictionary comprehension to form key value pairs of the subsets and their sums, provided those sums equal the required sum s.
#Note that the dictionary comprehension casts or converts the subsets as strings. This is because Python lists are unhashable and cannot be used as dictionary keys. 
#The workaround is to use strings which for all purposes are identical to character lists.
#The min() function ultimately gives the desired result using a lambda function.

class Solution:
  def minSubArray(self, nums, s):
    sum_set = {str(nums):sum(nums) for nums in [nums[y:2+x] for y in range(0,len(nums)) for x in range(0,len(nums[1:])) if len(nums[y:2+x])!=0] if sum(nums) == s}
    if sum_set is None or len(sum_set)==0:
     return None
    else:
     return min(sum_set,key = lambda k: len(k))

print(Solution().minSubArray([2, 3, 1, 2, 4, 3], 7))
