# 18) Input a number and calculate its factorial using ‘while’ loop.
num = int(input("Enter a number: "))
f = 1
i = 1
if num < 0:
    print("Invalid Input") # Factorial doesn't exist for negative numbers.
elif num == 0:
    print("The factorial is 1")
else:
    while i <= num:
        f *= i
        i += 1
    print("The factorial is", f)