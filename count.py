# 4) Input the age of ‘n’ employees and count the number 
# of people in the following age group using ‘while’ loop
n = int(input("Enter no. of employees:"))
c1 = 0
c2 = 0
c3 = 0 
i = 1
while i < n+1:
    age = int(input("Enter age:"))
    if age > 25 and age < 36:
        c1 += 1
    elif age > 35 and age < 46:
        c2 += 2
    elif age > 45 and age < 56:
        c3 += 1
    else:
        print("Invalid input!")
    i += 1
print("The no. of people in the age group 26-35 is",c1)
print("The no. of people in the age group 36-45 is",c2)
print("The no. of people in the age group 46-55 is",c3)
