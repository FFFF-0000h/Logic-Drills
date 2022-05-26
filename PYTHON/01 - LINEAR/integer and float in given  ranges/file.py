# From the math module, import random, randint
# the random() returns random float 
# the randint returns random integer
from random import randint,random

# collect upper and lower limit of the range
print("Range of integers")
intMin = int(input("enter minimum:"))
intMax = int(input("enter Maximum:"))

n = randint(intMin,intMax)

print("random int:",n)

# collect upper and lower limit of the range
print("Range of floats")
floatMin = float(input("enter minimum:"))
floatMax = float(input("enter Maximum:"))

n = random() * (floatMax-floatMin) + floatMin

print("random float:",n)

