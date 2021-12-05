from project.common.validator import Validator


class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    # @staticmethod
    # def __validate_name(value):
    #     if value.strip() == '':
    #         raise ValueError('Planet name cannot be empty string or whitespace!')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # self.__validate_name(value)
        Validator.raise_if_string_is_empty_or_whitespace(value, 'Planet name cannot be empty string or whitespace!')
        self.__name = value
