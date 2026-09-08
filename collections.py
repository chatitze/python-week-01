shopping_list =["milk", "bread", "eggs", "coffee", "apples"]

item_to_add = input("Enter an item to add: ").strip().lower()
shopping_list.append(item_to_add)

item_to_remove = input("Enter an item to remove: ").strip().lower()

if item_to_remove not in shopping_list:
    print(f"{item_to_remove} is not in your shopping list")
else: 
    shopping_list.remove(item_to_remove)

print(f"There are {len(shopping_list)} items in your shopping list.")

for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")

