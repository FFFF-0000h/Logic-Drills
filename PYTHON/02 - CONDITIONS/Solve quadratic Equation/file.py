from math import sqrt
a = eval(input("Enter a :"))
b = eval(input("Enter b :"))
c = eval(input("Enter c :"))

d = b * b - 4 * a * c 

if d > 0 :
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f"The roots are {x1} and {x2}")
elif d == 0 :
    x1 = (-b / (2 * a))
    print(f"The roots is {x1}")
else:
    print("No roots")    