#Input the Principal amount, rate of interest and time, and calculate the Simple Interest and 
#total amount to be paid by a person.

P = int(input("Enter the principal amount:"))
R = int(input("Enter the rate of interest:"))
T = int(input("Enter the time in years:"))
SI = (P*R*T)/100
total = P + SI
print("This is your simple interest", SI , "and this is your total", total)
