# Collct inputs
a = input("enter num: ")
b = input("enter num: ")
c = input("enter num: ")

# if a is greater than b and greater than c,
# then it is the maximum.
if b <= a >= c:
    print(a,"is the Maximum")
# Otherwise, we check the number B,
# that is greater than both a and c.
elif a <= b >= c:
    print(b,"is tha maximum")
# Otherwise, we check the number C,
# that it is greater than both a and b.
elif a  <=c >= b:
    print(c)
    
# nb 1: The last elif can be replaced by a
#  branch without a condition (else) 

# nb 2: In conditional expressions,
# the sign = is necessary for the case when  
# two numbers have maximum values  