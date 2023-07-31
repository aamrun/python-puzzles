#Implementation of python-puzzles/word_search

def word_search(matrix, word):
  for row in matrix:
    if word in "".join(row):
     return True

  columns = len(matrix[0])

  for column in range(0,columns):
    if word in "".join([row[column] for row in matrix]):
     return True

  return False
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM'))
# True

print(word_search(matrix, 'MASS'))
#True

print(word_search(matrix, 'GAME'))
#False

print(word_search(matrix, 'IP'))
#True

print(word_search(matrix, 'ABN'))
#True
