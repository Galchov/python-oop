from abc import ABC, abstractmethod


class BaseFish(ABC):
    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @staticmethod
    def __validate_name(value):
        if value.strip() == '':
            raise ValueError('Fish name cannot be an empty string.')
        return value

    @staticmethod
    def __validate_species(value):
        if value.strip() == '':
            raise ValueError('Fish species cannot be an empty string.')
        return value

    @staticmethod
    def __validate_price(value):
        if value <= 0:
            raise ValueError('Price cannot be equal to or below zero.')
        return value

    def eat(self):
        self.size += 5

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__validate_species(value)
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value
