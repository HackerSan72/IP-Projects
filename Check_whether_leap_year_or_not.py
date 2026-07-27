#8) Input the year and find whether it is a leap year or not. 

# A year is aleap year if it is perfectly disible by 4,
#  but not 100 unless it is also divisible by 400

y = int(input("Enter the year: "))

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(y,"is a leap year")
else:
    print(y,"is not a leap year")
    