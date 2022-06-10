# The check of divisibilty makes sense only for Integers
# Therefore, we convert the string returned by the input() function to an integer type using the int() function.

largeInt = int(input("Enter the larger Num:"))
smallInt = int(input("Enter the smaller Num:"))


# The % operator returns the remainder of the division.
# if it is zero, i.e there is no remainder, then the first number is divided completely into second.

if largeInt % smallInt == 0:
    print("Divisible")
else:
    print('Not Divisible')
    print(f"Remainder:{largeInt % smallInt}")
    
    