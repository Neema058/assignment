string = input("enter the string to check: ")
if string.isupper():
    print("all are uppercase letters")
elif string.islower():
    print("all are lowercase letters")
else:
    print("mix case letters")