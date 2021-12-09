from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    _DEFAULT_INITIAL_CAPACITY = 25

    def __init__(self, name):
        super().__init__(name, self._DEFAULT_INITIAL_CAPACITY)
