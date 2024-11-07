number = int(input("enter the number: "))
for i in range(number):
    if i == number-1:
        print("breaking the loop")
        break
    else:
        print(i)
print("the loop is broken")