"""This module contains the Product class."""


class Product:
    """Represent a product available for purchase."""

    def __init__(self, name, price, quantity):
        """Initialize a product with a name, price, and quantity."""
        if not name:
            raise ValueError("Product name cannot be empty")

        if price < 0:
            raise ValueError("Product price cannot be negative")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self):
        """Return the current product quantity."""
        return int(self.quantity)

    def set_quantity(self, quantity):
        """Update the product quantity and its active status."""
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.quantity = quantity
        self.active = quantity > 0

    def is_active(self):
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print the product's name, price, and quantity."""
        print(
            f"{self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )

    def buy(self, quantity):
        """Purchase a given quantity and return the total price."""
        if not self.active:
            raise ValueError("Product is not active")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if quantity > self.quantity:
            raise ValueError("Not enough products in stock")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return float(total_price)


def main():
    """Run a simple demonstration of the Product class."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
