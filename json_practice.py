import json

shopping_list = {
    "milk": 2,
    "bread": 1,
    "eggs": 12
}

with open("shopping_list.json", "w") as file:
    json.dump(shopping_list, file)


with open("shopping_list.json", "r") as file:
    loaded_list = json.load(file)

print(loaded_list)
print(type(loaded_list))
