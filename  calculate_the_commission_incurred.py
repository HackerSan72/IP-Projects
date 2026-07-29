# 14) Write a program to calculate the commission incurred 
# by a salesman based on the following criteria: 

sales = int(input("Enter the sales:"))
if sales >= 500000:
    rate = 0.20
elif 400000 <= sales <= 499999:
    rate = 0.15
elif 300000 <= sales <= 399999:
    rate = 0.10
else:
    rate = 0.05
        
commission = sales * rate
print("Your commision is:",commission)