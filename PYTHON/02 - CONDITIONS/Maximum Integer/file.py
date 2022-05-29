# Collct inputs
a = input("enter num: ")
b = input("enter num: ")
c = input("enter num: ")

# if a is greater than b and greater than c,
# then it is the maximum
if b <= a >= c:
    print(a,"is the Maximum")
# Otherwise, we check the number B,
# that is greater than both A and C.
elif a <= b >= c:
    print(b,"is tha maximum")