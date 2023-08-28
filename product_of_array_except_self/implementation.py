#Implementation of python-puzzles/product_of_array_except_self

def product(arr):
 prod = 1
 
 for i in arr:
  prod *= i

 return prod

def products(nums):
  list_length = len(nums)

  product_list = []

  for index in range(0,list_length):
   if index == 0:
    product_list.append(product(nums[1:]))
   elif list_length - index == 1:
    product_list.append(product(nums[:-1]))
   else:
    product_list.append(product(nums[:index] + nums[index + 1:]))

  return product_list

print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]

