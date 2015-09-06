#!/usr/bin/python
from array import array

###Class Student definition
class Student:
  def __init__(self, name, gpa, age):
    self.name = name
    self.gpa = gpa
    self.age = age

  def __str__(self):
    return "%s with GPA: %f, in age: %d" %(self.name, self.gpa, self.age)

  def __lt__(self, other):
    if (self.gpa < other.gpa): return True
    elif (self.gpa > other.gpa): return False
    elif (self.name < other.name): return True
    elif (self.name > other.name): return False
    elif (self.age < other.age): return True
    else: return False

  def __eq__(self, other):
    return (self.name == other.name and self.gpa == other.gpa and self.age == other.age)

  def __hash__(self):
    return hash((self.name, self.gpa, self.age))


def main():
  ###Create a test array of 5 students
  student_list = [Student('Tom', 4.0, 22), Student('Jim', 3.5, 22), Student('Lily', 3.7, 21), Student('Tracy', 3.9, 23), Student('Paul', 3.7, 22)]
  print "student_list"
  for elem in student_list: print elem
  print '\n'
  
  ###Test codes with sorted() and dict()
  sorted_list = sorted(student_list)
  print "sorted_list"
  for elem in sorted_list: print elem
  print '\n'

  print "student_dict"
  student_dict = dict([(elem.__hash__(), elem) for elem in student_list])
  for key in student_dict:
    print key,
    print ":",
    print student_dict[key]
  print '\n'

  ###sort in order if increasing GPA using a lambda expression
  print "student_list sorted with lambda"
  ### return a tuple to break the ties
  student_list.sort(key = lambda s: (s.gpa, s.name, s.age))
  for elem in student_list: print elem

  return 

if __name__ == "__main__":
  main()
