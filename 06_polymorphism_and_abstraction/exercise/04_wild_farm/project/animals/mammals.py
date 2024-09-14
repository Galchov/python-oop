from typing import List, Type

from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Food


class Mouse(Mammal):
    @property
    def preferred_food(self) -> List[Type[Food]]:
        return [Vegetable, Fruit]

    @property
    def weight_gaining(self) -> float:
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):
    @property
    def preferred_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gaining(self) -> float:
        return 0.40

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):
    @property
    def preferred_food(self) -> List[Type[Food]]:
        return [Vegetable, Meat]

    @property
    def weight_gaining(self) -> float:
        return 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):
    @property
    def preferred_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gaining(self) -> float:
        return 1.00

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
