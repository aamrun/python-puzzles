#Implementation of python-puzzles/longest_substring_without_repeating_characters

#This is another one liner solution utilising Python's list comprehension feature, similar to the implementation of python-puzzles/longest_substring_without_repeating_characters
#The inner list comprehension generates the set of all non-empty palindromic substrings of the given string.
#This list is then used in a dictionary comprehension to form key value pairs of the substrings and their lengths.
#The outer list generator works on this set and generates a list of lengths for each element of the set which has only unique characters.
#The max() function ultimately gives the desired result.

class Solution: 
    def longestPalindrome(self, string):
      word_set = {string:len(string) for string in [string[y:2+x] for y in range(0,len(string)) for x in range(0,len(string[1:])) if string[y:2+x]==string[y:2+x][::-1] and len(string[y:2+x])!=0]}
      return max(word_set,key = word_set.get)

s = ["tracecars","banana","million"]

[print(f"String : {string} , Longest palindromic substring : {Solution().longestPalindrome(string)}") for string in s]
