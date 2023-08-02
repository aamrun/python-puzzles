#Implementation of python-puzzles/validate_balanced_parentheses

class Solution:
  def isValid(self, s):
    opener_list,brackets = [],{')':'(','}':'{',']':'['}
    
    if s == "" or s is None:
     return True

    for s_char in s:
      if s_char in brackets and opener_list == []:
       return False
      elif s_char in brackets.values():
       opener_list.append(s_char)
      elif s_char in brackets:
       if brackets[s_char] != opener_list[-1]:
        return False
       else:
        opener_list.pop()

    if opener_list != []:
     return False

    return True

# Test Program
s = "()(){(())" 
# should return False
print(f"String : {s} , Valid : {Solution().isValid(s)}")

s = ""
# should return True
print(f"String : {s} , Valid : {Solution().isValid(s)}")

s = "([{}])()"
# should return True
print(f"String : {s} , Valid : {Solution().isValid(s)}")

s = "((()))" 
# should return True
print(f"String : {s} , Valid : {Solution().isValid(s)}")

s = "[()]{}"
# should return True
print(f"String : {s} , Valid : {Solution().isValid(s)}")

s = "({[)]"
# should return False
print(f"String : {s} , Valid : {Solution().isValid(s)}")
