class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("The price cannot be less than or equal to zero!")
        self.__price = value
