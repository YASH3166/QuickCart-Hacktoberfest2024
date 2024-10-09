# Shopping List Application

shopping_list = []

def show_menu():
    print("\n--- Shopping List Menu ---")
    print("1. Show current list")
    print("2. Add item to list")
    print("3. Remove item from list")
    print("4. Exit")

def show_list():
    if shopping_list:
        print("\nYour shopping list:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("\nYour shopping list is empty.")

def add_item():
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"{item} has been added to the list.")
    else:
        print("Item cannot be empty.")

def remove_item():
    if shopping_list:
        show_list()
        try:
            item_num = int(input("Enter the number of the item to remove: "))
            if 1 <= item_num <= len(shopping_list):
                removed_item = shopping_list.pop(item_num - 1)
                print(f"{removed_item} has been removed from the list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Your shopping list is empty, nothing to remove.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            show_list()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
