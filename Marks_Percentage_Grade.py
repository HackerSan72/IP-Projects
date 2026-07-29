# 13) Input the student’s name, class, roll number and marks in 5 subjects.
#  Compute the total marks, percentage and grade as per the following table.

name = input("Enter your name: ")
Class = input("Enter your class and section: ")
roll_no = int(input("Enter your roll no.: "))
m = int(input("Enter marks of maths out of 100 : "))
p = int(input("Enter marks of physics out of 100: "))
c = int(input("Enter marks of chemistry out of 100: "))
ip = int(input("Enter marks of IP out of 100: "))
e = int(input("Enter marks of english out of 100: ")) 
total =   m + p + c + ip + e
percentage = (m+p+c+ip+e)/500 *100

print(name)
print(Class)
print(roll_no)
print("The percentage is:",percentage)
print("The total marks obtained are:",total)


if total >= 90:
    print("Your grade is A")
elif total >= 70 and total < 90:
    print("Your grade is B")
elif total >= 50 and total < 70:
    print("Your grade is C")
elif total >= 40 and total < 50:
    print("Your grade is D")
elif total <40:
    print("Your grade is E")
else:
    print("Your grade is F")
