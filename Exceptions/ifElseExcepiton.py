try:
    num = int(input("Enter a number: "))
    assert num % 2 == 1
except:
    print("The entered number is even")