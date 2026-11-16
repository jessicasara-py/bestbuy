import products
import store


# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)


def start(best_buy):

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

        # Option 1: List all products
        if choice == "1":

            active_products = best_buy.get_all_products()

            if not active_products:
                print("No active products available.")
            else:
                for product in active_products:
                    product.show()

        # Option 2: Show total quantity
        elif choice == "2":

            print(
                f"Total quantity in store: "
                f"{best_buy.get_total_quantity()}"
            )

        # Option 3: Make an order
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

                # Empty input finishes the order
                if not product_input:
                    break

                # Check if input is a valid number
                try:
                    product_number = int(product_input)
                except ValueError:
                    print("Please enter a valid product number!")
                    continue

                # Check if product number exists
                if product_number < 1 or product_number > len(active_products):
                    print("Invalid product number. Please try again.")
                    continue

                selected_product = active_products[product_number - 1]

                # Ask for quantity
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

            # Process order
            if not shopping_list:
                print("No products selected. Order cancelled.")
                continue

            try:
                total_price = best_buy.order(shopping_list)

                print("********")
                print(
                    f"Order made! Total payment: ${total_price:g}"
                )

            except Exception as e:
                print(f"Order could not be completed: {e}")

        # Option 4: Quit
        elif choice == "4":

            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    start(best_buy)
