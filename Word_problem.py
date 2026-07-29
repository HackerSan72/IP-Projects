# 15) A store charges Rs. 120 per item if you buy less than or equal to  10 items. If you buy 
# between 10 and 99 items, the cost isRs. 100 per item. If you buy 100 or more items, the 
# cost is Rs. 70  per item. Write a program that asks the userhow many items they are buying 
# and prints the total cost.

items = int(input("Enter the total no. of items to be bought: "))
cost = 1
if items <= 10:
    cost = items * 120
elif items > 10 and items <= 99:
    cost = items * 100
    #print(cost)
elif items >= 100:
    cost = items * 70
else:
    print("Invalid input!")

print("The total cost is Rs.",cost) 
