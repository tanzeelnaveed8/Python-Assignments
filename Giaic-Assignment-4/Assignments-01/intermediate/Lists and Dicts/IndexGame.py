def access_element(my_list, index):
    try:
        return f"Element at index {index}: {my_list[index]}"
    except IndexError:
        return "Error: Index is out of range."

def modify_element(my_list, index, new_value):
    try:
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}'"
    except IndexError:
        return "Error: Index is out of range."

def slice_list(my_list, start, end):
    # Safely slice the list
    return my_list[start:end]

def index_game():
    my_list = ['dog', 'cat', 'parrot', 'hamster', 'turtle']
    print("\nWelcome to the Index Game!")
    print("Initial list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print(access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))
            print("Updated list:", my_list)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            sliced = slice_list(my_list, start, end)
            print("Sliced list:", sliced)

        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, please try again.")

index_game()
