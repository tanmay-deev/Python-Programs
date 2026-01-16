num = int(input("Enter the number"))


if(num > 0):
    last_digit = num % 10
else:
    print("Invalid Number")

if(last_digit % 5 == 0 ):
    print("divisible")
else:
    print("not divisible")
