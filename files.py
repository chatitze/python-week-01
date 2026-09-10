
try:
    with open("missing.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found.")
else:
    print(content)