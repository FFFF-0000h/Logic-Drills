# Here is a program to calculate the perimeter 
# and area of a right-angled triangle 
# using two legs entered as input

# lets import math module containing various maths functions

import math

# input() returns a string
AB = input("Length of the first leg: ")
AC = input("Length of the second leg: ")

# float() returns real number if it can be converted
AB = float(AB)
AC = float(AC)

# find the hypotenus 
# by the pythagorean theorem:
# "the sum of the squares of the legs
# is equal to the sqaure of the hypotenuse."
# The Sqrt() function of the math module
# returns a squareroot.

BC = math.sqrt(AB**2 + AC**2)

# The area of a triangle is equal to half of the
# area of the corresponding rectangle
area = (AB*AC) / 2

# Perimeter is the sum of all sides.
perimeter = AB + AC + BC


print(f"area of the triangle: {area}")
print(f"perimeter of the triangle: {perimeter}")