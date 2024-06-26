from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float) -> None:
        super().__init__(name, price=Coffee.PRICE, milliliters=Coffee.MILLILITERS)
        self.caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        if value <= 0:
            raise ValueError("The caffeine cannot be less than or equal to zero!")
        self.__caffeine = value
