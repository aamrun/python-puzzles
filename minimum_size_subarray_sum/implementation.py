#Implementation of python-puzzles/minimum_size_subarray_sum

#This is another almost one liner solution utilising Python's list comprehension feature, similar to the implementation of python-puzzles/longest_palindromic_substring
#The inner list comprehension generates the set of all non-empty subsets of the given number list.
#This list is then used in an outer list comprehension to store only those subsets whose sums equal the required sum s.
#A previous version of this implementation used a dictionary to store key value pairs of the lists and their sums. Since all the sums are the same, storing it is not required.
#The min() function ultimately gives the desired result using a lambda function.

class Solution:
  def minSubArray(self, nums, s):
    sum_set = [nums for nums in [nums[y:2+x] for y in range(0,len(nums)) for x in range(0,len(nums[1:])) if len(nums[y:2+x])!=0] if sum(nums) == s]
    if sum_set is None or len(sum_set)==0:
     return None
    else:
     return min(sum_set,key = lambda k: len(k))

print(Solution().minSubArray([2, 3, 1, 2, 4, 3], 7))
