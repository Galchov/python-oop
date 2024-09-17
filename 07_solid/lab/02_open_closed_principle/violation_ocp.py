class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)


"""
Add a new animal and refactor the code, 
so it works without the need of making changes on it, 
when adding new animals
"""
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
