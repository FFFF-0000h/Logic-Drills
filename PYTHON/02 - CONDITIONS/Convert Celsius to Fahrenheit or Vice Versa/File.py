# input nC or nF is expected where  is an integer.
a = input("Enter numF or numC:")

# the last symbol is collected
sign = a[-1]

# conversion into an integer
a = int(a)

# if the sign denotes Celsius,
if sign == "c" or sign == "C":
    
    # converting to Fahrenheit
    a = (a*9/5) + 32
    
    # rounding off to an integer
    a = int(a)
    print(f"{a}C")
 
# if the sign denotes fahrenheit   
elif sign == "f" or sign == "F":
    
    # converting to Fahrenheit
    a = (a - 32) * 5/9
    
    # rounding off to an integer
    a = int(a)
    print(f"{a}F")

