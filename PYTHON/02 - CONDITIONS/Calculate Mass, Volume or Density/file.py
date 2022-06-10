result = 0
# user chooses the parameter he wants calculate, mass(m), volume(v) or density(d)

flag = input("what do you wanna calculate? (m,d,v): ")

# if the mass is chosen, then you must ask for density and volume.
# Calculate mass by the formula m = d * v
if flag == "m":
    d = float(input("enter density:"))
    v = float(input("enter volume:"))
    result = d * v
    
# if the volume is chosen, then you must ask for density and mass.
# Calculate volume by the formula v = d * m
if flag == "v":
    d = float(input("enter density:"))
    m = float(input("enter mass:"))
    result = d * m
    
# if the density is chosen, then you must ask for mass and volume.
# Calculate density by the formula d =  m/v    
if flag == "d":
    m = float(input("enter mass:"))
    v = float(input("enter volume:"))
    result = m / v
print(f"{flag} = {result}")    