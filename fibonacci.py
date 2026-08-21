# 20) Write a program to print the Fibonacci series of n numbers where
#  ‘n’ is entered by the user using ‘for’ loop

n = int(input("Enter the no. of terms:"))
a = 0
b = 1
print(a)
print(b)
for i in range(n-2):
    c = a + b
    a = b
    b = c
    print(c)
