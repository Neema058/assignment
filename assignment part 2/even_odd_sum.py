limit = int(input("Enter the limit: "))

even_sum = 0
odd_sum = 0

for num in range(1, limit + 1):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)