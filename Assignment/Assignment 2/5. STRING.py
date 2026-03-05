my_string = ""

while True:
    print("\n--- STRING MENU ---")
    print("1. Enter String")
    print("2. Uppercase")
    print("3. Lowercase")
    print("4. Replace")
    print("5. Find")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        my_string = input("Enter string: ")

    elif choice == 2:
        print("Uppercase:", my_string.upper())

    elif choice == 3:
        print("Lowercase:", my_string.lower())

    elif choice == 4:
        old = input("Enter word to replace: ")
        new = input("Enter new word: ")
        print("Updated:", my_string.replace(old, new))

    elif choice == 5:
        word = input("Enter word to find: ")
        print("Index:", my_string.find(word))

    elif choice == 6:
        print("String:", my_string)

    elif choice == 7:
        break

    else:
        print("Invalid choice")