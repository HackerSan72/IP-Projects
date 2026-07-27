#4) Input the values of x, y and z, and calculate the expression : 4𝑥
#4x^4 + 3𝑦^3 + 9𝑧 + 6𝜋. (Use math module)

import math
x = (float(input("Enter a number: ")))
y = (float(input("Enter a number: ")))
z = (float(input("Enter a number: ")))

result = 4 * math.pow(x,4) + 3 * math.pow(y,3) + 9*z + 6 * math.pi
print(result)