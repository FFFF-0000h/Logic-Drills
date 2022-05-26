# First step in writing any program is understanding the problem
# The problem we have at hand is to add the digits of a random 3digits number e.g 234 should output == 9 i.e 2 + 3 + 4
# Unlike javascript we will have to import random
from random import random
# The random() generates a random fractional number from 0 to 1

# when the number is multiplied by 900,
# the range of number we can obtain will
# be from 0 to 899.(9)
# if you add 100  i.e 899 + 100 = 999

num = random() * 900 + 100

# with int() you can discard the decimal part
num = int(num)
print(f"num:{num}")
# At this stage, we have gotten the required random number

# Now you want to divide the number into digits
# to get thr first digit
# int divide the number by 100
a = num // 100 

# The second digit will be gotten by int dividing the num by 10
# then get remainder by remainder division with 10

b = (num // 10) % 10

# Then the last digit is gotten by using remainder divion by 10

c = num % 10

print(a+b+c)

