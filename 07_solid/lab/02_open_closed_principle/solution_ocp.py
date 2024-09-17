"""
Here's completely refactored 'Animal' class, turning it into an abstract base class.

The class provides the required interface for any animal that you'd like to define.
The interface consist of '.name' attribute and '.make_sound()' method that
all the subclasses must override, which will create individual functionality for
each of them.

Open-Closed Principle -> Software entities (classes, modules, functions, etc.)
should be open for extension, but closed for modification.
"""


from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Chicken(Animal):
    def make_sound(self):
        return "cluck-cluck"


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat("Tom"), Dog("Beethoven"), Chicken("Chick")]
animal_sound(animals)
