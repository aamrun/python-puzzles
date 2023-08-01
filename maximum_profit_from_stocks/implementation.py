#Implementation of python-puzzles/maximum_profit_from_stocks

#This is another almost one liner solution utilising Python's list comprehension feature, similar to the implementation of python-puzzles/longest_palindromic_substring
#The inner list comprehension generates the set of all non-empty subsets having more than 1 element 
#and the last element is greater than the first element since only these subsets can generate profits. .
#This list is then used in an outer list comprehension to create a list of the profits from all the subsets.
#The max() function ultimately gives the desired result.

def buy_and_sell(arr):
  return max([prices[-1] - prices[0] for prices in [arr[y:2+x] for y in range(0,len(arr)) for x in range(0,len(arr[1:])) if len(arr[y:2+x])>1 and arr[y:2+x][-1]>=arr[y:2+x][0]]])
  
print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
