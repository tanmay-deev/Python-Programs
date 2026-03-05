my_set = set()

while True:
    print("\n--- SET MENU ---")
    print("1. Add")
    print("2. Remove")
    print("3. Union")
    print("4. Intersection")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        element = input("Enter element to add: ")
        my_set.add(element)

    elif choice == 2:
        element = input("Enter element to remove: ")
        my_set.remove(element)

    elif choice == 3:
        other = set(input("Enter elements separated by comma: ").split(","))
        print("Union:", my_set.union(other))

    elif choice == 4:
        other = set(input("Enter elements separated by comma: ").split(","))
        print("Intersection:", my_set.intersection(other))

    elif choice == 5:
        print("Set:", my_set)

    elif choice == 6:
        break

    else:
        print("Invalid choice")