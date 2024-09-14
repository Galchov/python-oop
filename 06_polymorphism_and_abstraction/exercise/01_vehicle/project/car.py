from project.vehicle import Vehicle


class Car(Vehicle):
    AIR_CON = 0.9

    def drive(self, distance: int) -> None:
        consumption = (self.fuel_consumption + Car.AIR_CON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


# Test code:

# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
