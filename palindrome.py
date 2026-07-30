# 25) Input a string and check whether it is palindrome or not using ‘for’ loop
s = input("Enter a string: ")
p = ''
for i in range(len(s) - 1,-1,-1):
    p += s[i]
if p == s:
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")