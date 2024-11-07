num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))
operator = input("enter operator + - / *: ")
if operator == '+':
    print("the sum of two number is ", num1+num2)
elif operator == '-':
    print("the difference of two number is ", num1-num2)
elif operator == '/':
    print("the division of two number is ", num1/num2)
if operator == '*':
    print("the multiple of two number is ", num1*num2)