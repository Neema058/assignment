digit = int(input("enter digits: "))
while digit!=0:
    last_digit=digit % 10
    print(last_digit, end="")  #try without using end
    digit=digit // 10

