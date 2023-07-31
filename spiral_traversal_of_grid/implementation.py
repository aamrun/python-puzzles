#Implementation of python-puzzles/spiral_traversal_of_grid

def matrix_spiral_print(matrix):
  columns, rows = len(matrix[0]),len(matrix)

  counter = 0

  while columns > 2 * counter and rows > 2 * counter:
   for column in range(counter,columns-counter):
    print(matrix[counter][column],end = " ")
   for row in range(counter + 1,rows-counter):
    print(matrix[row][columns - counter - 1],end = " ")
   for column in range(columns - counter - 2,0,-1):
    print(matrix[rows - counter - 1][column],end = " ")
   for row in range(rows - counter - 2, counter + 1, -1):
    print(matrix[row][counter],end = " ")

   counter += 1

  print("\b")

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
