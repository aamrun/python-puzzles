#Implementation of python-puzzles/validate_balanced_parentheses

class Solution:
  def isValid(self, s):
    opener_list,openers,enders = [],"[{(",")}]"
    
    if s == "" or s is None:
     return True

    strlen = len(s)

    for i in range(0,strlen):
      if s[i] in enders and opener_list == []:
       return False
      elif s[i] in openers:
       opener_list.append(s[i])
      elif s[i] in enders:
       if (s[i] == ")" and opener_list[-1] != "(") or (s[i] == "}" and opener_list[-1] != "{") or (s[i] == "]" and opener_list[-1] != "["):
        return False
       elif (s[i] == ")" and opener_list[-1] == "(") or (s[i] == "}" and opener_list[-1] == "{") or (s[i] == "]" and opener_list[-1] == "["):
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
