from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []  # Contains 'Decoration' objects
        self.fish = []  # Contains 'Fish' object

    @staticmethod
    def __validate_name(value):
        if value == '':
            raise ValueError('Aquarium name cannot be an empty string.')
        return value

    def calculate_comfort(self):
        return sum(x._DEFAULT_COMFORT for x in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'

        self.fish.append(fish)
        return f'Successfully added {fish.__name__} to {self.name}.'

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        if not self.fish:
            return 'none'

        return f'''"{self.name}:
Fish: {[x.__name__ for x in self.fish]}
Decorations: {len(self.decorations)}
Comfort: {self.calculate_comfort()}"'''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value
