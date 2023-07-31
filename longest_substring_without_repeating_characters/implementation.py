#Implementation of python-puzzles/longest_substring_without_repeating_characters

#This is essentially a one liner solution utilising Python's list comprehension feature. 
#The inner list comprehension generates the set of all consecutive substrings of the given string. 
#This list is converted into a set to eliminate duplicates. 
#The outer list comprehension works on this set and generates a list of lengths for each element of the set which has only unique characters. 
#The max() function ultimately gives the desired result.

class Solution:
  def lengthOfLongestSubstring(self, string):
    return max([len(set(element)) for element in set([string[y:2+x] for y in range(0,len(string)) for x in range(0,len(string[1:]))]) if len(element) == len(set(element))])

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
