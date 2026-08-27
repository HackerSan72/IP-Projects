# 21) Input a number and find the sum of digits of that number using ‘while’ loop.
num = int(input("Enter a number"))
sum = 0
temp = num
while temp > 0:
    remainder = temp % 10
    sum += remainder
    temp = temp // 10
print("The sum of digits is:",sum)
    