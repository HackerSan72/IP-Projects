# 19) Input ‘n’ numbers and display the largest and smallest number at the end using ‘for’ loop.
n = int(input("Enter number of elemnts:"))
num = int(input("Enter a number: "))
a = num
b = num 
for i in range(n-1):
    num = int(input("Enter a number: "))
    if num > a:
        a = num
    else:
        b = num
print(a,b) 