
def calculate_price(price, quantity=1, discount=0):
    return price * quantity - discount

def print_receipt(price, quantity=1, discount=0):
    receipt = calculate_price(price, quantity, discount)
    print(f"Total: €{receipt}")

print_receipt(10, 3, 5)


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
    

number = get_positive_integer("How many? ")
print(f"You entered: {number}")