#Implementation of python-puzzles/first_and_Last_indices_of_an_element_in_sorted_array

class Solution: 
  def getRange(self, arr, target):
    positions = []
    try:
        positions.append(arr.index(target))
    except ValueError:
        return [-1,-1]

    positions.append(len(arr) - arr[::-1].index(target) - 1)

    return positions
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15]
target = 9
print(Solution().getRange(arr, target))
#Output: [6,8]

A = [100, 150, 150, 153]
target = 150
print(Solution().getRange(A, target))
#Output: [1,2]

A = [1,2,3,4,5,6,10]
target = 9
print(Solution().getRange(A, target))
#Output: [-1, -1]
