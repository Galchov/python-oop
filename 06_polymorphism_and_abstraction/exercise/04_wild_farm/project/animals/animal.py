from abc import ABC, abstractmethod
from typing import List, Type

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0

    @property
    @abstractmethod
    def preferred_food(self) -> List[Type[Food]]:
        pass

    @property
    @abstractmethod
    def weight_gaining(self) -> float:
        pass

    @staticmethod
    @abstractmethod
    def make_sound() -> None:
        pass

    def feed(self, food: Food) -> str or None:
        if type(food) not in self.preferred_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (food.quantity * self.weight_gaining)
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str) -> None:
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
