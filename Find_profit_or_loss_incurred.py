#11) Input the Cost Price and Selling Price of a product and find the profit or loss incurred
cost_price = int(input("Enter cost of product: "))
selling_price = int(input("Enter selling price of product: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("The profit is:",profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("The loss is:",loss)
else:
    print("No profit No loss") # Since the cot price is equal to selling price.
