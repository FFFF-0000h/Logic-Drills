# Step1: Understand the problem (research and comprehension)

# import the constant pi ftomthe math module
from math import pi

# get cylinder height
h = float(input("enter height: "))

# cylinder base radius 
r = float(input("enter radius: "))

# As a cylinder as two bases
# and the area of each is (pi*r**2)

bases = 2 * pi * r**2

# The area of the side surface of cylinder = 2*pi*r* h

sides = 2 * pi * r * h

# total surface area 
area = sides + bases

print("Area: ",area)