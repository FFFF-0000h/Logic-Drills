from turtle import position


c = input("Letter(a-z): ")

# ord() returns the ordinal number of a character in the symbol table
# The code for the first letter of the small letter alphabet is ord("a") = 97
# The letters are followed in an order
code = ord(c)


# therfore the distance can be gotten by subtracting 
# the code of the first letter from the code of the input letter
# and then the position can be gotten by adding 1
position_ = code - ord("a") + 1

print(f"Position of letter {c} is {position_}")
