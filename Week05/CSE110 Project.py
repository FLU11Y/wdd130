def add_item(cart):
    name = input("Enter the item name: ").strip()
    if not name:
        print("Item name cannot be empty.")
        return

    try:
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price per item: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    cart.append({"name": name, "quantity": quantity, "price": price})
    print(f"Added {quantity} {name}(s) to the shopping cart.")


def display_cart(cart):
    if not cart:
        print("Your shopping cart is empty.")
        return

    print("\nShopping Cart:")
    for item in cart:
        print(f"- {item['name']}: {item['quantity']} x ${item['price']:.2f}")


def remove_item(cart):
    if not cart:
        print("Your shopping cart is empty.")
        return

    name = input("Enter the item name to remove: ").strip().lower()
    for item in cart:
        if item["name"].lower() == name:
            cart.remove(item)
            print(f"Removed {item['name']} from the shopping cart.")
            return

    print("Item not found in the shopping cart.")


def compute_total(cart):
    total = 0
    for item in cart:
        total += item["quantity"] * item["price"]
    print(f"Total: ${total:.2f}")


shopping_cart = []

while True:
    print("\n1. Add a new item")
    print("2. Display the shopping cart")
    print("3. Remove an item")
    print("4. Compute the total")
    print("5. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_item(shopping_cart)
    elif choice == "2":
        display_cart(shopping_cart)
    elif choice == "3":
        remove_item(shopping_cart)
    elif choice == "4":
        compute_total(shopping_cart)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")