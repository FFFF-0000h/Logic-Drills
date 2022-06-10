print("The coordinates of a point:")
x = eval(input("Enter x:"))
y = eval(input("Enter y:"))

if x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")
elif x == 0 and y == 0:
    print("At the origin")
elif x == 0:
    print("on Y-axis")
elif y == 0:
    print("on x-axis")
   