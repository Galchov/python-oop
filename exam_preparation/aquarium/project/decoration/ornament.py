from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    _DEFAULT_COMFORT = 1
    _DEFAULT_PRICE = 5.0

    def __init__(self):
        super().__init__(self._DEFAULT_COMFORT, self._DEFAULT_PRICE)
