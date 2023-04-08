class Item:
    all = []
    discount_percentage = 0.27

    def __init__(self, name, price: float, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

        if not isinstance(quantity, int):
            raise TypeError("Quantity should be an integer")
        assert quantity > 0, "Quantity should be greater than 0"

        if not isinstance(price, (int, float)):
            raise TypeError("Price should be a float or an integer")

        Item.all.append(self)

    def __str__(self) -> str:
        return str(
            self.__dict__
        )  # you need to convert to a string format otherwise it will raise an error

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        )

    def calculateTotalPrice(
        self, discount_percentage: float = discount_percentage
    ) -> float:
        return (self.price * self.quantity) - self.price * discount_percentage

    @classmethod
    def sortBasedOnQuantity(cls, li):
        return sorted(li, reverse=True, key=lambda x: x.quantity)

    def __connectToPrivateServer():
        print(f"Connecting to private server")

    # __connectToPrivateServer()


# item1 = Item()
# item1.name = "Phone"
# item1.price = 19999
# item1.quantity = 2

# item1 = Item("Phone", 19999, 0)
# The above raises "AssertionError: Quantity should be greater than 0"

# item1 = Item("Phone", 19999, 20.2)
# The above raise "TypeError: Quantity should be an integer"

# item1 = Item("Phone", 19999, 20)
# item2 = Item("Phone", 18500, 10)

# print(item1)
# print("Total Price after discount :", item1.calculateTotalPrice())

# print(Item.sortBasedOnQuantity([item1, item2]))

# Item.__connectToPrivateServer()
