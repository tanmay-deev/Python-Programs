num1 = 5
num2 = 10.5
print("The type is", type(num1))

print("The value of num1 is {} and num2 is {}" .format(num1, num2))

num3 = int(input("Please enter the value "))
print(type(num3))

num11, num12, num13 = 10, 11, 12
print("The vlues of multiple variables are: ")
print(num11, num12, num13)

number1 = 5
number2 = 5
print("The addition of two number is: ", number1 + number2)

compl = 6 + 9j
print("The complex literal is: ", compl)

ch= "d"
print("The character is: ", ch, type(ch))

setflag = True
if setflag:
    print("Hello everyone!!")
    print("Solve the assignments")

setflag = False
if setflag:
    print("Good afternoon everyone!!")
    print("sovle the assignments")
print("Executed false")


no=3
if no < 5:
    print("number is less than 5")

no = int(input("Enter the number: "))

if no % 2 == 0:
    print("number is even")
else:
    print("number is odd")

no = 3
if no > 0:
    print("number is positive")
elif no <0:
    print("number is negative")
else:
    print("number is zero")