#Implementation of python-puzzles/move_zeroes

class Solution:
  def moveZeros(self, nums):
    starting_length = len(nums)

    [nums.remove(i) for i in nums if i==0]

    new_length = len(nums)

    [nums.append(0) for i in range(0,starting_length - new_length)]

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]

Solution().moveZeros(nums)

print(nums)
