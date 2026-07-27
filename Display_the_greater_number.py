#6) Input 2 numbers and find the greater number. 
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

if n1 > n2:
    print(n1,"is greater than", n2)
elif n1 == n2:
    print("Both numbers are equal")
else:
    print(n2,"is greater than", n1)