from project.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        super().__init__(expiration_date)
        self.name = name


"""
A simple example of using super() built-in function, which allows you to call attributes and 
methods defined in the superclass from the subclass.
"""