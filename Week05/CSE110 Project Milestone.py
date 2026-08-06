# Shopping Cart Program

cart = []

while True:
    print("\n1. Add item")
    print("2. Show cart")
    print("3. Quit")

    choice = input("Pick a number: ")

    if choice == "1":
        item = input("Type the item name: ")
        cart.append(item)
        print(f"Added '{item}' to your cart.")

    elif choice == "2":
        if cart:
            print("Your cart:")
            for item in cart:
                print(f"- {item}")
        else:
            print("Your cart is empty.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Please choose a valid option.")