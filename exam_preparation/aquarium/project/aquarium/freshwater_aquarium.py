from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    _DEFAULT_INITIAL_CAPACITY = 50

    def __init__(self, name):
        super().__init__(name, self._DEFAULT_INITIAL_CAPACITY)
