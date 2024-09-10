"""Simple example of using 'Static Methods', defined within a class without being tied to
the class'/instance's state or behaviour. They are based in the class, only to provide
some functionality when we need it later"""

from functools import reduce


class Calculator:

    @staticmethod
    def add(*nums):
        return reduce(lambda x, y: x + y, nums)

    @staticmethod
    def multiply(*nums):
        return reduce(lambda x, y: x * y, nums)

    @ staticmethod
    def divide(*nums):
        return reduce(lambda x, y: x / y, nums)

    @staticmethod
    def subtract(*nums):
        return reduce(lambda x, y: x - y, nums)


# Test code:
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))
