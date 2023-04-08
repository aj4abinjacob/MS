from item import Item


class Phone(Item):
    # all = Item.all

    def __init__(self, name, price: float, quantity, brand: str) -> None:
        super().__init__(name, price, quantity)
        self.brand = brand
        # Phone.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.brand})"
