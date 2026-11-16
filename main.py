"""This module provides the user interface for the BestBuy store."""

import products
import store


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
            continue

        if choice == "1":
            active_products = best_buy.get_all_products()

            if not active_products:
                print("No active products available.")
            else:
                for product in active_products:
                    product.show()

        elif choice == "2":
            print(
                f"Total quantity in store: "
                f"{best_buy.get_total_quantity()}"
            )

        elif choice == "3":
            shopping_list = []
            active_products = best_buy.get_all_products()

            if not active_products:
                print("No products available for order.")
                continue

            print("------")

            for index, product in enumerate(active_products, start=1):
                print(
                    f"{index}. {product.name}, "
                    f"Price: ${product.price}, "
                    f"Quantity: {product.get_quantity()}"
                )

            print("------")
            print("When you want to finish order, enter empty text.")

            while True:
                product_input = input(
                    "Which product # do you want? "
                ).strip()

                if not product_input:
                    break

                try:
                    product_number = int(product_input)
                except ValueError:
                    print("Please enter a valid product number!")
                    continue

                if not 1 <= product_number <= len(active_products):
                    print("Invalid product number. Please try again.")
                    continue

                selected_product = active_products[product_number - 1]

                quantity_input = input(
                    "What amount do you want? "
                ).strip()

                if not quantity_input:
                    print("Quantity cannot be empty. Please try again.")
                    continue

                try:
                    quantity = int(quantity_input)
                except ValueError:
                    print("Please enter a valid whole number!")
                    continue

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

                if quantity > selected_product.get_quantity():
                    print(
                        f"Not enough stock! Available: "
                        f"{selected_product.get_quantity()}"
                    )
                    continue

                shopping_list.append((selected_product, quantity))
                print("Product added to list!\n")

            if not shopping_list:
                print("No products selected. Order cancelled.")
                continue

            try:
                total_price = best_buy.order(shopping_list)

                print("********")
                print(f"Order made! Total payment: ${total_price:g}")

            except ValueError as error:
                print(f"Order could not be completed: {error}")

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
