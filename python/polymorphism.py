#!/usr/bin/python
class Shape:
  def __init__(self):
    pass
  def msg(self):
    return 'base shape'

class Circle(Shape):
  def msg(self):
    return 'Circle'

class Rectangle(Shape):
  def msg(self):
    return 'Rectangle'

shapes = [Shape(), Circle(), Rectangle()]
for shape in shapes:
  print shape.msg()
