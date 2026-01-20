# tup = (2, "hii", 50.5, '@')
# tup[2] = 100 Cannot make changes here
# print(tup)

tuple = ()
type(tuple)

tuple = (1, 2, 3, 4, 5)
print(tuple)

tuple = (12)
type(tuple) # it is considered as int
print(tuple)

#Accessing tuple

tuple = (1, 2, 3, 4, 5, 'typle_example', 5.55)
print(tuple)

for t in tuple:
    print(t)

print(tuple[:])
# print(tuple[5] [4])

#Appending tuple

tuple = tuple + (23, 45, 67)
print(tuple)

