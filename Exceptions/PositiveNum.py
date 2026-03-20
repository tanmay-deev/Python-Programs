
# write python program to implement try, except, else and assert check wether the entered number is positive or not and display accordingly 

try:
    num = int(input("Enter a number: "))
    assert num > 0
except:
    print("The entered number is negative or zero")
else:
    print("The entered number is positive")