from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    _DEFAULT_INITIAL_SIZE = 5
    _DEFAULT_AQUARIUM = 'SaltwaterAquarium'

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self._DEFAULT_INITIAL_SIZE, price)

    @classmethod
    def eat(cls):
        cls._DEFAULT_INITIAL_SIZE += 2
