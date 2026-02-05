def display(age):
    return(age)

finalAge = display(22)

print(finalAge)

def sum(n1 =4, n2 =5):
    res = n1 + n2
    print("the addition of two numbers is: ", res)

sum(23, 67)

sum(45)

sum()

# use of keywork arguments
# def dispaly(fName, lName):
#     print("first name is: ", fName)
#     print("last name is: ", lName)

# display(fName = 'ajmal', lName = 'Kasab')

# use of arbitary arguments, program to fin sum of multiple
def add(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Addition: ", result)

# function call with 3 argunments
add(11, 22, 3)


