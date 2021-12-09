from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    _DEFAULT_INITIAL_SIZE = 3
    _DEFAULT_AQUARIUM = 'FreshwaterAquarium'

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self._DEFAULT_INITIAL_SIZE, price)

    @classmethod
    def eat(cls):
        cls._DEFAULT_INITIAL_SIZE += 3
