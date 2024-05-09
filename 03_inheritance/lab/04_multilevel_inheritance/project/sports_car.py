from project.car import Car


class SportsCar(Car):
    def race(self):
        return "racing..."


# Test code:
racing_car = SportsCar()
print(racing_car.race())
print(racing_car.drive())
print(racing_car.move())

"""
This is an example of Multilevel Inheritance - When a child class 
becomes a parent class for another child class.
"""
