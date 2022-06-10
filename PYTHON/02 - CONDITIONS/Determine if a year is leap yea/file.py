# Enter the year you want to check

year = int(input("Enter year: "))

if year % 4 != 0:
    print("Year:Normal year")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Year:Leap year")    
else:
    print(
        "Year:Leap yaear"
    )        