integer = int(input("enter the integer: "))
if integer%2==0 and integer%3==0:
    print("divisible by both")
elif integer%2==0 :
    print("divisible by 2")
elif integer%3==0:
    print("divisible by 3")
else:
    print("not divisible by both")