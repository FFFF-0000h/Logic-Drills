# functions such as pow() and constant such as pi can be imported
# importing the whole math module
import math


# or simply 
# from math import pow,pi

# getting the radius value in string form through input() function
# float() function converts the string to float(real number)
radius = float(input("Radius: "))


# length of the circumference is 2*pi*r
len = 2 * math.pi * radius

# The area of the circle is pi*r*r
area = math.pi * math.pow(radius,2)

# or 
# area = math.pi * radius * radius
# or
# area = math.pi * radius ** 2


print("Length: ",len)
print("Area: ",area)