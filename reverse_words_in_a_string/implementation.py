#Implementation of python-puzzles/reverse_words_in_a_string

class Solution:
  def reverseWords(self, str):
    return " ".join([i[::-1] for i in str.split(" ")])

print(Solution().reverseWords("The cat in the hat"))
