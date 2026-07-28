#9) Input an alphabet and find whether it is in uppercase or lowercase
a = int(input("Enter an alphabet: "))
if a == 'ABCDEFGHIJKLMNOPQRSTUVwXYZ':
    print(a ,"is an uppercase letter")
elif a == 'abcdefghijklmnopqrstuvwxyz':
    print(a,"is an lowercase letter")
else:
    print("Unexpected input!")