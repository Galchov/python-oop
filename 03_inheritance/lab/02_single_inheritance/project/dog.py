from project.animal import Animal


class Dog(Animal):
    def bark(self):
        return "barking..."


# Test code:
dog = Dog()
print(dog.bark())
print(dog.eat())

"""
This is a simple example of Single Inheritance - When a child class 
inherits properties from single parent class only.
"""
