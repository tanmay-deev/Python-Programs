
# Write python program to implement recursion display sum of n numbers 

def sum(n):
    if n == 1:
        return 1
    else:
        return (n + sum(n -1 ))
    
num = int(input("Enter an number: "))
print("The sum of number ", num, " is", sum(num))