from project.drink.drink import Drink


class Water(Drink):
    __DEFAULT_WATER_PRICE = 1.50

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name, portion, self.__DEFAULT_WATER_PRICE, brand)
