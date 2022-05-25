print("A(x1,y1):")
x1 = float(input("\tx1: "))
y1 = float(input("\ty1: "))

print("B(x2,y2):")
x2 = float(input("\tx2: "))
y2 = float(input("\ty2: "))


print("Equation:")

k = (y1 - y2) / (x1 - x2)

c = y2 - k  * x2
print(f"\t y = {k}x + {c}")

