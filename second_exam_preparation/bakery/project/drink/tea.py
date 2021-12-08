from project.drink.drink import Drink


class Tea(Drink):
    __DEFAULT_TEA_PRICE = 2.50

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name, portion, self.__DEFAULT_TEA_PRICE, brand)
