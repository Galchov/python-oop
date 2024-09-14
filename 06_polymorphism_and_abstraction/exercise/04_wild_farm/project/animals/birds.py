from typing import List, Type

from project.animals.animal import Bird
from project.food import Food, Vegetable, Meat, Seed, Fruit


class Owl(Bird):

    @property
    def preferred_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gaining(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def preferred_food(self) -> List[Type[Food]]:
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def weight_gaining(self) -> float:
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"
