integer = int(input("enter digits: "))
sum=0
while integer!=0:
    last_digit=integer % 10
    sum+=last_digit    #try without using end
    integer=integer // 10
print(sum)

