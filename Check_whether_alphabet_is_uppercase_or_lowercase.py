#9) Input an alphabet and find whether it is in uppercase or lowercase
a = input("Enter an alphabet: ")
if a in 'ABCDEFGHIJKLMNOPQRSTUVwXYZ':
    print(a ,"is an uppercase letter")
elif a in 'abcdefghijklmnopqrstuvwxyz':
    print(a,"is an lowercase letter")
else:
    print("Unexpected input!")