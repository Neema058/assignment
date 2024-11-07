digit = int(input("enter digits: "))
count = 0
while digit!=0:
    digit=digit // 10
    count+=1
print(count)
    