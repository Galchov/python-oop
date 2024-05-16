from project.product import Product


class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name, price)
        self.milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters

    @milliliters.setter
    def milliliters(self, value):
        if value <= 0:
            raise ValueError("The milliliters cannot be less than or equal to zero!")
        self.__milliliters = value
