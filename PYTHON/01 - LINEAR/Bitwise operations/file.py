n1 = input("Binary n1: ")
n2 = input("Binary n1: ")
print()

# use int() to convert the inputs to number in base 2
n1 = int(n1,2)
n2 = int(n2,2)


bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2



bit_or = bin(bit_or)
bit_and = bin(bit_and)
bit_xor = bin(bit_xor)

print("n1: ",bin(n1))
print("n2: ",bin(n2))
print("OR: ",bit_or)
print("AND: ",bit_and)
print("XOR: ",bit_xor)