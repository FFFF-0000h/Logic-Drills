# Collect input
a = input("Enter num:")

# Convert to float 
a = float(a)

# The % operator returns the residue
# of the division.
# Even numbers are completely divisible by 2.
# i.e remainder == 0
#  Odd numbers have a residue equal to 1.

# if remainder of division == 0

if a%2 == 0:
    # num is even
    print("Even Number")
else:
    print("Odd Number")    
    