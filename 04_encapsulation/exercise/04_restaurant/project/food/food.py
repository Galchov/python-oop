from project.product import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float) -> None:
        super().__init__(name, price)
        self.grams = grams

    @property
    def grams(self):
        return self.__grams

    @grams.setter
    def grams(self, value):
        if value <= 0:
            raise ValueError("The grams cannot be less than or equal to zero!")
        self.__grams = value
