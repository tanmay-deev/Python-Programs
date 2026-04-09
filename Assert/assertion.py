# assert statement in python 

# syntax of assert statement
# assert <condition>, 
# assert<condition>, <error message>

# assertion without error

# def avg1(marks):
#     assert len(marks) != 0
#     return sum(marks) / len(marks)

# marks1 = []
# print("Average marks: ", avg1(marks1))

# assertion with error message

def avg2(marks):
    assert len(marks) != 0, "Marks list cannot be empty"
    return sum(marks) / len(marks)

marks2 = [75, 68, 46, 69]
print("Average marks: ", avg2(marks2))

# program to print the ni