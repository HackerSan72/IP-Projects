# 23) Program to find the sum of following series using ‘for’ loop:
#  1 +1/2+1/3+1/4+1/5+.......+1/n where n is entered by the user.

n = int(input("Enter number:"))
sum = 0
for i in range(1,n+1):
    sum += (1/i)
print(sum)