num = int(input("enter number to find its fibonacci: "))
a, b = 0, 1

print("The first 10 Fibonacci numbers are:")

for _ in range(num):
    print(a, end=" ")
    a, b = b, a + b
