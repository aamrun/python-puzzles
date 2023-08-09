def capacity(arr):
  N = len(arr)
  highest_left = [0] + [max(arr[:n]) for n in range(1,N)]
  highest_right = [max(arr[n:N]) for n in range(1,N)] + [0]
  water_level = [max(min(highest_left[n], highest_right[n]) - arr[n], 0) for n in range(N)]
  return sum(water_level)

potholes = [[1, 5, 3, 7, 2],
    [5, 3, 7, 2, 6, 4, 5, 9, 1, 2],
    [2, 6, 3, 5, 2, 8, 1, 4, 2, 2, 5, 3, 5, 7, 4, 1],
    [5, 5, 5, 5],
    [5, 6, 7, 8],
    [8, 7, 7, 6],
    [6, 7, 10, 7, 6],
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]

[print(f"Street : {street} , Collected rainwater : {capacity(street)}") for street in potholes]
