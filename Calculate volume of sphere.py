#5) Input the radius of a sphere and calculate its volume. (Use math module)

import math

r = int(input("Enter radius of sphere:"))
v = 4/3 * math.pi * math.pow(r,3)

print("The volume is: ",v)
