import json

def save_items(items_list):
    with open("shopping_list.json", "w") as file:
        json.dump(items_list, file)

def load_items():
    try:
        with open("shopping_list.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def view_items(items_list):
    print("\nYour shopping list:")

    for item, quantity in items_list.items():
        print(f"{item}: {quantity}")

def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Please enter a number greater than 0.")
            else:
                return number
        except ValueError:
            print("Please enter a number.")

def add_item(items_list):
    item_to_add = input("What item would you like to add? ").strip().lower()

    quantity_to_add = get_positive_integer("How many? ")

    if item_to_add in items_list:
        items_list[item_to_add] += quantity_to_add
    else:
        items_list[item_to_add] = quantity_to_add

    save_items(items_list)
    print(f"Added {quantity_to_add} {item_to_add}.")


def remove_item(items_list):
    item_to_remove = input("What item would you like to remove? ").strip().lower()

    if item_to_remove in items_list:
        del items_list[item_to_remove]
        save_items(items_list)
        print(f"Removed {item_to_remove}.")

    else:
        print(f"{item_to_remove} is not in your shopping list.")
    
def main():

    shopping_list = load_items() 

    while True:
        option = input("""
        --- Shopping List ---

        1. View items
        2. Add item
        3. Remove item
        4. Exit

        Choose an option: """)
        if option == "1":
            view_items(shopping_list)

        elif option == "2":
            add_item(shopping_list)
                
        elif option == "3":
            remove_item(shopping_list)

        elif option == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
