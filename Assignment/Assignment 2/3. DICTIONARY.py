my_dict = {}

while True:
    print("\n--- DICTIONARY MENU ---")
    print("1. Add Key-Value")
    print("2. Remove Key")
    print("3. Get Value")
    print("4. Display Keys")
    print("5. Display Values")
    print("6. Display Dictionary")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value

    elif choice == 2:
        key = input("Enter key to remove: ")
        my_dict.pop(key)

    elif choice == 3:
        key = input("Enter key to get value: ")
        print("Value:", my_dict.get(key))

    elif choice == 4:
        print("Keys:", my_dict.keys())

    elif choice == 5:
        print("Values:", my_dict.values())

    elif choice == 6:
        print("Dictionary:", my_dict)

    elif choice == 7:
        break

    else:
        print("Invalid choice")