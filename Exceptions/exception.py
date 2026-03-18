#Exception Handling in Python
try:
     num = 10
     denom = 0
     divresult = num/denom
     print(divresult)
except:
     print("Denominator cannot be 0")

# write python program to implement Exception handling for the following 

# a. Input a number from the user and check wether it is even or odd if it is odd then in the except block display the number is odd 
try:
     num = int(input("Enter a number: "))
     if num % 2 == 0:
         print("The number is even")
     else:
         raise ValueError("The number is odd")
except ValueError as e:
     print(e)