print("Enter the number to check")
number = int(input("The number you entered is: "))  # Convert input to an integer

if number == 0:
    print("The number is zero")
elif number < 0:  
    print("The number is negative")
else:
    print("The number is positive")
