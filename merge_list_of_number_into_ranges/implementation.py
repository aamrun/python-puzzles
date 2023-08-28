#Implementation of python-puzzles/merge_list_of_number_into_ranges

def findRanges(nums):
  range_list = []

  start_num, end_num = nums[0], nums[0]

  for i in nums:
   if i - end_num > 1:
    range_list.append(str(start_num) + '->' + str(end_num))
    start_num, end_num = i, i
   else:
    end_num = i

  range_list.append(str(start_num) + '->' + str(end_num))

  return range_list

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
