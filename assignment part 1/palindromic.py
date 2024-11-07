string1 = str(input("enter the string: "))
string2 = string1[::-1]
if string1 == string2:
    print("string is palindromic")
else:
    print("string is not palindromic")