def prime(num):
    if num <= 1:
        print("Not a Prime number")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime number")
            return

    print("It is a Prime number")

number = int(input("Enter a number: "))
prime(number)