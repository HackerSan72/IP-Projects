# 17) Write a program to print the table of an entered number using ‘while’ loop

num = int(input("Enter a number: "))
i = 1
result = 1
while i <= 10:
    result = num * i
    i += 1
    print(result)