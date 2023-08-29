#Implementation of python-puzzles/running_median

def running_median(stream):
  stream_length = len(stream)
  medians = []

  for i in range(1,stream_length + 1):
   new_list = sorted(stream[0:i])
   new_length = len(new_list)

   if new_length%2 != 0:
    medians.append(new_list[new_length//2])
   else:
    medians.append((new_list[new_length//2 - 1] + new_list[new_length//2])/2.0)

  return medians

print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2 2.0 2
