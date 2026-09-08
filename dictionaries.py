shopping_list = {
    "milk": 2,
    "bread": 1,
    "eggs": 12
}

shopping_list["apples"] = 6
shopping_list["milk"] = 3

del shopping_list["bread"]

item_to_add = input("What item would you like to add? ").strip().lower()

while True:
    try:
        quantity_to_add = int(input("How many? "))
        if quantity_to_add <= 0:
            print("Please enter a quantity greater than 0.")
        else:
            break

    except ValueError:
        print("Please enter the quantity as a number.")

if item_to_add in shopping_list:
    shopping_list[item_to_add] += quantity_to_add
else:
    shopping_list[item_to_add] = quantity_to_add

for item, quantity in shopping_list.items():
    print(f"{item}: {quantity}")

item_to_remove = input("What item would you like to remove? ").strip().lower()

if item_to_remove in shopping_list:
    del shopping_list[item_to_remove]
else:
    print(f"{item_to_remove} is not in your shopping list")

for item, quantity in shopping_list.items():
    print(f"{item}: {quantity}")