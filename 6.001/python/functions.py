"""
Overview: Starting learning the MIT Computer Science Degree Curriculum.
Date: 22/09/20
Lesson: Basic introduction to functions using basic mathematics
"""

import math


def square(num):
  return num**2


def fourthPower(num):
  return num**4


def isOdd(num):
  if (num % 2) == 0:
    return False
  return True


def pointDist(x1, y1, x2, y2):
  xDif = (x2 - x1)**2
  yDif = (y2 - y1)**2
  return math.sqrt(xDif + yDif)


def evalQuadratic(a, b, c):
  if a != 0:
    sol1 = (-b + math.sqrt(b**2 - 4*(a*c))) / (2*a)
    sol2 = (-b - math.sqrt(b**2 - 4*(a*c))) / (2*a)
    return sol1, sol2
  return None


def distanceFromPointToLine(px, py, a, b, c):
  top = (a * px) + (b * py) + c
  bottom = math.sqrt((a**2 + b**2))
  return abs((top / bottom))
  3