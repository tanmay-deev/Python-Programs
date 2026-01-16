list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 5.678, 9.1011, 7.1213, 8.98, 9.58, 6, 7, 3, 4, 5, 2, 1, 0, 4, 6]

for value in list:
    print(value)

print('replaced the 5th index value')
list[5] = 'REPLACED'
print(list)

print('sliced the array from index 7 to 10')
print(list[7:10])

print('append the int elements to the list')
list.append([5,7,3,5,9])
print(list)

print('deleted the 7th index')
del list[7]

print('full list deleted')
list.clear()
print(list)


#reverse list

list.reverse
print(list)