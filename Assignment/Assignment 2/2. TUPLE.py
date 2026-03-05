my_tuple = ()

while True:
    print("\n--- TUPLE MENU ---")
    print("1. Create Tuple")
    print("2. Count Element")
    print("3. Find Index")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        elements = input("Enter elements separated by comma: ")
        my_tuple = tuple(elements.split(","))

    elif choice == 2:
        element = input("Enter element to count: ")
        print("Count:", my_tuple.count(element))

    elif choice == 3:
        element = input("Enter element to find index: ")
        print("Index:", my_tuple.index(element))

    elif choice == 4:
        print("Tuple:", my_tuple)

    elif choice == 5:
        break

    else:
        print("Invalid choice")