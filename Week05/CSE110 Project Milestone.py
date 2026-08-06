# Shopping Cart Program

shopping_cart = []

while True:
    print("\n1. Add a new item")
    print("2. Display the contents of the shopping cart")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter the item name: ")
        shopping_cart.append(item)
        print(f"Added '{item}' to the shopping cart.")

    elif choice == "2":
        if shopping_cart:
            print("Shopping cart contents:")
            for item in shopping_cart:
                print(f"- {item}")
        else:
            print("Your shopping cart is empty.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")