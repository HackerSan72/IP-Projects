#10) Input an alphabet and find whether it is a vowel or consonant. 

a = input("Enter an alphabet: ")
if a in "AEIOU" or a in "aeiou":
    print(a,"is vowel")
elif a in "BCDFGHJKLMNPQRSTVWXYZ" or a in "bcdfghjklmnpqrstuvwxyz":
    print(a,"is a consonent")
else:
    print("Unexpected input!")
    