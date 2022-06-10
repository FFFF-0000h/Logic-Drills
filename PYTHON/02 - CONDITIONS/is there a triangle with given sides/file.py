print("Length of the sides: ")
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

# Each of them should be less than the sum of the other
# Therefore, the logical AND operator is used
if a + b > c and a + c > b and b + c > a :
    print("The triangle exists")
   
else:
    print("The triangle doesnt exists") 

