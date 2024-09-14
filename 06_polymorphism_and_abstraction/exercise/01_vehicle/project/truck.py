from project.vehicle import Vehicle


class Truck(Vehicle):
    AIR_CON = 1.6

    def drive(self, distance: int) -> None:
        consumption = (self.fuel_consumption + Truck.AIR_CON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * 0.95


# Test code:

# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
