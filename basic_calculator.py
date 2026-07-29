# 12) Display the menu and create a basic calculator with
#  addition, subtraction, multiplication and division based on the choice of user.
print("MENU")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

    if choice.lower() == 'q':
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid selection. Please choose a valid operation.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")


