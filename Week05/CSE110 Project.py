cart = []


def add_item(cart):
    name = input("Enter the item name: ").strip()
    if name == "":
        print("Please type an item name.")
        return

    try:
        quantity = int(input("How many do you want? "))
        price = float(input("What is the price for one item? "))
    except ValueError:
        print("Please enter a number.")
        return

    cart.append({"name": name, "quantity": quantity, "price": price})
    print(f"Added {quantity} {name}(s) to your cart.")


def show_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return

    print("\nYour cart:")
    for item in cart:
        print(f"- {item['name']}: {item['quantity']} x ${item['price']:.2f}")


def remove_item(cart):
    if not cart:
        print("Your cart is empty.")
        return

    name = input("Enter the item name to remove: ").strip().lower()
    for item in cart:
        if item["name"].lower() == name:
            cart.remove(item)
            print(f"Removed {item['name']} from your cart.")
            return

    print("That item is not in your cart.")


def show_total(cart):
    total = 0
    for item in cart:
        total += item["quantity"] * item["price"]
    print(f"Total price: ${total:.2f}")


while True:
    print("\n1. Add item")
    print("2. Show cart")
    print("3. Remove item")
    print("4. Show total")
    print("5. Quit")

    choice = input("Pick a number: ").strip()

    if choice == "1":
        add_item(cart)
    elif choice == "2":
        show_cart(cart)
    elif choice == "3":
        remove_item(cart)
    elif choice == "4":
        show_total(cart)
    elif choice == "5":
        print("Thank you. Goodbye!")
        break
    else:
        print("Please choose a valid option.")


