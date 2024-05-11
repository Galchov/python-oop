class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


# Test code:
person = Person("George", 32)
print(person.get_name())
print(person.get_age())

"""
__name and __age are private, which mean they are not accessed outside the class by convention, 
unless using name mangling, e.g., _Person__name, _Person__age.
"""
