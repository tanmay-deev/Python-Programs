# write python program to modify a string Hello, world to Hello there and also display the string in reverse order

str1 = "Hello, world"
str2 = "Hello there"
print("Modified String:", str2)
print("Reversed String:", str2[::-1])

# reverse string Ex: I am Studing Python - reversed Python Studing am I
str_reverse = "I am Studing Python"
words = str_reverse.split()
words.reverse()
print("Reversed String:", " ".join(words))


# count number of vowels and consonants in a string
string = input("Enter an String: ")
vowels = "aeiouAEIOU"
Vcount = 0
Ccount = 0
for char in string:
    if char.isalpha():
        if char in vowels:
            Vcount += 1
        else:
            Ccount += 1
print("Number of Vowels:", Vcount)
print("Number of Consonants:", Ccount)

# input sitring and display in uppercase and lowercase

string = input("Enter a string: ")
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())

# create the following list [1, 4, 6, 7, 9] and perform the following operations 1) display firsst 3 element 2) display th elements excluding first and last 3) Display the last element 4) display in decending order

list = [1, 4, 6, 7, 9]
print("First 3 elements:", list[:3])
print("Elements excluding first and last:", list[1:4])
print("Last element:", list[-1])
list.sort(reverse=True)
print("List in descending order:", list)






