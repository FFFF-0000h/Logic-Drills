import math
# The coordinates of a point that is either inside the circle or not.
print("points: ")
x = float(input("x: "))
y = float(input("y: "))

print("Radius of circle: ")
r = float(input("r:"))

hypotenus = math.sqrt(x**2 + y**2)
print(f"hypotenus:{hypotenus}")
if hypotenus <= r :
    print("point belongs to the circle")
else:
    print("Points doesnt belong to the circle")