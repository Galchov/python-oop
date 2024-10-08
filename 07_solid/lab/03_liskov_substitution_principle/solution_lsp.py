"""
If the functionality (attributes and methods) of the base class don't apply for the subclass,
that means the subclass is not substitutable for the base class. Basic inheritance rule.

Here is the refactored code, where the bad practice of throwing an error for not applicable
functionality is removed, and the subclass 'RubberDuck' is made an independent class.

Liskov Substitution Principle -> Subtypes must be substitutable for their base types.
"""


from abc import ABC, abstractmethod


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck:
    @staticmethod
    def quack():
        return "Squeek"

    # @staticmethod
    # def walk():
    #     """Rubber duck can walk only if you move it"""
    #     raise Exception('I cannot walk by myself')
    #
    # @staticmethod
    # def fly():
    #     """Rubber duck can fly only if you throw it"""
    #     raise Exception('I cannot fly by myself')


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
