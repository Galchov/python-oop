from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    _DEFAULT_COMFORT = 5
    _DEFAULT_PRICE = 10.0

    def __init__(self):
        super().__init__(self._DEFAULT_COMFORT, self._DEFAULT_PRICE)
