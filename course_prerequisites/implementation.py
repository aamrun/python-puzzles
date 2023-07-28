#Implementation of python-puzzles/course_prerequisites

#None is NULL in Python

def courses_to_take(course_to_prereqs):
  course_list = []

  while len(course_to_prereqs) != len(course_list):
    for course in course_to_prereqs:

      if set(course_list) == set(course_to_prereqs[course]):
       course_list.append(course)

  if course_list == []:
   return None

  return course_list

courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}

print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
