# Implement assert to check wether a number is prime or not if the number is prime it should disply that the entered is prime otherwise it should throw an error and display that the entered number is not prime use exception handling 

def check_prime(num):
    assert num > 1, "Number must be greater than 1."

    for i in range(2, int(num**0.5) + 1):
        assert num % i != 0, "Number is NOT Prime"

    return "Number is Prime"

num = int(input("Enter a number: "))

try:
    print(check_prime(num))
except AssertionError as e:
    print("Error:", e)

