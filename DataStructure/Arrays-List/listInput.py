list1 = []
list2 = []

print("Enter 10 elements for List 1:")
for i in range(10):
    list1.append(input())

print("Enter 10 elements for List 2:")
for i in range(10):
    list2.append(input())

list3 = list1 + list2

print("List 1:", list1)
print("List 2:", list2)
print("Combined List (List 3):", list3)
