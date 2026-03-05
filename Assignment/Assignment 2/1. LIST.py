my_list = []

while True:
    print("\n--- LIST MENU ---")
    print("1. Append")
    print("2. Insert")
    print("3. Remove")
    print("4. Pop")
    print("5. Sort")
    print("6. Reverse")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to append: ")
        my_list.append(element)

    elif choice == 2:
        pos = int(input("Enter position: "))
        element = input("Enter element: ")
        my_list.insert(pos, element)

    elif choice == 3:
        element = input("Enter element to remove: ")
        my_list.remove(element)

    elif choice == 4:
        my_list.pop()

    elif choice == 5:
        my_list.sort()

    elif choice == 6:
        my_list.reverse()

    elif choice == 7:
        print("List:", my_list)

    elif choice == 8:
        break

    else:
        print("Invalid choice")