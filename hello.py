name = input("What's your name? ")

print(f"\nHello {name}!")

while True:
    try:
        age  = int(input("How old are you? "))

        if 0 <= age < 18:
            years_until_18 = 18 - age
            print(f"You will be 18 in {years_until_18} years.")
            break

        elif age == 18 :
            print(f"You are already 18 years old!")
            break
            
        elif 18 < age <= 120 :
            print("You are older than 18.")
            break

        else :
            print("Please enter a value between 0 and 120.")

    except ValueError:
        print("Please enter your age as a number.")


