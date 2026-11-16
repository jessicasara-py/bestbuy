"""This module provides the user interface for the BestBuy store."""

import products
import store


def display_products(active_products):
    """Display all active products with their numbers."""
    for index, product in enumerate(active_products, start=1):
        print(
            f"{index}. {product.name}, "
            f"Price: ${product.price}, "
            f"Quantity: {product.get_quantity()}"
        )


def select_product(active_products):
    """Ask the user to select a product and return it."""
    while True:
        product_input = input(
            "Which product # do you want? "
        ).strip()

        if not product_input:
            return None

        try:
            product_number = int(product_input)
        except ValueError:
            print("Please enter a valid product number!")
            continue

        if not 1 <= product_number <= len(active_products):
            print("Invalid product number. Please try again.")
            continue

        return active_products[product_number - 1]


def get_quantity(selected_product):
    """Ask for a quantity and validate the requested amount."""
    quantity_input = input("What amount do you want? ").strip()

    if not quantity_input:
        print("Quantity cannot be empty. Please try again.")
        return None

    try:
        quantity = int(quantity_input)
    except ValueError:
        print("Please enter a valid whole number!")
        return None

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return None

    if quantity > selected_product.get_quantity():
        print(
            f"Not enough stock! Available: "
            f"{selected_product.get_quantity()}"
        )
        return None

    return quantity


def collect_shopping_list(active_products):
    """Collect products and quantities selected by the user."""
    shopping_list = []

    while True:
        selected_product = select_product(active_products)

        if selected_product is None:
            break

        quantity = get_quantity(selected_product)

        if quantity is None:
            continue

        shopping_list.append((selected_product, quantity))
        print("Product added to list!\n")

    return shopping_list


def make_order(best_buy):
    """Create and process an order."""
    active_products = best_buy.get_all_products()

    if not active_products:
        print("No products available for order.")
        return

    print("------")
    display_products(active_products)
    print("------")
    print("When you want to finish order, enter empty text.")

    shopping_list = collect_shopping_list(active_products)

    if not shopping_list:
        print("No products selected. Order cancelled.")
        return

    try:
        total_price = best_buy.order(shopping_list)

        print("********")
        print(f"Order made! Total payment: ${total_price:g}")

    except ValueError as error:
        print(f"Order could not be completed: {error}")


def start(best_buy):
    """Start the store menu and handle user interactions."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if not choice:
            print("Input cannot be empty. Please try again.")

        elif choice == "1":
            active_products = best_buy.get_all_products()

            if not active_products:
                print("No active products available.")
            else:
                display_products(active_products)

        elif choice == "2":
            print(
                f"Total quantity in store: "
                f"{best_buy.get_total_quantity()}"
            )

        elif choice == "3":
            make_order(best_buy)

        elif choice == "4":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")


def main():
    """Initialize the store and start the user interface."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product(
            "Bose QuietComfort Earbuds",
            price=250,
            quantity=500
        ),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
