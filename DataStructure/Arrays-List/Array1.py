#Data structues in python
# 1. List

list_ds = [] # Creating an empty list
print(list_ds)
list_ds = [5, 6, 7, 'list-data', 5.555] # Creating a list with elements
print(list_ds)

# list_ds = [5, 6, 7]
# print(list_ds)
# list_ds.append([123, 45])
# print(list_ds)
# list_ds.extend([567, 'example-extend'])
# print(list_ds)
# list_ds.insert(5, 'example-of-insert-func')
# print(list_ds)

for value in list_ds:
    print(value)

print(list_ds[0:3]) # Slicing the list
print(list_ds[::-1]) # Reversing the list using slicing


#Deleting elements forn the lsit
del list_ds[2] # Deleting element at index 2
print(list_ds)
list_ds.remove('list-data') # Removing element by value
print(list_ds)
popped = list_ds.pop(1) # Popping element at index 1
print('popped value: ', popped, 'Remanining elements: ', list_ds)
list_ds.clear() # Clearing the entire list
print(list_ds)