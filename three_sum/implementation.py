#Implementation of python-puzzles/three_sum

class Solution(object):
  def threeSum(self, nums):
    triplets = []

    nums_length = len(nums)
    
    k = 0    
    for a in nums[0:nums_length-2]:
     k += 1
     for b in nums[k:nums_length-1]:
      for c in nums[k+1:nums_length]:
       if a + b + c == 0:
        print([a,b,c])
        present = False
        for i in triplets:
         if sorted(i) == sorted([a, b, c]):
          present = True
        
        if present is False:
         triplets.append([a, b, c])

     return triplets

nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]

nums = [0, -1, 2, -3, 1]
print(Solution().threeSum(nums))
#[[0, -1, 1],[2, -3, 1]]
